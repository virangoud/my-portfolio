// ⚙️ USER DATA CONFIGURATION — edit this file to update the portfolio content.

const githubUsername = "virangoud";


const portfolio = {
  name: "Viranagouda Patil",
  initials: "VP",
  roles: ["DATA ANALYST", "POWER BI DEVELOPER", "DATA SCIENTIST"],
  email: "patilveeresh035@gmail.com",
  githubUsername,
  githubUrl: `https://github.com/${githubUsername}`,
  linkedinUrl: "https://www.linkedin.com/in/virangoud-patil-22b4782bb",

  // 🛠️ SKILLS (add new skills to these lists)
  skills: [
    {
      title: "BI & Visualization",
      icon: "fa-chart-line",
      color: "#d4af37",
      items: [
        "Power BI",
        "DAX Formulas",
        "Power Query",
        "Dashboard Design",
        "Data Modeling",
        "Report Automation",
        "Excel Analysis",
      ],
    },
    {
      title: "Data Science & ML",
      icon: "fa-brain",
      color: "#f5e27a",
      items: [
        "Python",
        "Pandas / NumPy",
        "Exploratory Data Analysis",
        "Scikit-Learn",
        "Regression Models",
        "Feature Engineering",
        "Matplotlib / Seaborn",
        "DL Models",
      ],
    },
    {
      title: "Systems & Tools",
      icon: "fa-tools",
      color: "#b8860b",
      items: [
        "SQL Database",
        "Git / GitHub",
        "Jupyter Notebooks",
        "Data Processing",
        "Streamlit Web Apps",
        "Freelance Delivery",
        "Google Colab",
      ],
    },
  ],

  // 📁 LOCAL METADATA FOR KNOWN PROJECTS
  // Keys are GitHub repo names; these override what the GitHub API returns.
  localProjectsMetadata: {
    "Mens_Wear-Insighs-BI-": {
      customName: "Mens Wear Insights Dashboard",
      category: "Power BI",
      description:
        "A comprehensive Power BI dashboard analyzing menswear brand collections and their shirt varieties. Analyzes sales revenue, net profit margins, applied discount rates, and identifies top-performing products.",
      techStack: ["Power BI", "Data Modeling", "DAX", "Business Analysis"],
      client: null,
      profession: null,
    },
    "Patil-s-Paints-Insighs": {
      customName: "Patil's Paints Insights Dashboard",
      category: "Power BI",
      description:
        "An analytics dashboard designed for sales, inventory management, and product category analysis. Optimized for small-to-medium retail paint business monitoring.",
      techStack: ["Power BI", "Power Query", "Sales Visualization"],
      client: "Patil's Paints Store",
      profession: "BI Developer & Data Analyst",
    },
    "Hospital-Emergency-ward-analysis": {
      customName: "Hospital Emergency Ward Analysis",
      category: "SQL & Database",
      description:
        "Exploratory data analysis of emergency room records to optimize patient wait times and staffing. Highlights peak attendance hours, case severity distributions, and resource constraints.",
      techStack: ["SQL", "Data Cleaning", "Exploratory Analysis", "Matplotlib"],
      client: "Sangmeshwar Hospital",
      profession: "Healthcare Data Analyst",
    },
    House_price_Machine_model: {
      customName: "House Price Prediction Model",
      category: "Python & ML",
      description:
        "A predictive Machine Learning model constructed in Jupyter Notebook to forecast residential property values. Includes detailed exploratory data analysis (EDA), cleaning missing data, and regression modeling.",
      techStack: ["Python", "Scikit-Learn", "Pandas", "Machine Learning"],
      client: null,
      profession: null,
    },
  },

  // 📈 EXPERIENCE TIMELINE
  experience: [
    {
      date: "2025 - Present",
      title: "Freelance BI Developer & Data Analyst",
      company: "Self-Employed",
      description:
        "Designing and developing custom Power BI dashboard suites for diverse business segments. Writing efficient DAX calculations, resolving data relationships, and cleaning client data pipelines using Python/Pandas.",
    },
    {
      date: "2024 - 2025",
      title: "Data Projects Developer",
      company: "Independent Work",
      description:
        "Built end-to-end data pipelines for retail (Menswear collection metrics, Paint business KPIs) and healthcare (emergency room performance datasets). Implemented Machine Learning regression algorithms to forecast real estate and housing markets.",
    },
  ],
};

export default portfolio;
