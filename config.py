import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

class Config:
    # Connexion à la base PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Clé secrète Flask (sessions, sécurité)
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")

    # Clé API Gemini
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
