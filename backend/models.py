from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from database import get_db_connection
from config import PASSWORD_SALT

class User:
    """User model for authentication"""
    
    @staticmethod
    def create(username, email, password):
        """Create a new user"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Hash the password with custom salt
        salted_password = password + PASSWORD_SALT
        password_hash = generate_password_hash(salted_password)
        
        # Insert the user
        cursor.execute(
            'INSERT INTO user (username, email, password_hash) VALUES (?, ?, ?)',
            (username, email, password_hash)
        )
        
        # Get the user ID
        user_id = cursor.lastrowid
        
        conn.commit()
        conn.close()
        
        return User.get_by_id(user_id)
    
    @staticmethod
    def get_by_id(user_id):
        """Get user by ID"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM user WHERE id = ?', (user_id,))
        user_data = cursor.fetchone()
        
        conn.close()
        
        if user_data:
            return User(user_data)
        return None
    
    @staticmethod
    def get_by_username(username):
        """Get user by username"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
        user_data = cursor.fetchone()
        
        conn.close()
        
        if user_data:
            return User(user_data)
        return None
    
    @staticmethod
    def get_by_email(email):
        """Get user by email"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM user WHERE email = ?', (email,))
        user_data = cursor.fetchone()
        
        conn.close()
        
        if user_data:
            return User(user_data)
        return None
    
    def __init__(self, user_data):
        """Initialize user from database row"""
        self.id = user_data['id']
        self.username = user_data['username']
        self.email = user_data['email']
        self.password_hash = user_data['password_hash']
        self.created_at = user_data['created_at']
    
    def check_password(self, password):
        """Check if provided password matches stored hash"""
        # Add the salt to the password before checking
        salted_password = password + PASSWORD_SALT
        return check_password_hash(self.password_hash, salted_password)
    
    def to_dict(self):
        """Convert user object to dictionary (for API responses)"""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at
        }
