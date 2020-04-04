# dependencies: tinyDB flask flask-cors
from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from tinydb import TinyDB, Query
# standard modules
from random import randint
import string
import random
import re
# files
import config


# ø Konfiguration

# → Datenbank
db = TinyDB("db/db.json")
# db.purge() # Datenbank clearen
# DATENBANKSTRUKTUR
# User(user_id, user_keyword)
users = db.table('users')
# Takes(↑user_id, ↑section_id, time_spend)
takes = db.table('takes')
# Section(section_id, ↑chapter_id, section_name)
sections = db.table('sections')
# Chapter(chapter_id, chapter_name)
chapters = db.table('chapters')

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


# ø App Routes

@app.route('/adduser', methods=['POST'])
def adduser():
    user = request.form['nm']
    # session['userID'] = user
    # print("POST: Set session['userID'] to " + user)
    if not is_user(user):
        users.insert({'user_keyword': user})
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
            users.insert({'user_keyword': user})
            return redirect('http://localhost:8080/dev/servertest')
    raise Exception("Could not allocate another user. All keywords are taken."
                    " You should increase USER_KEYWORD_LENGTH in settings.")


@app.route('/getallusers', methods=['GET'])
def get_all_users():
    # user = session.get('userID', 'userID not set')
    # print(config.Config.SESSION_TYPE)
    # if 'userID' in session:
    #     user = session['userID']
    # else:
    #     user = 'not set'
    # user = session.get('userID', 'userID not set')
    # print("GET: Got session['userID'] = " + str(user))
    return jsonify(users.all())


@app.route('/getallchapters')
def get_all_chapters():
    return jsonify(chapters.all())


@app.route('/getallsections')
def get_all_sections():
    return jsonify(sections.all())


@app.route('/getsections_bychapter_id/<chapter_id>')
def get_sections_bychapterid(chapter_id):
    # TODO: elegantere Methode zum herausfilter, von nicht integern
    if not bool(re.match("-?\\d+", chapter_id)):
        app.logger.warning('QUERY: Found invalid chapter_id \''
                           + str(chapter_id) + '\'. Input integers! ')
        return jsonify('Found invalid chapter_id')
    chapter_id = int(chapter_id)
    print(chapter_id)
    found = sections.search(q['chapter_id'] == chapter_id)
    print(found)
    N = len(found)
    if N == 0:
        app.logger.warning('QUERY: No sections with chapter_id=='
                           + str(chapter_id) + ' had been found.')
        return jsonify('no section in chapter \'' + str(chapter_id)
                       + '\' were found')
    found_sections = [None] * N
    for i in range(len(found)):
        sect = found[i]
        found_sections[i] = {
            'section_id': sect.eid,
            'chapter_id': sect['chapter_id'],
            'section_name': sect['section_name']
        }
    return jsonify(found_sections)


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
    print(response)
    return jsonify(response)


# LETS GO
if __name__ == '__main__':
    app.run()
