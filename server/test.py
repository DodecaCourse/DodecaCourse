from flask import *
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
# @app.route('/ping', methods=['POST', 'GET'])
# def ping_pong():
#     return jsonify('pong! hehe, test<b>TEST</b>')
@app.route('/setcookie', methods=['POST', 'GET'])
def ping_pong():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response("test")
        resp.set_cookie('userID', user)
        print("#---- Set cookie on userID", user)
        print(request.url)
        redirect(request.url)
        return("cookie['userId']:", user)
    return("no cookie set")

@app.route('/getcookie', methods=['GET'])
def getcookie():
   name = request.cookies.get('userID')
   return jsonify(name)

if __name__ == '__main__':
    app.run()
