from app import db

class Candidat(db.Model):
    __tablename__ = "candidats"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    prenom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    cv_url = db.Column(db.String(255), nullable=True)
    
    candidatures = db.relationship("Candidature", backref="candidat", lazy=True)
