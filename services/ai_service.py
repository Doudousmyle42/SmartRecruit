import os
import requests
from models.user import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from models.candidature import Candidature
from models.offre import OffreEmploi



GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class AIService:
    BASE_URL = "https://api.gemini.com/v1"

    @staticmethod
    def analyze_text(prompt: str):
        """
        Envoie un prompt à l'API Gemini et retourne la réponse.
        """
        headers = {
            "Authorization": f"Bearer {GEMINI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {"prompt": prompt}

        response = requests.post(f"{AIService.BASE_URL}/generate", json=payload, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}



class UserService:
    @staticmethod
    def create_user(nom, prenom, email, password):
        hashed_password = generate_password_hash(password)
        user = User(nom=nom, prenom=prenom, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def authenticate(email, password):
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            return user
        return None




class CandidatureService:
    @staticmethod
    def submit_candidature(candidat_id, offre_id, lettre_motivation):
        candidature = Candidature(
            candidat_id=candidat_id,
            offre_id=offre_id,
            lettre_motivation=lettre_motivation,
            statut="En attente"
        )
        db.session.add(candidature)
        db.session.commit()
        return candidature

    @staticmethod
    def update_status(candidature_id, statut):
        candidature = Candidature.query.get(candidature_id)
        if candidature:
            candidature.statut = statut
            db.session.commit()
        return candidature
    


class OffreService:
    @staticmethod
    def create_offre(titre, description, competences):
        offre = OffreEmploi(titre=titre, description=description, competences=competences)
        db.session.add(offre)
        db.session.commit()
        return offre

    @staticmethod
    def list_offres():
        return OffreEmploi.query.all()

