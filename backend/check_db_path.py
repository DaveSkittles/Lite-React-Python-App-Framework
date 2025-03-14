import os
from config import DATABASE_PATH, PROJECT_ROOT

print("Database Configuration Check")
print("--------------------------")
print(f"Project Root: {PROJECT_ROOT}")
print(f"Database Path from config: {DATABASE_PATH}")
print(f"Database Path exists: {os.path.exists(DATABASE_PATH)}")
print(f"Database Directory exists: {os.path.exists(os.path.dirname(DATABASE_PATH))}")

# Check if the path is absolute
if os.path.isabs(DATABASE_PATH):
    print(f"Database Path is absolute: Yes")
else:
    print(f"Database Path is absolute: No")
    
# Print the parent directory of the database file
print(f"Parent directory: {os.path.dirname(DATABASE_PATH)}")

# If the database doesn't exist, try to create an empty file
if not os.path.exists(DATABASE_PATH):
    try:
        os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
        with open(DATABASE_PATH, 'w') as f:
            pass
        print(f"Created empty file at {DATABASE_PATH}")
    except Exception as e:
        print(f"Error creating file: {e}")
        
print("\nTo fix any issues:")
print("1. Check that the DATABASE_PATH in your .env file is correct")
print("2. Make sure the directory exists or the application has permission to create it")
print("3. If using a relative path, it should be relative to the project root directory") 