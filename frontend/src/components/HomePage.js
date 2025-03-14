import React, { useContext } from 'react';
import { Link, Navigate } from 'react-router-dom';
import { AuthContext } from '../App';

function HomePage() {
  const { isAuthenticated } = useContext(AuthContext);
  
  // If user is already authenticated, redirect to dashboard
  if (isAuthenticated) {
    return <Navigate to="/dashboard" />;
  }
  
  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-md-8 text-center">
          <div className="card shadow-lg border-0 rounded-lg">
            <div className="card-body p-5">
              <h1 className="display-4 mb-4">Welcome to Lightweight App Framework</h1>
              <p className="lead mb-4">
                A simple, scalable framework for building proof-of-concept web applications
                with Python/SQLite backend and React frontend.
              </p>
              <div className="d-grid gap-2 d-md-flex justify-content-md-center">
                <Link to="/login" className="btn btn-primary btn-lg px-4 me-md-2">
                  Login
                </Link>
              </div>
            </div>
          </div>
          
          <div className="mt-5">
            <h2>Features</h2>
            <ul className="list-group list-group-flush mt-3">
              <li className="list-group-item">User authentication with JWT</li>
              <li className="list-group-item">SQLite database for easy setup</li>
              <li className="list-group-item">React frontend with routing</li>
              <li className="list-group-item">Flask RESTful API backend</li>
              <li className="list-group-item">Bootstrap for responsive design</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HomePage;
