import SectionTitle from "./SectionTitle.jsx";
import portfolio from "../data/portfolio.js";

export default function Skills() {
  return (
    <section id="skills">
      <SectionTitle emoji="🛠️">Skills &amp; Expertise</SectionTitle>
      <div className="grid-3">
        {portfolio.skills.map((group) => (
          <div className="glass-card" key={group.title}>
            <h3 className="skill-heading" style={{ color: group.color }}>
              <i className={`fas ${group.icon}`} style={{ marginRight: 10 }} /> {group.title}
            </h3>
            {group.items.map((skill) => (
              <span className="skill-tag" key={skill}>{skill}</span>
            ))}
          </div>
        ))}
      </div>
    </section>
  );
}
