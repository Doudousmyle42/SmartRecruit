from schemas import ma
from marshmallow import fields

class DestinationInSchema(ma.Schema):
    nom = fields.Str(required=True)
    pays = fields.Str(required=True)
    description = fields.Str(required=True)

class DestinationOutSchema(ma.Schema):
    id = fields.Int()
    nom = fields.Str()
    pays = fields.Str()
    description = fields.Str()
