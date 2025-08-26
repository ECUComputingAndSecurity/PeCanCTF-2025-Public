import { Link, useNavigate } from "react-router-dom";
export default function NotFound() {
  return (
    <div style={{ padding: "2rem" }}>
      <h1>404 - Page Not Found</h1>
      <p>This route doesn't exist.</p>
      <Link to="/" className="btn btn-success ">
        Home
      </Link>
    </div>
  );
}
