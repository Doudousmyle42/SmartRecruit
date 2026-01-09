from schemas import ma
from marshmallow import fields

class OffreInSchema(ma.Schema):
    titre = fields.Str(required=True)
    description = fields.Str(required=True)
    competences = fields.List(fields.Str(), required=True)

class OffreOutSchema(ma.Schema):
    id = fields.Int()
    titre = fields.Str()
    description = fields.Str()
    competences = fields.List(fields.Str())
    date_publication = fields.DateTime()