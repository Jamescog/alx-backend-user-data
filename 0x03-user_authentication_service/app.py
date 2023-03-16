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


@app.route('/sessions', methods=["POST"], strict_slashes=False)
def login() -> str:
    """session creator based on credentials"""

    email = request.form.get("email")
    password = request.form.get("password")

    if None in [email, password]:
        abort(400)

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        msg = {"email": email, "message": "logged in"}
        res = jsonify(msg)
        res.set_cookie("session_id", session_id)
        return res
    abort(401)


if __name__ == "__main__":
    app.run()
