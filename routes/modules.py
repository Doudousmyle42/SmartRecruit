from flask import Blueprint, request, jsonify
from app import db
from models.module import Module
from schemas.module_schema import ModuleInSchema, ModuleOutSchema

modules_bp = Blueprint("modules", __name__)

@modules_bp.route("/", methods=["POST"])
def create_module():
    data = request.get_json()
    errors = ModuleInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    module = Module(**data)
    db.session.add(module)
    db.session.commit()
    return ModuleOutSchema().jsonify(module), 201

@modules_bp.route("/", methods=["GET"])
def get_modules():
    modules = Module.query.all()
    return ModuleOutSchema(many=True).jsonify(modules), 200

@modules_bp.route("/<int:id>", methods=["GET"])
def get_module(id):
    module = Module.query.get_or_404(id)
    return ModuleOutSchema().jsonify(module), 200

@modules_bp.route("/<int:id>", methods=["PUT"])
def update_module(id):
    module = Module.query.get_or_404(id)
    data = request.get_json()
    errors = ModuleInSchema().validate(data)
    if errors:
        return jsonify(errors), 400

    for key, value in data.items():
        setattr(module, key, value)
    db.session.commit()
    return ModuleOutSchema().jsonify(module), 200

@modules_bp.route("/<int:id>", methods=["DELETE"])
def delete_module(id):
    module = Module.query.get_or_404(id)
    db.session.delete(module)
    db.session.commit()
    return jsonify({"message": "Module supprimé"}), 200
