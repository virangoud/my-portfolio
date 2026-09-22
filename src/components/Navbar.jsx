import portfolio from "../data/portfolio.js";

const LINKS = ["home", "about", "skills", "projects", "experience", "contact"];

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar__logo">{portfolio.initials}</div>
      <div className="navbar__links">
        {LINKS.map((id) => (
          <a key={id} href={`#${id}`}>
            {id.charAt(0).toUpperCase() + id.slice(1)}
          </a>
        ))}
      </div>
    </nav>
  );
}
