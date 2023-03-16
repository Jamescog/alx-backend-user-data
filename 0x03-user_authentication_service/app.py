#!/usr/bin/env python3
"""simple flask app to handle authorization and authentication
"""


from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """index route"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run()
