from schemas import ma
from marshmallow import fields

# Schéma d'entrée : données utilisateur
class UserInSchema(ma.Schema):
    nom = fields.Str(required=True)
    prenom = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)

# Schéma de sortie : représentation utilisateur
class UserOutSchema(ma.Schema):
    id = fields.Int()
    nom = fields.Str()
    prenom = fields.Str()
    email = fields.Email()
