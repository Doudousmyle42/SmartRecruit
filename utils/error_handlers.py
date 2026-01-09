from flask import jsonify

def register_error_handlers(app):
    # Erreur 400 : Mauvaise requête
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "error": "Bad Request",
            "message": str(error)
        }), 400

    # Erreur 404 : Ressource non trouvée
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "Not Found",
            "message": "La ressource demandée est introuvable."
        }), 404

    # Erreur 405 : Méthode non autorisée
    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "error": "Method Not Allowed",
            "message": "La méthode HTTP utilisée n'est pas autorisée pour cette ressource."
        }), 405

    # Erreur 500 : Erreur interne du serveur
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "error": "Internal Server Error",
            "message": "Une erreur interne est survenue. Veuillez réessayer plus tard."
        }), 500
