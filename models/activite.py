from app import db

class Activite(db.Model):
    __tablename__ = "activites"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    prix = db.Column(db.Float, nullable=False)

    destination_id = db.Column(db.Integer, db.ForeignKey("destinations.id"), nullable=False)
