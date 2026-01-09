from schemas import ma
from marshmallow import fields

class CandidatureInSchema(ma.Schema):
    candidat_id = fields.Int(required=True)
    offre_id = fields.Int(required=True)
    lettre_motivation = fields.Str(required=True)

class CandidatureOutSchema(ma.Schema):
    id = fields.Int()
    candidat_id = fields.Int()
    offre_id = fields.Int()
    lettre_motivation = fields.Str()
    statut = fields.Str()
    date_candidature = fields.DateTime()