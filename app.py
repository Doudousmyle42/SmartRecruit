from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

# Initialisation des extensions
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "dev_secret")

    # Initialiser les extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Importer et enregistrer les Blueprints
    from routes.offers import offers_bp
    from routes.candidats import candidates_bp
    from routes.applications import applications_bp
    from routes.cours import courses_bp
    from routes.users import users_bp
    from routes.destinations import destinations_bp

    app.register_blueprint(offers_bp, url_prefix="/api/offers")
    app.register_blueprint(candidates_bp, url_prefix="/api/candidates")
    app.register_blueprint(applications_bp, url_prefix="/api/applications")
    app.register_blueprint(courses_bp, url_prefix="/api/courses")
    app.register_blueprint(users_bp, url_prefix="/api/users")
    app.register_blueprint(destinations_bp, url_prefix="/api/destinations")

    # Création des tables directement 
    with app.app_context():
        db.create_all()

    # Gestion des erreurs personnalisées
    from utils.error_handlers import register_error_handlers
    register_error_handlers(app)

    return app

# Point d'entrée
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
