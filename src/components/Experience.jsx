import SectionTitle from "./SectionTitle.jsx";
import portfolio from "../data/portfolio.js";

export default function Experience() {
  return (
    <section id="experience">
      <SectionTitle emoji="📈">Experience &amp; Freelance Services</SectionTitle>

      <div className="glass-card" style={{ borderLeft: "5px solid #d4af37" }}>
        <h3 style={{ color: "#d4af37", marginTop: 0 }}>
          <i className="fas fa-handshake" style={{ marginRight: 10 }} /> Available for Freelance &amp; Contract Work
        </h3>
        <p className="body-text">
          I provide custom dashboard building and data services for startups and small-to-medium businesses. If you
          have messy Excel files or SQL tables, I can transform them into a clean, auto-updating dashboard. I also
          develop custom predictive models to help forecast sales, stock requirements, or client retention.
        </p>
      </div>

      <div className="timeline">
        {portfolio.experience.map((item) => (
          <div className="timeline-item" key={item.title}>
            <div className="timeline-date">{item.date}</div>
            <div className="timeline-title">{item.title}</div>
            <div className="timeline-company">{item.company}</div>
            <p style={{ color: "#c9b78a", fontSize: "0.95rem" }}>{item.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
