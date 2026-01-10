from flask import Blueprint, request, jsonify
from app import db
from models.candidat import Candidat
from schemas.candidat_schema import CandidatInSchema, CandidatOutSchema

candidates_bp = Blueprint("candidates", __name__)

# Créer un candidat
@candidates_bp.route("/", methods=["POST"])
def create_candidate():
    data = request.get_json()
    schema = CandidatInSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    candidat = Candidat(**data)
    db.session.add(candidat)
    db.session.commit()

    return CandidatOutSchema().jsonify(candidat), 201

# Récupérer tous les candidats
@candidates_bp.route("/", methods=["GET"])
def get_candidates():
    candidates = Candidat.query.all()
    return CandidatOutSchema(many=True).jsonify(candidates), 200

# Récupérer un candidat par ID
@candidates_bp.route("/<int:id>", methods=["GET"])
def get_candidate(id):
    candidat = Candidat.query.get_or_404(id)
    return CandidatOutSchema().jsonify(candidat), 200

# Mettre à jour un candidat
@candidates_bp.route("/<int:id>", methods=["PUT"])
def update_candidate(id):
    candidat = Candidat.query.get_or_404(id)
    data = request.get_json()
    schema = CandidatInSchema()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400

    for key, value in data.items():
        setattr(candidat, key, value)

    db.session.commit()
    return CandidatOutSchema().jsonify(candidat), 200

# Supprimer un candidat
@candidates_bp.route("/<int:id>", methods=["DELETE"])
def delete_candidate(id):
    candidat = Candidat.query.get_or_404(id)
    db.session.delete(candidat)
    db.session.commit()
    return jsonify({"message": "Candidat supprimé"}), 200
