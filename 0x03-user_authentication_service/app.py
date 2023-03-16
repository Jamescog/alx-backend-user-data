#!/usr/bin/env python3
"""simple flask app to handle authorization and authentication
"""


from flask import Flask, jsonify, request, abort
from auth import Auth
Auth = Auth()


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """index route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users():
    """implements the registration of the user"""

    email = request.form.get("email")
    password = request.form.get("password")

    if None in [email, password]:
        abort(400)

    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": email, "email": "user created"}), 201
    except ValueError:
        return jsonify({"error": "email already registered"}), 400


if __name__ == "__main__":
    app.run()
