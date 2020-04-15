# dependencies: tinyDB flask flask-cors tinyrecord
from flask import Flask, jsonify, request, redirect, session
from flask_cors import CORS

from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
from tinyrecord import transaction
# standard modules
from random import randint
import string
import random
import re
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
db.close()  # close after inserting data

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
CORS(app, origins=["http://localhost:8080"], headers=['Content-Type'],
     expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)

# ø Utility Funktionen


def is_user(user_key):
    return not (len(users.search(q['user_keyword'] == user_key)) == 0)


def get_completed_chapters(completed_targets):
    ret_chapters = []
    for c in chapters.all():
        id = c['chapter_id']
        chapter_targets = targets.search(q['chapter_id'] == id)
        if len(chapter_targets) == 0:
            return jsonify("error on searching for targets, chaper emtpy?")
        completed_chapter = True
        for t in chapter_targets:
            if not t['target_id'] in completed_targets:
                completed_chapter = False
                break

        if completed_chapter:
            ret_chapters.append(id)
    return ret_chapters


def get_completed_modules(completed_chapters):
    ret_modules = []
    for m in modules.all():
        id = m['module_id']
        module_chapters = chapters.search(q['module_id'] == id)
        if len(module_chapters) == 0:
            return jsonify("error on searching for chapters, module emtpy?")
        completed_module = True
        for c in module_chapters:
            if not c['chapter_id'] in completed_chapters:
                completed_module = False
                break

        if completed_module:
            ret_modules.append(id)
    return ret_modules


# ø App Routes

#   * Datenbank Stuff

@app.route('/adduser', methods=['POST'])
def adduser():
    user = request.form['nm']
    # session['userID'] = user
    # print("POST: Set session['userID'] to " + user)
    if not is_user(user):
        with transaction(users) as tr:
            tr.insert({'user_keyword': user})
        return redirect('http://localhost:8080/dev/servertest')
    else:
        return jsonify('user with keyword ' + user + ' already exists.')


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
            return jsonify(user)
    raise Exception("Could not allocate another user. All keywords are taken."
                    " You should increase USER_KEYWORD_LENGTH in settings.")


@app.route('/getallusers', methods=['GET'])
def get_all_users():
    return jsonify(users.all())


@app.route('/getallmodules')
def get_all_modules():
    return jsonify(modules.all())


@app.route('/getallchapters')
def get_all_chapters():
    return jsonify(chapters.all())


@app.route('/getalltargets')
def get_all_targets():
    return jsonify(targets.all())


@app.route('/getalltakes')
def get_all_takes():
    return jsonify(takes.all())


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


@app.route('/get_targets_bychapter_id/<int:chapter_id>')
def get_targets_by_chapter_id(chapter_id):
    found = targets.search(q['chapter_id'] == chapter_id)
    N = len(found)
    if N == 0:
        app.logger.warning('QUERY: No targets with chapter_id=='
                           + str(chapter_id) + ' had been found.')
        return jsonify('no targets in chapter \'' + str(chapter_id)
                       + '\' were found')
    found_targets = [None] * N
    for i in range(len(found)):
        tar = found[i]
        found_targets[i] = {
            'target_id': tar.eid,
            'chapter_id': tar['chapter_id']
        }
    return jsonify(found_targets)


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
    return jsonify({
        'user_id': found[0].eid,
        'user_keyword': found[0]['user_keyword']
    })


@app.route('/complete_target/<int:user_id>/<int:target_id>/<int:level>')
def complete_target(user_id, target_id, level):
    # Check if all arguments are valid first
    # → user_id
    # TODO: Same wie oben(get_user_by_key), vllt in Methode packen
    # ist nur schwierig, da wir Fehlermeldungen returnen müssen
    if not users.contains(eids=[user_id]):
        app.logger.warning("QUERY: Found invalid user_id " + str(user_id)
                           + " found. User does not exist.")
        return jsonify("Found invalid user_id " + str(user_id) + " found."
                       " User does not exist.")
    if not targets.contains(q['target_id'] == target_id):
        app.logger.warning("QUERY: Found invalid target_id " + str(target_id)
                           + " found. chapter does not exist.")
        return jsonify("Found invalid target_id " + str(target_id) + " found."
                       " target does not exist.")
    # → time_spend
    # if not is_integer_string(time_spend):
    #     app.logger.warning('QUERY: Found invalid time_spend \''
    #                        + str(time_spend) + '\'. Input integers! ')
    #     return jsonify('Found invalid time_spend. Expected integer.')
    # Magic starts here
    # check if entry already exists
    found = takes.update({'completed': True}, (q['user_id'] == user_id)
                         & (q['target_id'] == target_id)
                         & (q['level'] == level))
    if len(found) == 0:
        with transaction(takes) as tr:
            tr.insert({
                'user_id': user_id,
                'target_id': target_id,
                'level': level,
                'completed': True
            })
    elif len(found) > 1:
        app.logger.warning('QUERY: Multiple takes entries with same'
                           ' target_id, user_id & level have been found.'
                           ' Updating all instances')
    # db.close()
    return jsonify("User \'" + str(user_id) + "\' succesfully took target \'"
                   + str(target_id) + "\' on level \'" + str(level) + "\'")


@app.route('/unset_complete_target/<int:user_id>/<int:target_id>/<int:level>')
def unset_complete_target(user_id, target_id, level):
    # Check if all arguments are valid first
    # → user_id
    # TODO: Same wie oben(get_user_by_key), vllt in Methode packen
    # ist nur schwierig, da wir Fehlermeldungen returnen müssen
    if not users.contains(eids=[user_id]):
        app.logger.warning("QUERY: Found invalid user_id " + str(user_id)
                           + " found. User does not exist.")
        return jsonify("Found invalid user_id " + str(user_id) + " found."
                       " User does not exist.")
    if not targets.contains(q['target_id'] == target_id):
        app.logger.warning("QUERY: Found invalid target_id " + str(target_id)
                           + " found. chapter does not exist.")
        return jsonify("Found invalid target_id " + str(target_id) + " found."
                       " target does not exist.")
    # → time_spend
    # if not is_integer_string(time_spend):
    #     app.logger.warning('QUERY: Found invalid time_spend \''
    #                        + str(time_spend) + '\'. Input integers! ')
    #     return jsonify('Found invalid time_spend. Expected integer.')
    # Magic starts here
    # set completed to false if take exists
    found = takes.update({'completed': False}, (q['user_id'] == user_id)
                         & (q['target_id'] == target_id)
                         & (q['level'] == level))
    # db.close()
    return jsonify("User \'" + str(user_id) + "\' reset completed on target \'"
                   + str(target_id) + "\' on level \'" + str(level) + "\'")


@app.route('/getsettings/<int:user_id>')
def get_user_settings(user_id):
    if not users.contains(eids=[user_id]):
        app.logger.warning("QUERY: Found invalid user_id " + str(user_id)
                           + ". User does not exist.")
        return jsonify("Found invalid user id " + str(user_id) + "."
                       " User does not exist.")
    # user_id valid
    usr = users.get(eid=user_id)
    setting_names = [*config.Config.DEFAULT_SETTINGS.keys()]
    N = len(setting_names)
    returned_settings = {}
    for i in range(N):
        if setting_names[i] in usr.keys():
            returned_settings[setting_names[i]] = usr[setting_names[i]]
        else:
            returned_settings[setting_names[i]] = \
                config.Config.DEFAULT_SETTINGS[setting_names[i]]
    return jsonify(returned_settings)


@app.route('/get_takes_by_user_id/<int:user_id>')
def get_user_takes(user_id):
    if not users.contains(eids=[user_id]):
        app.logger.warning("QUERY: Found invalid user_id " + str(user_id)
                           + ". User does not exist.")
        return jsonify("Found invalid user id " + str(user_id) + "."
                       " User does not exist.")
    # user_id valid
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

@app.route('/get_completed_by_user_id/<int:user_id>')
def get_completed_by_user_id(user_id):
    """
    Returns lists of
        completed_modules, completed_chapters and completed_targets
    by analyzing the structure and takes matching the user_id
    """
    if not users.contains(eids=[user_id]):
        app.logger.warning("QUERY: Found invalid user_id " + str(user_id)
                           + ". User does not exist.")
        return jsonify("Found invalid user id " + str(user_id) + "."
                       " User does not exist.")
    # user_id valid
    # search all takes
    foundtakes = takes.search(q['user_id'] == user_id)
    N = len(foundtakes)
    ret_targets = [{}] * N
    for i in range(N):
        take = foundtakes[i]
        tar = targets.search(q['target_id'] == take['target_id'])
        if not len(tar) == 1:
            return jsonify("error on searching for targets")
        ret_targets[i] = tar['target_id']
    ret_chapters = get_completed_chapters(ret_targets)
    ret_modules = get_completed_modules(ret_chapters)

    return jsonify({
                    "targets": ret_targets,
                    "chapters": ret_chapters,
                    "modules": ret_modules
                   })

#   * Cookie Stuff


@app.route('/setcurrentuser/<user_keyword>')
def set_current_user(user_keyword):
    ret = jsonify("Success on setcurrentuser to " + str(user_keyword))
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
    # if not'user_keyword' in session.keys():
    #     print("hä?")
    #     return jsonify("no current user set")
    # TODO: Fix this trash
    # Hat noch keinen Error produziert
    # try:
    # for key in session.keys():
    #     session.pop(key)
    # session.clear()
    # TODO: extrem hässliches Workaround, aber funktioniert auch noch nicht
    session.clear()
    return jsonify('success')
    # do not use bare except(meme)
    # except:
    # print("an error occured on logout, while trying to delete the session")
    # return jsonify("err")


# @app.route('/getcurrentuser_withid')
# def get_current_user_with_id():
#     user_key = request.cookies.get('user_keyword')
#     if user_key is None:
#         return jsonify("no current user set")
#     user = {
#         'user_keyword': user_key,
#         'user_id': request.cookies.get('user_id')
#     }
#     return jsonify(user)

#   * Extra Testing Stuff


@app.route('/random')
def rand():
    """
    Returns a random integer between 1 and 100.

    Returns:
        int: random int
    """
    response = {
        'rand': randint(1, 100)
    }
    return jsonify(response)


# handle withCredentials
# TODO: Nochmal genau lesen, wie hier die credentials funktionieren

# @app.after_request
# def handle_credentials(response):
#     response.headers["Access-Control-Allow-Credentials"] = True
#     return response


# LETS GO
if __name__ == '__main__':
    app.run()
