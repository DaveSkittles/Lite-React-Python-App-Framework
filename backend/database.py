import sqlite3
import os
from config import DATABASE_PATH

def get_db_connection():
    """Get a connection to the SQLite database"""
    # Get the absolute path to the database
    db_path = os.path.abspath(DATABASE_PATH)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Return rows as dictionaries
    return conn

def init_db():
    """Initialize the database with required tables"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()
    
def reset_db():
    """Reset the database (for development purposes)"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Drop tables
    cursor.execute('DROP TABLE IF EXISTS user')
    
    conn.commit()
    conn.close()
    
    # Recreate tables
    init_db()
