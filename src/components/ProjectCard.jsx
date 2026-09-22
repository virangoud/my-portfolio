import { CATEGORY_STYLES } from "../data/categories.js";

export default function ProjectCard({ project }) {
  const s = CATEGORY_STYLES[project.category] || CATEGORY_STYLES["Python & ML"];

  return (
    <div className="glass-card project-card">
      <div className="project-card__header">
        <h3 style={{ color: s.color }}>{project.name}</h3>
        <span className="category-badge" style={{ background: s.bg, color: s.color, borderColor: s.border }}>
          {project.category}
          {project.stars > 0 && ` | ★ ${project.stars}`}
        </span>
      </div>

      {project.client && (
        <div style={{ marginBottom: 12 }}>
          <div className="client-badge">
            <i className="fas fa-building" style={{ color: s.color, fontSize: "0.8rem" }} />
            <span className="client-name">{project.client}</span>
            {project.profession && (
              <div className="client-tooltip" style={{ borderColor: s.color, color: s.color }}>
                <i className="fas fa-user-tie" style={{ marginRight: 6 }} />
                {project.profession}
              </div>
            )}
          </div>
        </div>
      )}

      <p className="project-card__desc">{project.description}</p>

      <div style={{ marginBottom: 20 }}>
        {project.techStack.map((tech) => (
          <span className="tech-tag" key={tech}>{tech}</span>
        ))}
      </div>

      <a
        href={project.githubUrl}
        target="_blank"
        rel="noopener noreferrer"
        className="btn-glow btn-sm"
        style={{ background: s.color, boxShadow: `0 0 15px ${s.bg}`, color: s.btnText }}
      >
        <i className="fab fa-github" style={{ marginRight: 5 }} /> View Repository
      </a>
    </div>
  );
}
