import { useEffect, useState } from "react";
import portfolio from "../data/portfolio.js";

function RoleCycle({ roles }) {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    if (roles.length < 2) return;
    const id = setInterval(() => setIndex((i) => (i + 1) % roles.length), 3000);
    return () => clearInterval(id);
  }, [roles.length]);

  return (
    <div className="role-window">
      <div className="role-cycle">
        {/* key forces remount so the CSS animation restarts */}
        <span key={index} className="role-label">{roles[index]}</span>
      </div>
    </div>
  );
}

export default function Hero() {
  const { name, initials, roles, githubUrl, linkedinUrl, email } = portfolio;

  return (
    <section id="home" className="hero">
      <div className="hero__text">
        <h1 className="hero-title">{name}</h1>
        <div className="hero-subtitle">Data Analyst &amp; Power BI Dashboard Expert</div>
        <p className="hero__intro">
          I transform complex datasets into high-impact visual stories. Specializing in{" "}
          <strong style={{ color: "#d4af37" }}>Power BI interactive dashboards</strong>, database analysis, and{" "}
          <strong style={{ color: "#f5e27a" }}>machine learning predictive models</strong>, I help businesses and
          clients make data-driven decisions that increase profitability and optimize operations.
        </p>

        <div className="hero__actions">
          <a href="#contact" className="btn-glow">Get In Touch</a>
          <a href={githubUrl} target="_blank" rel="noopener noreferrer" className="btn-outline">
            <i className="fab fa-github" style={{ marginRight: 8 }} /> GitHub Profile
          </a>
        </div>

        <div className="social-links">
          <a href={githubUrl} target="_blank" rel="noopener noreferrer" className="social-icon" aria-label="GitHub">
            <i className="fab fa-github" />
          </a>
          <a href={linkedinUrl} target="_blank" rel="noopener noreferrer" className="social-icon" aria-label="LinkedIn">
            <i className="fab fa-linkedin" />
          </a>
          <a href={`mailto:${email}`} className="social-icon" aria-label="Email">
            <i className="fas fa-envelope" />
          </a>
        </div>
      </div>

      <div className="hero__visual">
        <div className="hero-orb">
          <div>
            <div className="hero-orb__initials">{initials}</div>
            <RoleCycle roles={roles} />
          </div>
        </div>
      </div>
    </section>
  );
}
