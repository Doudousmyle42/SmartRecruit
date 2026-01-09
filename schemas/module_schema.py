from schemas import ma
from marshmallow import fields

class ModuleInSchema(ma.Schema):
    titre = fields.Str(required=True)
    contenu = fields.Str(required=True)

class ModuleOutSchema(ma.Schema):
    id = fields.Int()
    titre = fields.Str()
    contenu = fields.Str()
