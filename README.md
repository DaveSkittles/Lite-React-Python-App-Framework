# 🚀 Lightweight App Framework

A super lightweight framework that allows people to use Python/SQLite backend + React/HTML frontend to build scalable POC web applications.

## 📁 Project Structure

```
project/
├── .env                  # Environment variables
├── backend/
│   ├── app.py            # Main application entrypoint
│   ├── config.py         # Configuration (loads from .env)
│   ├── models.py         # User model with direct SQLite access
│   ├── auth.py           # Authentication routes & utilities
│   ├── database.py       # SQLite database initialization and helper functions
│   └── requirements.txt  # Python dependencies (Flask, etc.)
└── frontend/
    ├── public/
    │   └── index.html    # HTML entry point
    ├── src/
    │   ├── App.js        # Main React component with routing
    │   ├── index.js      # ReactDOM rendering
    │   └── components/
    │       ├── HomePage.js      # Homepage with login button
    │       ├── LoginPage.js     # Login form component
    │       └── Dashboard.js     # Protected area after login
    ├── package.json      # Dependencies (react, react-router, axios, etc.)
    └── README.md         # This file
```

## 🛠️ Setup Instructions

### 🔐 Environment Setup

1. Create a `.env` file in the root directory with the following variables:
   ```
   # Application secrets
   SECRET_KEY=your-secret-key
   JWT_SECRET_KEY=your-jwt-secret-key
   PASSWORD_SALT=your-custom-password-salt

   # Database configuration
   # This path is relative to the project root directory
   # You can also use an absolute path if needed
   DATABASE_PATH=backend/app.db

   # Server configuration
   FLASK_DEBUG=True
   FLASK_HOST=0.0.0.0
   FLASK_PORT=5000

   # CORS settings
   CORS_ORIGINS=http://localhost:3000
   ```

### 🐍 Backend Setup

1. Navigate to the backend directory:

   ```
   cd backend
   ```
2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```
4. Create a demo user:

   ```
   python create_demo_user.py
   ```
5. Run the Flask application:

   ```
   python app.py
   ```

   The backend will run on http://localhost:5000 ✨

### ⚛️ Frontend Setup

1. Navigate to the frontend directory:

   ```
   cd frontend
   ```
2. Install dependencies using pnpm:

   ```
   # Install pnpm if you don't have it already
   # npm install -g pnpm
   
   # Install dependencies
   pnpm install
   ```
3. Run the React development server:

   ```
   pnpm start
   ```

   The frontend will run on http://localhost:3000 ✨

## 💾 Database Configuration

The SQLite database is created based on the `DATABASE_PATH` specified in your `.env` file. By default, it's set to `backend/app.db`, which creates the database file in the `backend` directory.

You can change this path to any location you prefer:

- **Relative path**: If you specify a relative path (e.g., `data/myapp.db`), it will be resolved relative to the project root directory.
- **Absolute path**: You can also specify an absolute path (e.g., `/var/data/myapp.db` on Linux/Mac or `C:/data/myapp.db` on Windows).

The application will automatically create any necessary directories in the path if they don't exist.

## 🔒 Security Features

### 🔑 Password Hashing

The application uses a double-layered approach to password security:

1. **Custom Application Salt**: A global salt is defined in the `.env` file as `PASSWORD_SALT`. This salt is concatenated with the user's password before hashing.
2. **Werkzeug's Password Hashing**: The salted password is then hashed using Werkzeug's `generate_password_hash` function, which adds its own salt and uses a secure hashing algorithm.

This approach provides additional security even if the database is compromised, as attackers would also need the application's custom salt to attempt cracking the passwords.

### 🔖 JWT Authentication

JSON Web Tokens (JWT) are used for authentication. The tokens are signed with a secret key defined in the `.env` file as `JWT_SECRET_KEY`.

## ✨ Features

- 🔐 User authentication with JWT
- 💾 Direct SQLite database access (no ORM)
- 🔒 Secure password hashing with custom salt
- ⚙️ Environment variables for configuration
- ⚛️ React frontend with routing
- 🌐 Flask RESTful API backend
- 🎨 Bootstrap for responsive design
- 📦 pnpm for fast, disk-space efficient package management

## 🔧 Extending the Framework

This lightweight framework is designed to be easily extended. Here are some ideas:

- 📊 Add more models to `models.py`
- 🔌 Create new API endpoints in `app.py`
- 🧩 Add more React components in the frontend
- 📤 Implement file uploads
- 📈 Add data visualization
- 👥 Implement user management features

## 🚀 Production Deployment

For production deployment, consider:

1. 🗄️ Using a production-ready database like PostgreSQL
2. 🔐 Setting up proper environment variables for secrets
3. 🔒 Configuring HTTPS
4. 📦 Building the React app (`pnpm build`) and serving it via Flask or a dedicated web server
5. 🚀 Using a WSGI server like Gunicorn for the Flask application
