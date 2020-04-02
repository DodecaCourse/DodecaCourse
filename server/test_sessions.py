from flask import session, Flask, jsonify, request, redirect
from flask_cors import CORS
from random import randint
import config

# Später auskommentieren
DEBUG = True

app = Flask(__name__)
app.config.from_object(config.Config)
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/set', methods=['POST'])
def set():
    user = request.form['nm']
    session['userID'] = user
    print("POST: Set session['userID'] to " + user)
    return redirect('http://localhost:8080/dev/servertest')


@app.route('/get', methods=['GET'])
def get():
    # user = session.get('userID', 'userID not set')
    # print(config.Config.SESSION_TYPE)
    # if 'userID' in session:
    #     user = session['userID']
    # else:
    #     user = 'not set'
    user = session.get('userID', 'userID not set')
    print("GET: Got session['userID'] = " + str(user))
    return jsonify(user)


@app.route('/random')
def random():
    response = {
        'rand': randint(1, 100)
    }
    print(response)
    return jsonify(response)


# LETS GO
if __name__ == '__main__':
    app.run()
