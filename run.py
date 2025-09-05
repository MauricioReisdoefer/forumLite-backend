from flask import Flask
from flask_cors import CORS
from routes.post_routes import post_bp
from routes.topic_routes import topic_bp
from routes.user_routes import user_bp
from models.table_registry import certifyTableRegistry
from flask_jwt_extended import JWTManager

from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "shit")
    
    JWTManager(app=app)
    CORS(app)  
    
    app.register_blueprint(post_bp)
    app.register_blueprint(topic_bp)
    app.register_blueprint(user_bp)

    certifyTableRegistry()

    @app.route("/")
    def home():
        return {"message": "API Flask rodando"}

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
