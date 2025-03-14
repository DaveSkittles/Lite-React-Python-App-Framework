import React, { useContext } from 'react';
import { AuthContext } from '../App';

function Dashboard() {
  const { user, logout } = useContext(AuthContext);
  
  return (
    <div className="container py-5">
      <div className="row justify-content-center">
        <div className="col-md-8">
          <div className="card shadow-lg border-0 rounded-lg">
            <div className="card-header bg-primary text-white d-flex justify-content-between align-items-center">
              <h3 className="font-weight-light my-2">Dashboard</h3>
              <button 
                onClick={logout} 
                className="btn btn-light btn-sm"
              >
                Logout
              </button>
            </div>
            <div className="card-body p-4">
              <div className="alert alert-success" role="alert">
                <h4 className="alert-heading">Welcome, {user?.username}!</h4>
                <p>You have successfully logged in to the Lightweight App Framework.</p>
                <hr />
                <p className="mb-0">This is a protected area that only authenticated users can access.</p>
              </div>
              
              <div className="mt-4">
                <h4>User Information</h4>
                <table className="table table-bordered">
                  <tbody>
                    <tr>
                      <th scope="row">Username</th>
                      <td>{user?.username}</td>
                    </tr>
                    <tr>
                      <th scope="row">Email</th>
                      <td>{user?.email}</td>
                    </tr>
                    <tr>
                      <th scope="row">User ID</th>
                      <td>{user?.id}</td>
                    </tr>
                    <tr>
                      <th scope="row">Account Created</th>
                      <td>{new Date(user?.created_at).toLocaleString()}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
              
              <div className="mt-4">
                <h4>What's Next?</h4>
                <p>
                  This is where you would build your application's main functionality.
                  Some ideas for what you could add:
                </p>
                <ul>
                  <li>Data entry forms</li>
                  <li>Data visualization</li>
                  <li>File uploads</li>
                  <li>User management</li>
                  <li>Settings and preferences</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
