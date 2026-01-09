from flask import Blueprint, request, jsonify
from app import db
from models.offre import OffreEmploi
from schemas.offre_schema import OffreInSchema, OffreOutSchema

offres_bp = Blueprint("offres", __name__)

@offres_bp.route("/", methods=["POST"])
def create_offre():
    data = request.get_json()
    errors = OffreInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    offre = OffreEmploi(**data)
    db.session.add(offre)
    db.session.commit()
    return OffreOutSchema().jsonify(offre), 201

@offres_bp.route("/", methods=["GET"])
def get_offres():
    offres = OffreEmploi.query.all()
    return OffreOutSchema(many=True).jsonify(offres), 200

@offres_bp.route("/<int:id>", methods=["GET"])
def get_offre(id):
    offre = OffreEmploi.query.get_or_404(id)
    return OffreOutSchema().jsonify(offre), 200

@offres_bp.route("/<int:id>", methods=["PUT"])
def update_offre(id):
    offre = OffreEmploi.query.get_or_404(id)
    data = request.get_json()
    errors = OffreInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    for key, value in data.items():
        setattr(offre, key, value)
    db.session.commit()
    return OffreOutSchema().jsonify(offre), 200

@offres_bp.route("/<int:id>", methods=["DELETE"])
def delete_offre(id):
    offre = OffreEmploi.query.get_or_404(id)
    db.session.delete(offre)
    db.session.commit()
    return jsonify({"message": "Offre supprimée"}), 200
