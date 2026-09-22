# my-portfolio

Personal portfolio for **Viranagouda Patil** — Data Analyst & Power BI Developer.
Built with **React + Vite** (converted from the original Streamlit app).

## Getting started

Requires Node.js 18+.

```bash
npm install
npm run dev       # start dev server at http://localhost:5173
npm run build     # production build into dist/
npm run preview   # preview the production build
```

## Project structure

```
index.html                  # HTML shell (fonts, Font Awesome)
src/
  main.jsx                  # React entry point
  App.jsx                   # Page layout (all sections)
  data/portfolio.js         # ⚙️ Edit your name, links, skills, projects, experience here
  data/categories.js        # Project category colours & groups
  hooks/useGithubProjects.js# Fetches public repos from GitHub (10-min cache, offline fallback)
  components/               # Navbar, Hero, About, Skills, Projects, ProjectCard, Experience, Contact
  styles/style.css          # Gold & black theme
```

## Notes

- Projects are fetched live from `https://api.github.com/users/<username>/repos`. Forks are skipped, and
  entries in `localProjectsMetadata` override the name/description/tech stack of matching repos.
  If GitHub is unreachable, the local metadata is shown instead.
- The contact form posts to [FormSubmit](https://formsubmit.co). The first submission sends a confirmation
  email to the configured address that must be approved once.
- `dist/` is a static site — deploy it to Vercel, Netlify, GitHub Pages, etc.
