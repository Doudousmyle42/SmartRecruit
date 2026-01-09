from flask import Blueprint, request, jsonify
from app import db
from models.cours import Cours
from schemas.cours_schema import CoursInSchema, CoursOutSchema

cours_bp = Blueprint("cours", __name__)

@cours_bp.route("/", methods=["POST"])
def create_cours():
    data = request.get_json()
    errors = CoursInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    cours = Cours(**data)
    db.session.add(cours)
    db.session.commit()
    return CoursOutSchema().jsonify(cours), 201

@cours_bp.route("/", methods=["GET"])
def get_cours():
    cours = Cours.query.all()
    return CoursOutSchema(many=True).jsonify(cours), 200

@cours_bp.route("/<int:id>", methods=["GET"])
def get_cours_by_id(id):
    cours = Cours.query.get_or_404(id)
    return CoursOutSchema().jsonify(cours), 200

@cours_bp.route("/<int:id>", methods=["PUT"])
def update_cours(id):
    cours = Cours.query.get_or_404(id)
    data = request.get_json()
    errors = CoursInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    for key, value in data.items():
        setattr(cours, key, value)
    db.session.commit()
    return CoursOutSchema().jsonify(cours), 200

@cours_bp.route("/<int:id>", methods=["DELETE"])
def delete_cours(id):
    cours = Cours.query.get_or_404(id)
    db.session.delete(cours)
    db.session.commit()
    return jsonify({"message": "Cours supprimé"}), 200
