import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import APIEndpoints from "../apiEndpoints.js";

function Network() {
  document.title = "Network Penetration Testing";
  const apiUrl = `${APIEndpoints.mainOnly}/network?filtered=true`;

  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch(apiUrl);
        if (!res.ok) throw new Error("Network response not ok");
        const json = await res.json();
        setData(json);
      } catch (e) {
        setError(e.message);
      }
    }
    fetchData();
  }, []);

  if (error) return <div>Error: {error}</div>;
  if (!data) return <div>Loading...</div>;

  return (
    <>
      <div className="card">
        <div className="card-body">
          <div>{data.message}</div>
        </div>
        <div className="mb-3">
          <div className="card-header">
            <div className="row">
              <div className="col-md-6">
                <Link to="/" className="btn btn-success ">
                  Home
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Network;
