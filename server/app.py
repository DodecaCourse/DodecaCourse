"""
Copyright 2020 Maximilian Herzog, Hans Olischläger, Valentin Pratz,
Philipp Tepel
This file is part of Dodeca Course.

Dodeca Course is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Dodeca Course is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Dodeca Course.  If not, see <https://www.gnu.org/licenses/>.
"""
# dependencies: tinyDB flask flask-cors tinyrecord
from flask import Flask, jsonify, session
from flask_cors import CORS

from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
from tinyrecord import transaction
# standard modules
import string
import random
import importlib
# decorators
from functools import wraps
# files
import config
from read_structure import insert_structure
importlib.reload(config)

# ø Config

# → Database
db = TinyDB("db.json", storage=CachingMiddleware(JSONStorage))
# db.purge()  # removed comments if you want to reset the database

db.purge_table('modules')
db.purge_table('chapters')
db.purge_table('targets')

# DATABASE
# User(user_id, user_keyword, settings...) (for settings see config)
users = db.table('users')
# Take(take_id, ↑user_id, ↑target_id, time_spend, finished)
takes = db.table('takes')
# module(module_id)
modules = db.table('modules')
# chapter(chapter_id, ↑module_id)
chapters = db.table('chapters')
# Target(target_id, ↑chapter_id)
targets = db.table('targets')

# Read Modules Chapters and Targets from static public/structure.json
insert_structure("../public/structure.json", modules, chapters, targets,
                 output=config.Config.DEBUG)
db.storage.flush()  # close after inserting data

# → Start Query
q = Query()
# Users waiting for confirmation
temp_keywords = set()

# → General App-Conifg
# ..read out of config.py(.env)!
app = Flask(__name__)
importlib.reload(config)
app.config.from_object(config.Config)
# CORS allows us to restrict the access to the FRONTEND_SERVER
CORS(app, origins=[config.Config.FRONTEND_SERVER], headers=['Content-Type'],
     expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)


# Decorators to check input
def check_user_id(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if not users.contains(eids=[kwargs['user_id']]):
            app.logger.warning("QUERY: Found invalid user_id "
                               + str(kwargs['user_id'])
                               + ". User does not exist.")
            return jsonify("Found invalid user_id " + str(kwargs['user_id'])
                           + ". User does not exist.")
        return func(*args, **kwargs)
    return decorated


def check_target_id(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if not targets.contains(q['target_id'] == kwargs['target_id']):
            app.logger.warning("QUERY: Found invalid target_id "
                               + str(kwargs['target_id'])
                               + ". Target does not exist.")
            return jsonify("Found invalid target_id "
                           + str(kwargs['target_id'])
                           + ". Target does not exist.")
        return func(*args, **kwargs)
    return decorated


def check_chapter_id(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if not chapters.contains(q['chapter_id'] == kwargs['chapter_id']):
            app.logger.warning("QUERY: Found invalid chapter_id "
                               + str(kwargs['chapter_id'])
                               + ". Chapter does not exist.")
            return jsonify("Found invalid chapter_id "
                           + str(kwargs['chapter_id'])
                           + ". Chapter does not exist.")
        return func(*args, **kwargs)
    return decorated


def check_setting_name(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        setting_names = [*config.Config.DEFAULT_SETTINGS.keys()]
        if not kwargs["setting_name"] in setting_names:
            app.logger.warning("QUERY: Found invalid setting_name "
                               + str(kwargs['setting_name'])
                               + ".")
            return jsonify("Found invalid setting_name "
                           + str(kwargs['setting_name'])
                           + ".")
        return func(*args, **kwargs)
    return decorated


def is_user(user_key):
    return not (len(users.search(q['user_keyword'] == user_key)) == 0)

# currently unused, will delete later
# def get_completed_chapters(completed_targets):
#     ret_chapters = []
#     empty_chapters = []
#     for c in chapters.all():
#         id = int(c['chapter_id'])
#         chapter_targets = targets.search(q['chapter_id'] == id)
#         print(id, chapter_targets)
#         if len(chapter_targets) == 0:
#             empty_chapters.append(id)
#             # return jsonify("error on searching for targets, chaper emtpy?")
#         else:
#             completed_chapter = True
#             for t in chapter_targets:
#                 if not t['target_id'] in completed_targets:
#                     completed_chapter = False
#                     break
#
#             if completed_chapter:
#                 ret_chapters.append(id)
#     return ret_chapters, empty_chapters


# def get_completed_modules(completed_chapters, empty_chapters):
#     ret_modules = []
#     no_test_modules = []
#     for m in modules.all():
#         id = int(m['module_id'])
#         module_chapters = chapters.search(q['module_id'] == id)
#         if len(module_chapters) == 0:
#             return jsonify("error on searching for chapters, module emtpy?")
#         completed_module = True
#         no_test_module = True
#         for c in module_chapters:
#             if not c['chapter_id'] in completed_chapters:
#                 if not c['chapter_id'] in empty_chapters:
#                     completed_module = False
#                     break
#             if no_test_module:
#                 if c['chapter_id'] in empty_chapters:
#                     no_test_module = False
#
#         if completed_module:
#             ret_modules.append(id)
#         if no_test_module:
#             no_test_modules.append(id)
#     return ret_modules, no_test_modules


# ø App Routes

#   * Datenbank Stuff

# @app.route('/adduser', methods=['POST'])
# def adduser():
#     user = request.form['nm']
#     # session['userID'] = user
#     # print("POST: Set session['userID'] to " + user)
#     if not is_user(user):
#         with transaction(users) as tr:
#             tr.insert({'user_keyword': user})
#         return redirect('http://localhost:8080/dev/servertest')
#     else:
#         return jsonify('user with keyword ' + user + ' already exists.')


@app.route('/generate_user_keyword')
def generate_user_keyword():
    """
    Generates random user keyword, that is compatible with the current
    users database.

    Returns:
        url: redirect to original site

    Raises:
        Exception: Raises exception when all possible keywords are taken and
            therefore no new user keywords could be generated.

    """
    # get user keyword length from config.py
    lenkey = config.Config.USER_KEYWORD_LENGTH
    set = string.ascii_letters.replace('l', '').replace('I', '')\
        .replace('O', '') + string.digits.replace('0', '')
    set
    max_amount_of_user_keys = len(set)**lenkey
    for i in range(max_amount_of_user_keys):
        user = ''.join(random.choice(set) for j in range(lenkey))
        if not is_user(user):
            temp_keywords.add(user)
            return jsonify(user)
    raise Exception("Could not allocate another user. All keywords are taken."
                    " You should increase USER_KEYWORD_LENGTH in settings.")


@app.route('/confirm_user_keyword/<user>')
def confirm_user_keyword(user):
    """
    Creates user for generated keyword awaiting confirmation

    Returns:
        url: result of set_current_user
    """
    if user in temp_keywords and not is_user(user):
        with transaction(users) as tr:
            tr.insert({'user_keyword': user})
        db.storage.flush()
        temp_keywords.remove(user)
        print(temp_keywords)
        return set_current_user(user)
    raise Exception("Could not confirm user.")


@app.route('/getuser_bykey/<user_key>')
def get_user_by_key(user_key):
    found = users.search(q['user_keyword'] == user_key)
    if len(found) == 0:
        app.logger.warning('QUERY: No user with user_keyword=='
                           + str(user_key) + ' has been found.')
        return jsonify(None)
    elif len(found) > 1:
        app.logger.warning('QUERY: Multiple user have the same user_keyword \''
                           + str(user_key) + '\'.\n Returning first found '
                           'instance')
    lchap = None
    if 'logoff_chapter' in found[0].keys():
        lchap = found[0]['logoff_chapter']

    like = False
    if 'like' in found[0].keys():
        like = found[0]["like"]

    # get settings
    setting_names = [*config.Config.DEFAULT_SETTINGS.keys()]
    settings = {}
    for setting_name in setting_names:
        if setting_name in found[0].keys():
            settings[setting_name] = found[0][setting_name]
        else:
            settings[setting_name] = \
                config.Config.DEFAULT_SETTINGS[setting_name]

    return jsonify({
        'user_id': found[0].eid,
        'user_keyword': found[0]['user_keyword'],
        'logoff_chapter': lchap,
        'like': like,
        'settings': settings
    })


@app.route('/set_logoff_chapter/<int:user_id>/<int:chapter_id>')
@check_user_id
@check_chapter_id
def set_logoff_chapter(user_id, chapter_id):
    found = users.update({
                         'logoff_chapter': chapter_id
                         }, eids=[user_id])
    if len(found) == 0:
        app.logger.error('QUERY: No user found with user_id ' + str(user_id))
        return jsonify(None)
    db.storage.flush()
    return jsonify("success on setting logoff_chapter on user " + str(user_id)
                   + " to " + str(chapter_id))


@app.route('/complete_target/<int:user_id>/<int:target_id>/<int:level>')
@check_user_id
@check_target_id
def complete_target(user_id, target_id, level):
    found = takes.upsert({
                            'completed': True,
                            'user_id': user_id,
                            'target_id': target_id,
                            'level': level
                         }, (q['user_id'] == user_id)
                         & (q['target_id'] == target_id)
                         & (q['level'] == level))
    if len(found) > 1:
        app.logger.warning('QUERY: Multiple takes entries with same'
                           ' target_id, user_id & level have been found.'
                           ' Updating all instances')
    # update if entry exists
    # found = takes.search((q['target_id'] == target_id)
    #                      & (q['user_id'] == user_id))
    # if len(found) == 0:
    #     # create if not
    #     with transaction(takes) as tr:
    #         tr.insert({
    #             'user_id': user_id,
    #             'target_id': target_id,
    #             'level': level,
    #             'completed': True
    #         })
    # else:
    #   if len(found) > 1:
    #       app.logger.warning('QUERY: Multiple takes entries with same'
    #                          ' target_id, user_id & level have been found.'
    #                          ' Updating all instances')
    #     takes.update({'completed': True}, (q['user_id'] == user_id)
    #                  & (q['target_id'] == target_id)
    #                  & (q['level'] == level))
    db.storage.flush()
    return jsonify("User \'" + str(user_id) + "\' succesfully took target \'"
                   + str(target_id) + "\' on level \'" + str(level) + "\'")


@app.route('/unset_complete_target/<int:user_id>/<int:target_id>/<int:level>')
@check_user_id
@check_target_id
def unset_complete_target(user_id, target_id, level):
    # set completed to false if take exists
    found = takes.upsert({
                            'completed': False,
                            'user_id': user_id,
                            'target_id': target_id,
                            'level': level
                         }, (q['user_id'] == user_id)
                         & (q['target_id'] == target_id)
                         & (q['level'] == level))
    if len(found) > 1:
        app.logger.warning('QUERY: Multiple takes entries with same'
                           ' target_id, user_id & level have been found.'
                           ' Updating all instances')
    db.storage.flush()
    return jsonify("User \'" + str(user_id) + "\' reset completed on target \'"
                   + str(target_id) + "\' on level \'" + str(level) + "\'")


# @app.route('/getsettings/<int:user_id>')
# @check_user_id
# def get_user_settings(user_id):
#     usr = users.get(eid=user_id)
#     setting_names = [*config.Config.DEFAULT_SETTINGS.keys()]
#     N = len(setting_names)
#     returned_settings = {}
#     for i in range(N):
#         if setting_names[i] in usr.keys():
#             returned_settings[setting_names[i]] = usr[setting_names[i]]
#         else:
#             returned_settings[setting_names[i]] = \
#                 config.Config.DEFAULT_SETTINGS[setting_names[i]]
#     return jsonify(returned_settings)

@app.route('/setsetting/<int:user_id>/<setting_name>/<int:value>')
@check_user_id
@check_setting_name
def set_setting(user_id, setting_name, value):
    users.update({"setting_name": value}, eids=[user_id])
    return jsonify("sucess on setting " + str(setting_name) + " to "
                   + str(value) + " at user " + str(user_id))


@app.route('/get_takes_by_user_id/<int:user_id>')
@check_user_id
def get_user_takes(user_id):
    foundtakes = takes.search(q['user_id'] == user_id)
    N = len(foundtakes)
    ret_targets = {}
    for i in range(N):
        take = foundtakes[i]
        # TODO: Add error when eid in target does not exist
        # TODO: Add error when take is missing keys
        # Using try except for now
        if not take['target_id'] in ret_targets:
            ret_targets[take['target_id']] = {}
        ret_targets[take['target_id']][take['level']] = {
            'take_id': take.eid,
            'target_id': take['target_id'],
            # 'time_spend': take['time_spend'],
            'completed': take['completed']
        }
    return jsonify(ret_targets)

# currently unused, will delete later
# @app.route('/get_completed_by_user_id/<int:user_id>')
# @check_user_id
# def get_completed_by_user_id(user_id):
#     """
#     Returns lists of
#         completed_modules, completed_chapters and completed_targets
#     by analyzing the structure and takes matching the user_id
#     """
#     # search all takes
#     foundtakes = takes.search(q['user_id'] == user_id)
#     N = len(foundtakes)
#     ret_targets = [0] * N
#     for i in range(N):
#         take = foundtakes[i]
#         tar = targets.search(q['target_id'] == take['target_id'])
#         if not len(tar) == 1:
#             return jsonify("error on searching for targets")
#         ret_targets[i] = tar[0]['target_id']
#     ret_chapters, empty_chapters = get_completed_chapters(ret_targets)
#     print(ret_chapters, empty_chapters)
#     ret_modules, no_test_modules = get_completed_modules(ret_chapters,
#                                                          empty_chapters)
#     print(ret_modules, no_test_modules)
#
#     return jsonify({
#                     "targets": ret_targets,
#                     "chapters": ret_chapters,
#                     "empty_chapters": empty_chapters,
#                     "modules": ret_modules,
#                     "no_test_modules": no_test_modules
#                    })


@app.route('/set_like/<int:user_id>/<int:like_int>')
@check_user_id
def set_like(user_id, like_int):
    like = (like_int == 1)
    # found = users.update({'like': like}, eids=[user_id])
    users.update({'like': like}, eids=[user_id])
    # print(len(found))
    # if len(found) > 1:
    #     app.logger.warnign("QUERY: Multiple users with user_id "
    # + str(user_id)
    #                        + "found!")
    db.storage.flush()
    return jsonify("success on setting like=" + str(like) + " on user "
                   + str(user_id))


@app.route('/get_likes/')
def get_likes():
    found = users.search(q["like"])
    # print(found)
    return jsonify(len(found))


#   * Cookie Stuff

@app.route('/setcurrentuser/<user_keyword>')
def set_current_user(user_keyword):
    # ret = jsonify("Success on setcurrentuser to " + str(user_keyword))
    # resp = make_response(ret)
    # TODO: Fix
    # resp.set_cookie('user_keyword', value=user_keyword,
    #                 domain='domain.local')
    session['user_keyword'] = user_keyword
    print("Set cookie user_keyword to \'" + user_keyword + "\'")
    return get_user_by_key(user_keyword)


@app.route('/getcurrentuser')
def get_current_user():
    # print(session)
    if not'user_keyword' in session.keys():
        return jsonify(None)
    user_keyword = session['user_keyword']
    return get_user_by_key(user_keyword)


@app.route('/logout')
def logout():
    session.clear()
    return jsonify('success')

# handle withCredentials
# TODO: Read about credentials for further info

# @app.after_request
# def handle_credentials(response):
#     response.headers["Access-Control-Allow-Credentials"] = True
#     return response


# LETS GO
if __name__ == '__main__':
    app.run()
