import SectionTitle from "./SectionTitle.jsx";
import ProjectCard from "./ProjectCard.jsx";
import useGithubProjects from "../hooks/useGithubProjects.js";
import { CATEGORY_STYLES, PROJECT_GROUPS } from "../data/categories.js";

export default function Projects() {
  const { projects, loading } = useGithubProjects();

  const groups = PROJECT_GROUPS.map((g) => ({
    ...g,
    projects: projects.filter((p) => p.category === g.category),
  })).filter((g) => g.projects.length > 0);

  return (
    <section id="projects">
      <SectionTitle emoji="📁">Projects Portfolio</SectionTitle>

      {loading && (
        <div className="glass-card loading-card">
          <i className="fas fa-spinner fa-spin" style={{ marginRight: 10 }} /> Loading projects from GitHub...
        </div>
      )}

      {!loading && groups.length === 0 && (
        <div className="glass-card">
          No public projects fetched from GitHub yet. Check the username in src/data/portfolio.js!
        </div>
      )}

      {groups.map((group) => (
        <div key={group.category}>
          <h3 className="project-group-title" style={{ color: CATEGORY_STYLES[group.category].color }}>
            <i className={`fas ${group.icon}`} /> {group.title}
          </h3>
          <div className="grid-2">
            {group.projects.map((project) => (
              <ProjectCard key={project.repoKey} project={project} />
            ))}
          </div>
        </div>
      ))}
    </section>
  );
}
