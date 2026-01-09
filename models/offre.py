from app import db

class OffreEmploi(db.Model):
    __tablename__ = "offres"

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    competences = db.Column(db.ARRAY(db.String), nullable=False)
    date_publication = db.Column(db.DateTime, nullable=False, server_default=db.func.now())

    candidatures = db.relationship("Candidature", backref="offre", lazy=True)
