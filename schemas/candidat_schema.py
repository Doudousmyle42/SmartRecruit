from schemas import ma
from marshmallow import fields

# Schéma d'entrée : données candidat
class CandidatInSchema(ma.Schema):
    nom = fields.Str(required=True)
    prenom = fields.Str(required=True)
    email = fields.Email(required=True)
    telephone = fields.Str(required=True)

# Schéma de sortie : représentation candidat
class CandidatOutSchema(ma.Schema):
    id = fields.Int()
    nom = fields.Str()
    prenom = fields.Str()
    email = fields.Email()
    telephone = fields.Str()
    cv_url = fields.Str()