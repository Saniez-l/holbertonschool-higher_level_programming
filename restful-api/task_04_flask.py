#!/usr/bin/python3
"""
Module for API with flask
"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Route home def
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Def rout data
    Return jsonify user
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Def status
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Def get user
    Return jsonify user
    """
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=['POST'])
def post():
    """
    Def post for add new user
    Return jsonify new user
    """
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    users[username] = {"username": username,"name": name, "age": age, "city": city}

    return jsonify({"user add": users[username]})


if __name__ == "__main__":
    app.run()
