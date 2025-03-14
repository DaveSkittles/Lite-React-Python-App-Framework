from models import User
from database import reset_db
from config import PASSWORD_SALT

print("Resetting database and creating demo user...")
print(f"Using password salt: {PASSWORD_SALT[:3]}{'*' * (len(PASSWORD_SALT) - 3)}")

# Reset the database (drop and recreate tables)
reset_db()

# Create demo user
demo_user = User.create(
    username='demo',
    email='demo@example.com',
    password='password'
)

print("Database reset and demo user created successfully!")
print("You can now log in with:")
print("Username: demo")
print("Password: password") 