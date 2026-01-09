from flask import Blueprint, request, jsonify
from app import db
from models.user import User
from schemas.user_schema import UserInSchema, UserOutSchema

users_bp = Blueprint("users", __name__)

@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    errors = UserInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return UserOutSchema().jsonify(user), 201

@users_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return UserOutSchema(many=True).jsonify(users), 200

@users_bp.route("/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    return UserOutSchema().jsonify(user), 200

@users_bp.route("/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    errors = UserInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return UserOutSchema().jsonify(user), 200

@users_bp.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Utilisateur supprimé"}), 200
