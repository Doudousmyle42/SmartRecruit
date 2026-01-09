from flask import Blueprint, request, jsonify
from app import db
from models.activite import Activite
from schemas.activite_schema import ActiviteInSchema, ActiviteOutSchema

activites_bp = Blueprint("activites", __name__)

@activites_bp.route("/", methods=["POST"])
def create_activite():
    data = request.get_json()
    errors = ActiviteInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    activite = Activite(**data)
    db.session.add(activite)
    db.session.commit()
    return ActiviteOutSchema().jsonify(activite), 201

@activites_bp.route("/", methods=["GET"])
def get_activites():
    activites = Activite.query.all()
    return ActiviteOutSchema(many=True).jsonify(activites), 200

@activites_bp.route("/<int:id>", methods=["GET"])
def get_activite(id):
    activite = Activite.query.get_or_404(id)
    return ActiviteOutSchema().jsonify(activite), 200

@activites_bp.route("/<int:id>", methods=["PUT"])
def update_activite(id):
    activite = Activite.query.get_or_404(id)
    data = request.get_json()
    errors = ActiviteInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    for key, value in data.items():
        setattr(activite, key, value)
    db.session.commit()
    return ActiviteOutSchema().jsonify(activite), 200

@activites_bp.route("/<int:id>", methods=["DELETE"])
def delete_activite(id):
    activite = Activite.query.get_or_404(id)
    db.session.delete(activite)
    db.session.commit()
    return jsonify({"message": "Activité supprimée"}), 200
