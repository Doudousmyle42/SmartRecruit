from flask import Blueprint, request, jsonify
from app import db
from models.cours import Cours
from schemas.cours_schema import CoursInSchema, CoursOutSchema

courses_bp = Blueprint("courses", __name__)

@courses_bp.route("/", methods=["POST"])
def create_cours():
    data = request.get_json()
    errors = CoursInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    cours = Cours(**data)
    db.session.add(cours)
    db.session.commit()
    return CoursOutSchema().jsonify(cours), 201

@courses_bp.route("/", methods=["GET"])
def get_courses():
    courses = Cours.query.all()
    return CoursOutSchema(many=True).jsonify(courses), 200

@courses_bp.route("/<int:id>", methods=["GET"])
def get_courses_by_id(id):
    course = Cours.query.get_or_404(id)
    return CoursOutSchema().jsonify(course), 200

@courses_bp.route("/<int:id>", methods=["PUT"])
def update_courses(id):
    cours = Cours.query.get_or_404(id)
    data = request.get_json()
    errors = CoursInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    for key, value in data.items():
        setattr(cours, key, value)
    db.session.commit()
    return CoursOutSchema().jsonify(cours), 200

@courses_bp.route("/<int:id>", methods=["DELETE"])
def delete_courses(id):
    cours = Cours.query.get_or_404(id)
    db.session.delete(cours)
    db.session.commit()
    return jsonify({"message": "Cours supprimé"}), 200
