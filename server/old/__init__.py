"""Initialize application."""
from flask import Flask, jsonify
from flask_session import Session
from random import randint

sess = Session()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    # ...
    sess.init_app(app)

    @app.route('/api/random')
    def random_number():
        response = {
            'randomNumber': randint(1, 100)
        }
        return jsonify(response)

    return app
