import os
from datetime import timedelta
from dotenv import load_dotenv

# Get the absolute path to the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from .env file
load_dotenv(os.path.join(PROJECT_ROOT, '.env'))

# Base directory of the application
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Database configuration
# If DATABASE_PATH is relative, make it relative to the project root
db_path = os.environ.get('DATABASE_PATH', 'backend/app.db')
if not os.path.isabs(db_path):
    DATABASE_PATH = os.path.join(PROJECT_ROOT, db_path)
else:
    DATABASE_PATH = db_path

# Secret key for session management and JWT
SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Password salt for additional security
PASSWORD_SALT = os.environ.get('PASSWORD_SALT', 'default-salt-change-in-production')

# JWT configuration
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', SECRET_KEY)
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

# CORS settings
CORS_ORIGINS = os.environ.get('CORS_ORIGINS', 'http://localhost:3000').split(',')

# Flask server settings
FLASK_DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() in ('true', '1', 't')
FLASK_HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
FLASK_PORT = int(os.environ.get('FLASK_PORT', 5000))
