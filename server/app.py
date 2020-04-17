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
# decorators
from functools import wraps
# files
import config
from read_structure import insert_structure
# ø Datenbank laden
# TODO

# ø Konfiguration

# → Datenbank
db = TinyDB("db.json", storage=CachingMiddleware(JSONStorage))
# db.purge()  # Datenbank clearen

db.purge_table('modules')
db.purge_table('chapters')
db.purge_table('targets')

# DATENBANKSTRUKTUR
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

# Modules Chapters und targets aus structure.json lesen
insert_structure("../public/structure.json", modules, chapters, targets)
db.storage.flush()  # close after inserting data

# → Query starten
# TODO: Sollte man hier jedes mal die Query neu initialisieren oder oben
# einmal starten?
q = Query()

# → Allgemeine App-Konfiguration
# wird aus config.py(und .env) geladen!
app = Flask(__name__)
app.config.from_object(config.Config)
# CORS ermöglicht es, Regeln für den Zugriff festzulegen.
# Wir wollen hier alle Zugriffe erlauben.
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


@app.route('/generateuser')
def generate_user():
    """
    Generates random user keyword, that is compatible with the current
    users database.

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
    set = string.ascii_letters + string.digits
    max_amount_of_user_keys = len(set)**lenkey
    for i in range(max_amount_of_user_keys):
        user = ''.join(random.choice(set) for j in range(lenkey))
        if not is_user(user):
            with transaction(users) as tr:
                tr.insert({'user_keyword': user})
            # db.close()
            db.storage.flush()
            return jsonify(user)
    raise Exception("Could not allocate another user. All keywords are taken."
                    " You should increase USER_KEYWORD_LENGTH in settings.")


# @app.route('/getchapters_bymodule_id/<module_id>')
# def get_chapters_bymoduleid(module_id):
#     if not bool(re.match("-?\\d+", module_id)):
#         app.logger.warning('QUERY: Found invalid module_id \''
#                            + str(module_id) + '\'. Input integers! ')
#         return jsonify('Found invalid module_id')
#     module_id = int(module_id)
#     found = chapters.search(q['module_id'] == module_id)
#     N = len(found)
#     if N == 0:
#         app.logger.warning('QUERY: No chapters with module_id=='
#                            + str(module_id) + ' had been found.')
#         return jsonify('no chapter in module \'' + str(module_id)
#                        + '\' were found')
#     found_chapters = [None] * N
#     for i in range(len(found)):
#         sect = found[i]
#         found_chapters[i] = {
#             'chapter_id': sect.eid,
#             'module_id': sect['module_id'],
#             'chapter_name': sect['chapter_name']
#         }
#     return jsonify(found_chapters)


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
        print("no logoff chapter found")
    return jsonify({
        'user_id': found[0].eid,
        'user_keyword': found[0]['user_keyword'],
        'logoff_chapter': lchap
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


#   * Extra Testing Stuff
# @app.route('/random')
# def rand():
#     """
#     Returns a random integer between 1 and 100.
#
#     Returns:
#         int: random int
#     """
#     response = {
#         'rand': randint(1, 100)
#     }
#     return jsonify(response)


# handle withCredentials
# TODO: Nochmal genau lesen, wie hier die credentials funktionieren

# @app.after_request
# def handle_credentials(response):
#     response.headers["Access-Control-Allow-Credentials"] = True
#     return response


# LETS GO
if __name__ == '__main__':
    app.run()
