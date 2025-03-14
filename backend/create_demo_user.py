from models import User
from database import init_db
from config import PASSWORD_SALT

print(f"Using password salt: {PASSWORD_SALT[:3]}{'*' * (len(PASSWORD_SALT) - 3)}")

# Initialize the database
init_db()

# Check if demo user already exists
if not User.get_by_username('demo'):
    # Create demo user
    demo_user = User.create(
        username='demo',
        email='demo@example.com',
        password='password'
    )
    print("Demo user created successfully!")
else:
    print("Demo user already exists.") 