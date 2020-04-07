# dependencies: tinyDB flask flask-cors tinyrecord
from flask import Flask, jsonify, request, redirect
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

# ø Datenbank laden
# TODO

# ø Konfiguration

# → Datenbank
db = TinyDB("db/db.json",
            storage=CachingMiddleware(JSONStorage))
# db.purge() # Datenbank clearen
# DATENBANKSTRUKTUR
# User(user_id, user_keyword, settings...) (for settings see config)
users = db.table('users')
# Takes(take_id, ↑user_id, ↑target_id, time_spend, finished)
takes = db.table('takes')
# targets(target_id, ↑chapter_id)
targets = db.table('targets')
# chapter(chapter_id, ↑module_id, chapter_name)
chapters = db.table('chapters')
# module(module_id, module_name)
modules = db.table('modules')

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
CORS(app, resources={r'/*': {'origins': '*'}})


# ø Utility Funktionen

def is_user(user_key):
    return not (len(users.search(q['user_keyword'] == user_key)) == 0)


def is_integer_string(string):
    # TODO: elegantere Methode zum herausfilter, von nicht integern
    return bool(re.match("-?\\d+", string))


# ø App Routes

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


@app.route('/generateuser', methods=['POST', 'GET'])
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
            return redirect('http://localhost:8080/dev/servertest')
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


@app.route('/getchapters_bymodule_id/<module_id>')
def get_chapters_bymoduleid(module_id):
    if not bool(re.match("-?\\d+", module_id)):
        app.logger.warning('QUERY: Found invalid module_id \''
                           + str(module_id) + '\'. Input integers! ')
        return jsonify('Found invalid module_id')
    module_id = int(module_id)
    found = chapters.search(q['module_id'] == module_id)
    N = len(found)
    if N == 0:
        app.logger.warning('QUERY: No chapters with module_id=='
                           + str(module_id) + ' had been found.')
        return jsonify('no chapter in module \'' + str(module_id)
                       + '\' were found')
    found_chapters = [None] * N
    for i in range(len(found)):
        sect = found[i]
        found_chapters[i] = {
            'chapter_id': sect.eid,
            'module_id': sect['module_id'],
            'chapter_name': sect['chapter_name']
        }
    return jsonify(found_chapters)


@app.route('/get_targets_bychapter_id/<chapter_id>')
def get_targets_by_chapter_id(chapter_id):
    if not is_integer_string(chapter_id):
        app.logger.warning('QUERY: Found invalid chapter_id \''
                           + str(chapter_id) + '\'. Input integers! ')
        return jsonify('Found invalid chapter_id')
    chapter_id = int(chapter_id)
    found = targets.search(q['chapter_id'] == chapter_id)
    N = len(found)
    if N == 0:
        app.logger.warning('QUERY: No targets with chapter_id=='
                           + str(chapter_id) + ' had been found.')
        return jsonify('no targets in chapter \'' + str(chapter_id)
                       + '\' were found')
    found_targets = [None] * N
    for i in range(len(found)):
        lvl = found[i]
        found_targets[i] = {
            'target_id': lvl.eid,
            'chapter_id': lvl['chapter_id']
        }
    return jsonify(found_targets)


@app.route('/getuser_bykey/<user_key>')
def get_user_by_key(user_key):
    found = users.search(q['user_keyword'] == user_key)
    if len(found) == 0:
        app.logger.warning('QUERY: No user with user_keyword=='
                           + str(user_key) + ' has been found.')
        return jsonify('user with keyword \'' + user_key + '\' was not found')
    elif len(found) > 1:
        app.logger.warning('QUERY: Multiple user have the same user_keyword \''
                           + str(user_key) + '\'.\n Returning first found '
                           'instance')
    return jsonify({
        'user_id': found[0].eid,
        'user_keyword': found[0]['user_keyword']
    })


@app.route('/takechapter/<user_id>/<chapter_id>/<time_spend>')
def take_chapter(user_id, chapter_id, time_spend):
    # Check if all arguments are valid first
    # → user_id
    # TODO: Same wie oben(get_user_by_key), vllt in Methode packen
    # ist nur schwierig, da wir Fehlermeldungen returnen müssen
    if not is_integer_string(user_id):
        app.logger.warning('QUERY: Found invalid user_id \''
                           + str(user_id) + '\'. Input integers! ')
        return jsonify('Found invalid user_id')
    user_id = int(user_id)
    if not users.contains(eids=[user_id]):
        app.logger.warning("QUERY: Found invalid user_id " + str(user_id)
                           + " found. User does not exist.")
        return jsonify("Found invalid user_id " + str(user_id) + " found."
                       " User does not exist.")
    # → chapter_id
    if not is_integer_string(chapter_id):
        app.logger.warning('QUERY: Found invalid chapter_id \''
                           + str(chapter_id) + '\'. Input integers! ')
        return jsonify('Found invalid chapter_id')
    chapter_id = int(chapter_id)
    if not users.contains(eids=[chapter_id]):
        app.logger.warning("QUERY: Found invalid chapter_id " + str(chapter_id)
                           + " found. chapter does not exist.")
        return jsonify("Found invalid chapter_id " + str(user_id) + " found."
                       " chapter does not exist.")
    # → time_spend
    if not is_integer_string(time_spend):
        app.logger.warning('QUERY: Found invalid time_spend \''
                           + str(time_spend) + '\'. Input integers! ')
        return jsonify('Found invalid time_spend. Expected integer.')
    # Magic starts here
    # check if entry already exists
    found = takes.search((q['user_id'] == user_id)
                         & (q['chapter_id'] == chapter_id))
    if len(found) == 0:
        with transaction(takes) as tr:
            tr.insert({
                'user_id': user_id,
                'chapter_id': chapter_id,
                'time_spend': time_spend
            })
    else:
        if len(found) > 1:
            app.logger.warning('QUERY: Multiple takes entries with same'
                               ' chapter_id and user_id have been found.'
                               ' Updating first found instance')
        found[0]['time_spend'] = time_spend
    return jsonify("User \'" + str(user_id) + "\' succesfully took chapter \'"
                   + str(chapter_id) + "\'")


@app.route('/getsettings/<user_id>')
def get_user_settings(user_id):
    if not is_integer_string(user_id):
        app.logger.warning('QUERY: Found invalid user_id \''
                           + str(user_id) + '\'. Input integers! ')
        return jsonify('Found invalid user_id')
    user_id = int(user_id)
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


@app.route('/getchapters_byuser_id/<user_id>')
def get_user_levles(user_id):
    if not is_integer_string(user_id):
        app.logger.warning('QUERY: Found invalid user_id \''
                           + str(user_id) + '\'. Input integers! ')
        return jsonify('Found invalid user_id')
    user_id = int(user_id)
    if not users.contains(eids=[user_id]):
        app.logger.warning("QUERY: Found invalid user_id " + str(user_id)
                           + ". User does not exist.")
        return jsonify("Found invalid user id " + str(user_id) + "."
                       " User does not exist.")
    # user_id valid
    foundtakes = takes.search(q['user_id'] == user_id)
    N = len(foundtakes)
    ret_targets = [{}] * N
    for i in range(N):
        take = foundtakes[i]
        # TODO: Add error when eid in target does not exist
        # TODO: Add error when take is missing keys
        # Using try except for now
        lvl = targets.get(eid=take['target_id'])
        ret_targets[i] = {
            'take_id': take.eid,
            'chapter_id': lvl.eid,
            'chapter_name': lvl['chapter_name'],
            'time_spend': take['time_spend'],
            'finished': take['finished']
        }
    return jsonify(ret_targets)


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


# LETS GO
if __name__ == '__main__':
    app.run()
