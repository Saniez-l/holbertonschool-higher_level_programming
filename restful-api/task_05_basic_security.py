#!/usr/bin/python3
"""
API Security and Authentication Techniques
"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import get_jwt

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    """
    Verifie password
    """
    if username in users and \
            check_password_hash(users.get(username)["password"], password):
        return username

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def index():
    """
    Return sentence
    """
    return "Basic Auth: Access Granted"

#...............................................................................

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Unauthorized"}), 401

    access_token = create_access_token(identity=username, additional_claims={"role": user["role"]})
    return jsonify(access_token=access_token)


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()


def protected():
    # Access the identity of the current user with get_jwt_identity
    
    current_user = get_jwt_identity()
    return jsonify({"msg": "JWT Auth: Access Granted"}), 200

@jwt.unauthorized_loader
def missing_token_callback(err):
    return jsonify({"error": "Unauthorized"}), 401

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin():
    
    claims = get_jwt()         
    role = claims.get("role", None)

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return("Admin Access: Granted"), 200
#..................................................
if __name__ == '__main__':
    app.run()
