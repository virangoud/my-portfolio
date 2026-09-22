import Navbar from "./components/Navbar.jsx";
import Hero from "./components/Hero.jsx";
import About from "./components/About.jsx";
import Skills from "./components/Skills.jsx";
import Projects from "./components/Projects.jsx";
import Experience from "./components/Experience.jsx";
import Contact from "./components/Contact.jsx";
import portfolio from "./data/portfolio.js";

export default function App() {
  return (
    <div className="container">
      <Navbar />
      <Hero />
      <About />
      <Skills />
      <Projects />
      <Experience />
      <Contact />
      <footer className="site-footer">
        © {new Date().getFullYear()} {portfolio.name}
      </footer>
    </div>
  );
}
