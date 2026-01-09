from app import db

class Module(db.Model):
    __tablename__ = "modules"

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(150), nullable=False)
    contenu = db.Column(db.Text, nullable=False)

    cours_id = db.Column(db.Integer, db.ForeignKey("cours.id"), nullable=False)
