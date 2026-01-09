from app import db

class Candidature(db.Model):
    __tablename__ = "candidatures"

    id = db.Column(db.Integer, primary_key=True)
    candidat_id = db.Column(db.Integer, db.ForeignKey("candidats.id"), nullable=False)
    offre_id = db.Column(db.Integer, db.ForeignKey("offres.id"), nullable=False)
    lettre_motivation = db.Column(db.Text, nullable=False)
    statut = db.Column(db.String(50), default="En attente")
    date_candidature = db.Column(db.DateTime, nullable=False, server_default=db.func.now())