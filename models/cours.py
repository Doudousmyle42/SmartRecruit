from app import db

class Cours(db.Model):
    __tablename__ = "cours"

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)

    modules = db.relationship("Module", backref="cours", lazy=True)
