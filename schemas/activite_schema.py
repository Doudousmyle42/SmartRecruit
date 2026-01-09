from schemas import ma
from marshmallow import fields

class ActiviteInSchema(ma.Schema):
    nom = fields.Str(required=True)
    description = fields.Str(required=True)
    prix = fields.Float(required=True)

class ActiviteOutSchema(ma.Schema):
    id = fields.Int()
    nom = fields.Str()
    description = fields.Str()
    prix = fields.Float()
