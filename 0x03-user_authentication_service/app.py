#!/usr/bin/env python3
"""simple flask app to handle authorization and authentication
"""


from flask import Flask, jsonify, request, abort
from auth import Auth
AUTH = Auth()


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """index route"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """Registers a new user if it does not exist before"""
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    msg = {"email": email, "message": "user created"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run()
