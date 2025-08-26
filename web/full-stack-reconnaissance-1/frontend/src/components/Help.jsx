import React, { useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import APIEndpoints from "../apiEndpoints.js";

function Help() {
  document.title = "Help Page";
  const goBack = () => {
    window.history.back();
  };

  return (
    <>
      <div className="card">
        <div className="card-body">
          <div>
            You can create a new account or use one of the below credentials
          </div>
          {/* <table className="table table-hover table-bordered">
            <thead>
              <tr className="table-success">
                <th scope="col">Name</th>
                <th scope="col">Username</th>
                <th scope="col">Password</th>
              </tr>
            </thead>
            <tbody>
              <tr className="table-secondary">
                <td>Eric Williams</td>
                <td>cookpamela</td>
                <td>@8YZv29Rjb</td>
              </tr>
              <tr className="table-secondary">
                <td>Timothy Gonzalez</td>
                <td>diaznicole</td>
                <td>sH6Z&jbh!(</td>
              </tr>
              <tr className="table-secondary">
                <td>Eric Williams</td>
                <td>cookpamela</td>
                <td>@8YZv29Rjb</td>
              </tr>
              <tr className="table-secondary">
                <td>Steven Hunt</td>
                <td>campbellkristen</td>
                <td>*3yTI+Stcg</td>
              </tr>
            </tbody>
          </table> */}
        </div>
        <div className="mb-3">
          <div className="card-header">
            <div className="row">
              <div className="col-md-6">
                <Link
                  onClick={goBack}
                  className="btn btn-success btn-sm float-end"
                >
                  Back
                </Link>
              </div>
              <div className="col-md-2">
                <Link to="/login" className="btn btn-success btn-sm float-end">
                  Login
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Help;
