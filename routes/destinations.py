from flask import Blueprint, request, jsonify
from app import db
from models.destination import Destination
from schemas.destination_schema import DestinationInSchema, DestinationOutSchema

destinations_bp = Blueprint("destinations", __name__)

@destinations_bp.route("/", methods=["POST"])
def create_destination():
    data = request.get_json()
    errors = DestinationInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    destination = Destination(**data)
    db.session.add(destination)
    db.session.commit()
    return DestinationOutSchema().jsonify(destination), 201

@destinations_bp.route("/", methods=["GET"])
def get_destinations():
    destinations = Destination.query.all()
    return DestinationOutSchema(many=True).jsonify(destinations), 200

@destinations_bp.route("/<int:id>", methods=["GET"])
def get_destination(id):
    destination = Destination.query.get_or_404(id)
    return DestinationOutSchema().jsonify(destination), 200

@destinations_bp.route("/<int:id>", methods=["PUT"])
def update_destination(id):
    destination = Destination.query.get_or_404(id)
    data = request.get_json()
    errors = DestinationInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    for key, value in data.items():
        setattr(destination, key, value)
    db.session.commit()
    return DestinationOutSchema().jsonify(destination), 200

@destinations_bp.route("/<int:id>", methods=["DELETE"])
def delete_destination(id):
    destination = Destination.query.get_or_404(id)
    db.session.delete(destination)
    db.session.commit()
    return jsonify({"message": "Destination supprimée"}), 200
