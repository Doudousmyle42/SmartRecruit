from app import db

class Destination(db.Model):
    __tablename__ = "destinations"

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(150), nullable=False)
    pays = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    activites = db.relationship("Activite", backref="destination", lazy=True)
