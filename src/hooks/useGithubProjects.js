import { useEffect, useState } from "react";
import portfolio from "../data/portfolio.js";

const CACHE_KEY = "gh-projects";
const CACHE_TTL_MS = 10 * 60 * 1000; // 10 minutes, avoids GitHub API rate limits

function titleCase(str) {
  return str.toLowerCase().replace(/\b\w/g, (c) => c.toUpperCase());
}

function categorize(repoName) {
  const n = repoName.toLowerCase();
  const has = (...words) => words.some((w) => n.includes(w));
  if (has("bi", "dashboard", "powerbi", "insights", "wear", "paint")) return "Power BI";
  if (has("sql", "database", "db", "query", "ward")) return "SQL & Database";
  return "Python & ML";
}

function fromMetadata(repoName, meta, base = {}) {
  return {
    githubUrl: `https://github.com/${portfolio.githubUsername}/${repoName}`,
    stars: 0,
    ...base,
    repoKey: repoName,
    name: meta.customName,
    category: meta.category,
    description: meta.description,
    techStack: meta.techStack,
    client: meta.client || null,
    profession: meta.profession || null,
  };
}

export function getFallbackProjects() {
  return Object.entries(portfolio.localProjectsMetadata).map(([repo, meta]) => fromMetadata(repo, meta));
}

function readCache() {
  try {
    const raw = sessionStorage.getItem(CACHE_KEY);
    if (!raw) return null;
    const { data, expires } = JSON.parse(raw);
    return Date.now() < expires ? data : null;
  } catch {
    return null;
  }
}

function writeCache(data) {
  try {
    sessionStorage.setItem(CACHE_KEY, JSON.stringify({ data, expires: Date.now() + CACHE_TTL_MS }));
  } catch {
    /* storage unavailable — ignore */
  }
}

async function fetchGithubProjects(signal) {
  const url = `https://api.github.com/users/${portfolio.githubUsername}/repos?sort=updated&per_page=100`;
  const res = await fetch(url, { headers: { Accept: "application/vnd.github.v3+json" }, signal });
  if (!res.ok) throw new Error(`GitHub API responded ${res.status}`);
  const repos = await res.json();

  return repos
    .filter((repo) => !repo.fork)
    .map((repo) => {
      const base = {
        name: titleCase(repo.name.replace(/[-_]/g, " ")),
        category: categorize(repo.name),
        description: repo.description || "No description provided on GitHub yet.",
        techStack: repo.language ? [repo.language] : ["Data Analysis"],
        githubUrl: repo.html_url,
        stars: repo.stargazers_count || 0,
        repoKey: repo.name,
        client: null,
        profession: null,
      };
      const meta = portfolio.localProjectsMetadata[repo.name];
      return meta ? fromMetadata(repo.name, meta, base) : base;
    });
}

export default function useGithubProjects() {
  const [projects, setProjects] = useState(() => readCache());
  const [loading, setLoading] = useState(projects === null);

  useEffect(() => {
    if (projects !== null) return;
    let cancelled = false;
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 5000);

    fetchGithubProjects(controller.signal)
      .then((data) => {
        if (cancelled) return;
        writeCache(data);
        setProjects(data);
      })
      .catch((err) => {
        if (cancelled) return;
        console.warn("[github] using fallback projects:", err.message);
        setProjects(getFallbackProjects());
      })
      .finally(() => {
        clearTimeout(timeout);
        if (!cancelled) setLoading(false);
      });

    return () => {
      cancelled = true;
      clearTimeout(timeout);
      controller.abort();
    };
  }, []); // eslint-disable-line react-hooks/exhaustive-deps

  return { projects: projects || [], loading };
}
