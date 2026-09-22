import SectionTitle from "./SectionTitle.jsx";

const REASONS = [
  ["Business-Centric Dashboards:", "I don't just make charts; I design reports around core business objectives (Sales growth, profit margins, cost reductions)."],
  ["Clean Data Prep:", "Experienced in writing DAX queries, Power Query transformations, and Python pipelines to handle missing data and outliers."],
  ["Version Control & Git:", "All my work is structured, documented, and version-controlled via GitHub, ensuring high reliability."],
  ["Fast Delivery & Collaboration:", "Transparent communication, milestone updates, and prompt responses."],
];

export default function About() {
  return (
    <section id="about">
      <SectionTitle emoji="👤">About Me</SectionTitle>

      <div className="glass-card">
        <h3 style={{ color: "#d4af37", marginBottom: 15 }}>Who I Am</h3>
        <p className="body-text">
          Hi! I am a passionate <strong style={{ color: "#f5e27a" }}>Data Analyst and Power BI Dashboard Developer</strong>.
          My goal is to translate raw and messy databases into clean, structured, and insightful visual interfaces.
          With a strong analytical mindset, I design dashboards that tell a story, highlight key metrics, and reveal
          hidden trends.
        </p>
        <p className="body-text" style={{ marginTop: 15 }}>
          In addition to business intelligence reporting, I build{" "}
          <strong style={{ color: "#f5e27a" }}>Machine Learning models</strong> to predict outcomes (such as housing
          prices) and run complex data mining operations. I utilize Python and industry-standard libraries to run
          exploratory data analysis (EDA), pre-process features, and construct reliable models.
        </p>
      </div>

      <div className="glass-card">
        <h3 style={{ color: "#f5e27a", marginBottom: 15 }}>Why Work With Me?</h3>
        <ul className="why-list">
          {REASONS.map(([title, text]) => (
            <li key={title}>
              <strong>{title}</strong> {text}
            </li>
          ))}
        </ul>
      </div>
    </section>
  );
}
