from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

# Import configuration and modules
from config import *
from database import init_db
from auth import auth_bp

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    
    # Load configuration
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = JWT_ACCESS_TOKEN_EXPIRES
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = JWT_REFRESH_TOKEN_EXPIRES
    
    # Initialize extensions
    CORS(app, resources={r"/api/*": {"origins": CORS_ORIGINS}})
    jwt = JWTManager(app)
    
    # Initialize database
    init_db()
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    
    # Basic route for API status
    @app.route('/api/status')
    def status():
        return jsonify({'status': 'API is running'})
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=FLASK_DEBUG, host=FLASK_HOST, port=FLASK_PORT)
