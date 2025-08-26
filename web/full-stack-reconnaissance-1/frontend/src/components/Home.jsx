import React, { useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import APIEndpoints from "../apiEndpoints.js";

function Home() {
  document.title = "Home Page";
  return (
    <div className="card">
      <div className="card-header">
        <div className="row">
          <div className="col-md-6">Create account</div>
          <div className="col-md-6">
            <Link to="/register" className="btn btn-success btn-sm float-end">
              Register
            </Link>
          </div>
        </div>
      </div>
      <div className="card-header">
        <div className="row">
          <div className="col-md-6">Login to your account</div>
          <div className="col-md-6">
            <Link to="/login" className="btn btn-success btn-sm float-end">
              Login
            </Link>
          </div>
        </div>
      </div>
      <div className="card-header">
        <div className="row">
          <div className="col-md-6">Help</div>
          <div className="col-md-6">
            <Link to="/help" className="btn btn-success btn-sm float-end">
              Help
            </Link>
          </div>
        </div>
      </div>
      <div className="card-body">
        <div className="row">
          <div className="col-md-4">&nbsp;</div>
          <div className="col-md-4">
            <div className="mb-3"> </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
