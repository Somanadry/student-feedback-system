from flask import Blueprint, request, jsonify
from ..models.user import User
from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint("auth", __name__)

# @auth_bp.route("/register", methods=["POST"])
# def register():
#     data = request.get_json()
#     hashed_pw = generate_password_hash(data["password"])

#     user = User(username=data["username"], password=hashed_pw, role=data["role"])
#     db.session.add(user)
#     db.session.commit()

#     return jsonify({"message": "User created"}), 201
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Missing credentials"}), 400

    hashed_pw = generate_password_hash(data["password"])
    user = User(username=data["username"], password=hashed_pw, role=data["role"])

    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists"}), 400

    return jsonify({"message": "User created"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401

    # token = create_access_token(identity={"username": user.username, "role": user.role})
    token = create_access_token(identity=user.username, additional_claims={"role": user.role})

    return jsonify(access_token=token)

@auth_bp.route("/reset_admin", methods=["POST"])
def reset_admin():
    user = User.query.filter_by(username="admin1").first()
    if user:
        user.password = generate_password_hash("1234")
        db.session.commit()
    return {"message": "admin reset"}
