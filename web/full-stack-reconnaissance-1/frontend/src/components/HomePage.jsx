import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import APIEndpoints from "../apiEndpoints.js";

function HomePage() {
  document.title = "Home Page";
  const apiUrl = APIEndpoints.testAPI;

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
        <div className="mb-3">
          <div className="card-header">
            <div className="row">
              <h4>The main Cybersecurity penetration testing domains</h4>
              <p>
                Penetration testing, often called pentesting or ethical hacking,
                is like hiring a skilled, ethical "burglar" to try and break
                into your computer systems, networks, or applications. The goal
                isn't to cause harm, but to find weaknesses and vulnerabilities
                before malicious attackers do. Think of it as a controlled,
                simulated cyberattack. Security professionals, known as
                penetration testers (or "pentesters"), use the same tools,
                techniques, and methodologies as real attackers to identify
                exploitable flaws.{" "}
              </p>
              <p>
                Pentesting covers a wide range of systems and environments.
                While the exact categorizations can vary slightly between
                organizations and frameworks, the main penetration testing
                domains typically include:
              </p>
            </div>
          </div>
        </div>
        <div className="card-body">
          <div className="divpadding">
            <Link to="/networking" className="btn btn-success">
              Network Penetration Testing
            </Link>{" "}
          </div>
          <div className="divpadding">
            <Link to="/websites" className="btn btn-success">
              Web Application Penetration Testing
            </Link>{" "}
          </div>
          <div className="divpadding">
            <Link to="/mobilestuff" className="btn btn-success ">
              Mobile Application Penetration Testing
            </Link>{" "}
          </div>
          <div className="divpadding">
            <Link to="/clouding" className="btn btn-success ">
              Cloud Penetration Testing
            </Link>{" "}
          </div>
          <div className="divpadding">
            <Link to="/socialspace" className="btn btn-success ">
              Social Engineering Penetration Testing
            </Link>{" "}
          </div>
          <div className="divpadding">
            <Link to="/physicalenviroments" className="btn btn-success ">
              Physical Security Penetration Testing
            </Link>{" "}
          </div>
          <div className="divpadding">
            <Link to="/clientendpoint" className="btn btn-success ">
              Client-Side Penetration Testing
            </Link>{" "}
          </div>
          <div className="divpadding">
            <Link to="/iotdevices" className="btn btn-success ">
              IoT (Internet of Things) Penetration Testing
            </Link>{" "}
          </div>
        </div>
        {/* <div className="mb-3">
          <div className="card-header">
            <div className="row">
              <div className="col-md-6">
                <Link to="/" className="btn btn-primary">
                  Home
                </Link>
              </div>
            </div>
          </div>
        </div> */}
      </div>
    </>
  );
}

export default HomePage;
