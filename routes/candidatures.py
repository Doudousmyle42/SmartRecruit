from flask import Blueprint, request, jsonify
from app import db
from models.candidature import Candidature
from schemas.candidature_schema import CandidatureInSchema, CandidatureOutSchema

applications_bp = Blueprint("applications", __name__)

@applications_bp.route("/", methods=["POST"])
def create_candidature():
    data = request.get_json()
    errors = CandidatureInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    candidature = Candidature(**data)
    db.session.add(candidature)
    db.session.commit()
    return CandidatureOutSchema().jsonify(candidature), 201

@applications_bp.route("/", methods=["GET"])
def get_candidatures():
    candidatures = Candidature.query.all()
    return CandidatureOutSchema(many=True).jsonify(candidatures), 200

@applications_bp.route("/<int:id>", methods=["GET"])
def get_candidature(id):
    candidature = Candidature.query.get_or_404(id)
    return CandidatureOutSchema().jsonify(candidature), 200

@applications_bp.route("/<int:id>", methods=["PUT"])
def update_candidature(id):
    candidature = Candidature.query.get_or_404(id)
    data = request.get_json()
    errors = CandidatureInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    for key, value in data.items():
        setattr(candidature, key, value)
    db.session.commit()
    return CandidatureOutSchema().jsonify(candidature), 200

@applications_bp.route("/<int:id>", methods=["DELETE"])
def delete_candidature(id):
    candidature = Candidature.query.get_or_404(id)
    db.session.delete(candidature)
    db.session.commit()
    return jsonify({"message": "Candidature supprimée"}), 200
