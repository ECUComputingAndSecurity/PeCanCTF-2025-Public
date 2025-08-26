import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import APIEndpoints from "../apiEndpoints.js";

function Iot() {
  document.title = "IoT (Internet of Things) Penetration Testing";

  const apiUrl = `${APIEndpoints.mainOnly}/iot`;

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
                {/* <Link
                  onClick={goBack}
                  className="btn btn-success btn-sm float-end"
                >
                  Back
                </Link> */}
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

export default Iot;
