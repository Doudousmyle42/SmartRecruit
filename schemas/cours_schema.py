from schemas import ma
from marshmallow import fields

class CoursInSchema(ma.Schema):
    titre = fields.Str(required=True)
    description = fields.Str(required=True)

class CoursOutSchema(ma.Schema):
    id = fields.Int()
    titre = fields.Str()
    description = fields.Str()
