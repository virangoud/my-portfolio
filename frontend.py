import streamlit as st
import os
import requests
# Set page configurations
st.set_page_config(
    page_title="Viranagouda Patil | Portfolio",
    layout="wide"
)
# Load and inject custom CSS
def load_css(css_file):
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file {css_file} not found.")
# Inject FontAwesome for modern icons
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
    unsafe_allow_html=True
)
load_css("style.css")
# =========================================================================
# ⚙️ USER DATA CONFIGURATION
# =========================================================================
name = "Viranagouda Patil"
roles = ["Data Analyst", "Power BI Developer", "Machine Learning Specialist"]
email = "patilveeresh035@gmail.com"
github_username = "virangoud"
github_url = f"https://github.com/{github_username}"
linkedin_url = "https://www.linkedin.com/in/virangoud-patil-22b4782bb"
# 🛠️ SKILLS SECTION DATA (Simply add new skills to these lists)
skills_data = {
    "BI & Visualization": [
        "Power BI", 
        "DAX Formulas", 
        "Power Query", 
        "Dashboard Design", 
        "Data Modeling", 
        "Report Automation", 
        "Excel Analysis"
    ],
    "Data Science & ML": [
        "Python", 
        "Pandas / NumPy", 
        "Exploratory Data Analysis", 
        "Scikit-Learn", 
        "Regression Models", 
        "Feature Engineering", 
        "Matplotlib / Seaborn",
        "DL Models "
    ],
    "Systems, SQL & Tools": [
        "SQL Database",
        "Git / GitHub", 
        "Jupyter Notebooks", 
        "Data Processing", 
        "Streamlit Web Apps", 
        "Freelance Delivery",
        "Google Colab"
    ]
}
# 📁 LOCAL CUSTOM METADATA FOR YOUR KNOWN PROJECTS
# (We use this to enhance description & tech stacks of your main repos)
local_projects_metadata = {
    "Mens_Wear-Insighs-BI-": {
        "custom_name": "Mens Wear Insights Dashboard",
        "category": "Power BI",
        "description": "A comprehensive Power BI dashboard analyzing menswear brand collections and their shirt varieties. Analyzes sales revenue, net profit margins, applied discount rates, and identifies top-performing products.",
        "tech_stack": ["Power BI", "Data Modeling", "DAX", "Business Analysis"],
        "client": None,
        "profession": None
    },
    "Patil-s-Paints-Insighs": {
        "custom_name": "Patil's Paints Insights Dashboard",
        "category": "Power BI",
        "description": "An analytics dashboard designed for sales, inventory management, and product category analysis. Optimized for small-to-medium retail paint business monitoring.",
        "tech_stack": ["Power BI", "Power Query", "Sales Visualization"],
        "client": "Patil's Paints Store",
        "profession": "BI Developer & Data Analyst"
    },
    "Hospital-Emergency-ward-analysis": {
        "custom_name": "Hospital Emergency Ward Analysis",
        "category": "SQL & Database",
        "description": "Exploratory data analysis of emergency room records to optimize patient wait times and staffing. Highlights peak attendance hours, case severity distributions, and resource constraints.",
        "tech_stack": ["SQL", "Data Cleaning", "Exploratory Analysis", "Matplotlib"],
        "client": "Sangmeshwar Hospital",
        "profession": "Healthcare Data Analyst"
    },
    "House_price_Machine_model": {
        "custom_name": "House Price Prediction Model",
        "category": "Python & ML",
        "description": "A predictive Machine Learning model constructed in Jupyter Notebook to forecast residential property values. Includes detailed exploratory data analysis (EDA), cleaning missing data, and regression modeling.",
        "tech_stack": ["Python", "Scikit-Learn", "Pandas", "Machine Learning"],
        "client": None,
        "profession": None
    }
}
# 🌐 LIVE GITHUB FETCH FUNCTION
@st.cache_data(ttl=600)  # Cache results for 10 minutes to avoid API rate limiting
def fetch_github_projects(username):
    projects = []
    try:
        url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            repos = response.json()
            for repo in repos:
                # Skip forks
                if repo.get("fork", False):
                    continue
                    
                repo_name = repo["name"]
                proj = {
                    "name": repo_name.replace("-", " ").replace("_", " ").title(),
                    "category": "Python & ML", 
                    "description": repo.get("description") or "No description provided on GitHub yet.",
                    "tech_stack": [repo.get("language")] if repo.get("language") else ["Data Analysis"],
                    "github_url": repo["html_url"],
                    "stars": repo.get("stargazers_count", 0),
                    "repo_key": repo_name
                }
                
                # Auto Categorizer based on name & language
                lower_name = repo_name.lower()
                lower_desc = (repo.get("description") or "").lower()
                lower_lang = (repo.get("language") or "").lower()
                
                if "bi" in lower_name or "dashboard" in lower_name or "powerbi" in lower_name or "insights" in lower_name or "wear" in lower_name or "paint" in lower_name:
                    proj["category"] = "Power BI"
                elif "sql" in lower_name or "database" in lower_name or "db" in lower_name or "query" in lower_name or "ward" in lower_name:
                    proj["category"] = "SQL & Database"
                elif "model" in lower_name or "predict" in lower_name or "price" in lower_name or "machine" in lower_name or "jupyter" in lower_name or "python" in lower_lang or "notebook" in lower_lang:
                    proj["category"] = "Python & ML"
                
                # Merge with local custom metadata if available
                if repo_name in local_projects_metadata:
                    meta = local_projects_metadata[repo_name]
                    proj["name"] = meta["custom_name"]
                    proj["category"] = meta["category"]
                    proj["description"] = meta["description"]
                    proj["tech_stack"] = meta["tech_stack"]
                    proj["client"] = meta.get("client")
                    proj["profession"] = meta.get("profession")
                
                projects.append(proj)
        else:
            projects = get_fallback_projects()
    except Exception as e:
        projects = get_fallback_projects()
        
    return projects
def get_fallback_projects():
    projects = []
    for repo_name, meta in local_projects_metadata.items():
        projects.append({
            "name": meta["custom_name"],
            "category": meta["category"],
            "description": meta["description"],
            "tech_stack": meta["tech_stack"],
            "github_url": f"https://github.com/{github_username}/{repo_name}",
            "stars": 0,
            "repo_key": repo_name,
            "client": meta.get("client"),
            "profession": meta.get("profession")
        })
    return projects
# Fetch projects dynamically
all_projects = fetch_github_projects(github_username)
# Helper function to render a single project card
def render_project_card(project):
    category = project["category"]
    stars_str = f' | ★ {project["stars"]}' if project.get("stars", 0) > 0 else ""
    
    if category == "Power BI":
        badge_color = "#d4af37"   # Gold
        badge_bg = "rgba(212, 175, 55, 0.1)"
        border_color = "rgba(212, 175, 55, 0.3)"
        text_btn_color = "#0a0a0a"
    elif category == "SQL & Database":
        badge_color = "#f5e27a"   # Light gold
        badge_bg = "rgba(245, 226, 122, 0.1)"
        border_color = "rgba(245, 226, 122, 0.3)"
        text_btn_color = "#0a0a0a"
    else:  # Python & ML
        badge_color = "#b8860b"   # Dark gold
        badge_bg = "rgba(184, 134, 11, 0.12)"
        border_color = "rgba(184, 134, 11, 0.35)"
        text_btn_color = "#f5e27a"
    tech_tags = "".join(f'<span class="tech-tag">{tech}</span>' for tech in project["tech_stack"])
    
    # Build client/company hover badge if available
    client = project.get("client")
    profession = project.get("profession")
    client_html = ""
    if client:
        client_html = (
            '<div style="margin-bottom: 12px;">'
            f'  <div class="client-badge" style="display: inline-flex; align-items: center; gap: 8px;'
            f'       background: rgba(212,175,55,0.08); border: 1px solid rgba(212,175,55,0.25);'
            f'       border-radius: 8px; padding: 6px 12px; cursor: default; position: relative;">'
            f'    <i class="fas fa-building" style="color: {badge_color}; font-size: 0.8rem;"></i>'
            f'    <span style="color: #c9b78a; font-size: 0.82rem; font-weight: 600;">{client}</span>'
            f'    <div class="client-tooltip" style="position: absolute; bottom: 110%; left: 50%; transform: translateX(-50%);'
            f'         background: #1a1500; border: 1px solid {badge_color}; border-radius: 8px;'
            f'         padding: 6px 12px; white-space: nowrap; z-index: 10; pointer-events: none;'
            f'         font-size: 0.78rem; color: {badge_color}; font-weight: 600; opacity: 0; transition: opacity 0.2s;">'
            f'      <i class="fas fa-user-tie" style="margin-right: 6px;"></i>{profession}'
            f'    </div>'
            f'  </div>'
            '</div>'
        )
    card_html = f'''
    <div class="glass-card">
    <div style="display: flex; justify-content: space-between; align-items: start;">
      <h3 style="color: {badge_color}; margin-top: 0; margin-bottom: 5px; font-weight:700;">{project["name"]}</h3>
      <span style="background: {badge_bg}; color: {badge_color}; border: 1px solid {border_color}; padding: 2px 8px; border-radius: 12px; font-size: 0.75rem; font-weight: bold;">{category}{stars_str}</span>
    </div>
    {client_html}
    <p style="color: #c9b78a; font-size: 0.95rem; margin-top: 10px; margin-bottom: 15px; line-height: 1.5; min-height: 70px;">
      {project["description"]}
    </p>
    <div style="margin-bottom: 20px;">
      {tech_tags}
    </div>
    <a href="{project["github_url"]}" target="_blank" class="btn-glow" 
       style="padding: 6px 16px; font-size: 0.85rem; background: {badge_color}; box-shadow: 0 0 15px {badge_bg}; color: {text_btn_color} !important;">
       <i class="fab fa-github" style="margin-right: 5px;"></i> View Repository
    </a>
    </div>
    '''
    return card_html
# =========================================================================
# 🏠 SINGLE-PAGE LANDING
# =========================================================================
# Navigation Bar Header (Top Navigation Links)
st.markdown(
    f'''
    <div style="display: flex; justify-content: space-between; align-items: center; 
                padding: 15px 30px; background: rgba(10, 10, 10, 0.9); backdrop-filter: blur(10px);
                border-bottom: 1px solid rgba(212, 175, 55, 0.2); border-radius: 12px; margin-bottom: 30px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.5);">
        <div style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; font-weight: 800; background: linear-gradient(135deg, #d4af37, #f5e27a); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">VP</div>
        <div style="display: flex; gap: 20px;">
            <a href="#home" style="color: #a08c5a; text-decoration: none; font-weight: 600; font-size: 0.95rem; transition: color 0.2s;">Home</a>
            <a href="#about" style="color: #a08c5a; text-decoration: none; font-weight: 600; font-size: 0.95rem;">About</a>
            <a href="#skills" style="color: #a08c5a; text-decoration: none; font-weight: 600; font-size: 0.95rem;">Skills</a>
            <a href="#projects" style="color: #a08c5a; text-decoration: none; font-weight: 600; font-size: 0.95rem;">Projects</a>
            <a href="#experience" style="color: #a08c5a; text-decoration: none; font-weight: 600; font-size: 0.95rem;">Experience</a>
            <a href="#contact" style="color: #a08c5a; text-decoration: none; font-weight: 600; font-size: 0.95rem;">Contact</a>
        </div>
    </div>
    ''',
    unsafe_allow_html=True
)
# 1. HOME SECTION
st.markdown('<div id="home"></div>', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown(
        f'<h1 class="hero-title">{name}</h1>'
        f'<div class="hero-subtitle">Data Analyst & Power BI Dashboard Expert</div>',
        unsafe_allow_html=True
    )
    
    st.markdown(
        '<p style="font-size: 1.15rem; line-height: 1.7; color: #c9b78a; margin-bottom: 30px; max-width: 700px;">'
        'I transform complex datasets into high-impact visual stories. Specializing in '
        '<strong style="color: #d4af37;">Power BI interactive dashboards</strong>, database analysis, and '
        '<strong style="color: #f5e27a;">machine learning predictive models</strong>, I help businesses '
        'and clients make data-driven decisions that increase profitability and optimize operations.'
        '</p>',
        unsafe_allow_html=True
    )
    
    # Action Buttons
    st.markdown(
        f'<div style="display: flex; gap: 15px; flex-wrap: wrap; margin-bottom: 25px;">'
        f'<a href="#contact" class="btn-glow">Get In Touch</a>'
        f'<a href="{github_url}" target="_blank" class="btn-outline"><i class="fab fa-github" style="margin-right: 8px;"></i> GitHub Profile</a>'
        f'</div>',
        unsafe_allow_html=True
    )
    
    # Social Icons
    st.markdown(
        f'<div class="social-links" style="margin-top: 15px;">'
        f'<a href="{github_url}" target="_blank" class="social-icon"><i class="fab fa-github"></i></a>'
        f'<a href="{linkedin_url}" target="_blank" class="social-icon"><i class="fab fa-linkedin"></i></a>'
        f'<a href="mailto:{email}" class="social-icon"><i class="fas fa-envelope"></i></a>'
        f'</div>',
        unsafe_allow_html=True
    )
with col2:
    # Decorative gold data visual with cycling role titles
    st.markdown(
        '''
        <div style="text-align: center; padding: 20px;">
            <div style="width: 220px; height: 220px; border-radius: 50%;
                        background: radial-gradient(circle at 35% 35%, rgba(212,175,55,0.18), rgba(184,134,11,0.06) 70%);
                        border: 2px solid rgba(212,175,55,0.4);
                        box-shadow: 0 0 50px rgba(212,175,55,0.22), inset 0 0 35px rgba(212,175,55,0.06);
                        display: inline-flex; align-items: center; justify-content: center;
                        animation: pulse-gold 3s ease-in-out infinite;">
                <div style="text-align:center;">
                    <div style="font-family: Outfit, sans-serif; font-size: 3.8rem; font-weight: 900;
                                background: linear-gradient(135deg, #d4af37 0%, #f5e27a 50%, #b8860b 100%);
                                -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                                line-height: 1;">VP</div>
                    <div style="height: 28px; overflow: hidden; margin-top: 6px;">
                        <div id="role-cycle" style="font-size: 0.58rem; color: #d4af37; font-weight: 700;
                                                     letter-spacing: 2.5px; line-height: 28px;">
                            DATA ANALYST
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <style>
        @keyframes pulse-gold {
            0%, 100% { box-shadow: 0 0 30px rgba(212,175,55,0.18), inset 0 0 20px rgba(212,175,55,0.04); }
            50%       { box-shadow: 0 0 60px rgba(212,175,55,0.40), inset 0 0 40px rgba(212,175,55,0.10); }
        }
        @keyframes fadeSlideUp {
            0%   { opacity: 0; transform: translateY(10px); }
            15%  { opacity: 1; transform: translateY(0); }
            75%  { opacity: 1; transform: translateY(0); }
            90%  { opacity: 0; transform: translateY(-10px); }
            100% { opacity: 0; transform: translateY(-10px); }
        }
        .role-label {
            display: inline-block;
            font-size: 0.58rem;
            color: #d4af37;
            font-weight: 700;
            letter-spacing: 2.5px;
            animation: fadeSlideUp 3s ease-in-out infinite;
            position: absolute;
            width: 100%;
            left: 0;
            text-align: center;
        }
        #role-cycle {
            position: relative;
            height: 20px;
            display: block;
        }
        </style>
        <script>
        (function() {
            const roles = ["DATA ANALYST", "POWER BI DEVELOPER", "DATA SCIENTIST"];
            let current = 0;
            const el = document.getElementById("role-cycle");
            if (!el) return;

            function showRole(index) {
                const span = document.createElement("span");
                span.className = "role-label";
                span.textContent = roles[index];
                // Clear previous
                while (el.firstChild) el.removeChild(el.firstChild);
                el.appendChild(span);
            }

            showRole(0);
            setInterval(function() {
                current = (current + 1) % roles.length;
                showRole(current);
            }, 3000);
        })();
        </script>
        ''',
        unsafe_allow_html=True
    )
# 2. ABOUT ME SECTION
st.markdown('<div id="about" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2 style="background: linear-gradient(135deg, #d4af37, #f5e27a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem;">👤 About Me</h2>', unsafe_allow_html=True)
st.markdown(
    '<div class="glass-card">'
    '<h3 style="color: #d4af37; margin-bottom: 15px;">Who I Am</h3>'
    '<p style="font-size: 1.05rem; line-height: 1.7; color: #c9b78a;">'
    'Hi! I am a passionate <strong style="color: #f5e27a;">Data Analyst and Power BI Dashboard Developer</strong>. '
    'My goal is to translate raw and messy databases into clean, structured, and insightful visual interfaces. '
    'With a strong analytical mindset, I design dashboards that tell a story, highlight key metrics, and reveal hidden trends.'
    '</p>'
    '<p style="font-size: 1.05rem; line-height: 1.7; color: #c9b78a; margin-top: 15px;">'
    'In addition to business intelligence reporting, I build <strong style="color: #f5e27a;">Machine Learning models</strong> to predict '
    'outcomes (such as housing prices) and run complex data mining operations. I utilize Python and industry-standard '
    'libraries to run exploratory data analysis (EDA), pre-process features, and construct reliable models.'
    '</p>'
    '</div>'
    '<div class="glass-card">'
    '<h3 style="color: #f5e27a; margin-bottom: 15px;">Why Work With Me?</h3>'
    '<ul style="color: #c9b78a; line-height: 1.8; margin-left: 20px; font-size: 1.05rem;">'
    '<li><strong style="color: #d4af37;">Business-Centric Dashboards:</strong> I don\'t just make charts; I design reports around core business objectives (Sales growth, profit margins, cost reductions).</li>'
    '<li><strong style="color: #d4af37;">Clean Data Prep:</strong> Experienced in writing DAX queries, Power Query transformations, and Python pipelines to handle missing data and outliers.</li>'
    '<li><strong style="color: #d4af37;">Version Control & Git:</strong> All my work is structured, documented, and version-controlled via GitHub, ensuring high reliability.</li>'
    '<li><strong style="color: #d4af37;">Fast Delivery & Collaboration:</strong> Transparent communication, milestone updates, and prompt responses.</li>'
    '</ul>'
    '</div>',
    unsafe_allow_html=True
)
# 3. SKILLS SECTION
st.markdown('<div id="skills" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2 style="background: linear-gradient(135deg, #d4af37, #f5e27a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem;">🛠️ Skills & Expertise</h2>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="glass-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown(
        '<h3 style="color: #d4af37; border-bottom: 1px solid rgba(212, 175, 55, 0.2); padding-bottom: 10px; margin-bottom: 15px;">'
        '<i class="fas fa-chart-line" style="margin-right: 10px;"></i> BI & Visualization'
        '</h3>', 
        unsafe_allow_html=True
    )
    for skill in skills_data["BI & Visualization"]:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="glass-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown(
        '<h3 style="color: #f5e27a; border-bottom: 1px solid rgba(245, 226, 122, 0.2); padding-bottom: 10px; margin-bottom: 15px;">'
        '<i class="fas fa-brain" style="margin-right: 10px;"></i> Data Science & ML'
        '</h3>', 
        unsafe_allow_html=True
    )
    for skill in skills_data["Data Science & ML"]:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="glass-card" style="height: 100%;">', unsafe_allow_html=True)
    st.markdown(
        '<h3 style="color: #b8860b; border-bottom: 1px solid rgba(184, 134, 11, 0.2); padding-bottom: 10px; margin-bottom: 15px;">'
        '<i class="fas fa-tools" style="margin-right: 10px;"></i> Systems & Tools'
        '</h3>', 
        unsafe_allow_html=True
    )
    for skill in skills_data["Systems, SQL & Tools"]:
        st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
# 4. PROJECTS SECTION
st.markdown('<div id="projects" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2 style="background: linear-gradient(135deg, #d4af37, #f5e27a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem;">📁 Projects Portfolio</h2>', unsafe_allow_html=True)
# Separate projects into category lists dynamically
power_bi_projects = [p for p in all_projects if p["category"] == "Power BI"]
sql_projects = [p for p in all_projects if p["category"] == "SQL & Database"]
python_projects = [p for p in all_projects if p["category"] == "Python & ML"]
# Subsection: Power BI Dashboards
if power_bi_projects:
    st.markdown('<h3 style="color: #d4af37; margin-top: 25px; margin-bottom: 15px;"><i class="fas fa-chart-pie"></i> Power BI Dashboards</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for idx, project in enumerate(power_bi_projects):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(render_project_card(project), unsafe_allow_html=True)
# Subsection: SQL & Database Analysis
if sql_projects:
    st.markdown('<h3 style="color: #f5e27a; margin-top: 25px; margin-bottom: 15px;"><i class="fas fa-database"></i> SQL & Database Analysis</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for idx, project in enumerate(sql_projects):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(render_project_card(project), unsafe_allow_html=True)
# Subsection: Python & Machine Learning
if python_projects:
    st.markdown('<h3 style="color: #b8860b; margin-top: 25px; margin-bottom: 15px;"><i class="fas fa-laptop-code"></i> Python & Machine Learning</h3>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    for idx, project in enumerate(python_projects):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(render_project_card(project), unsafe_allow_html=True)
if not power_bi_projects and not sql_projects and not python_projects:
    st.info("No public projects fetched from your GitHub profile yet. Check your username configuration in app.py!")
# 5. EXPERIENCE & FREELANCE SERVICES
st.markdown('<div id="experience" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2 style="background: linear-gradient(135deg, #d4af37, #f5e27a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem;">📈 Experience & Freelance Services</h2>', unsafe_allow_html=True)
st.markdown(
    '<div class="glass-card" style="border-left: 5px solid #d4af37;">'
    '<h3 style="color: #d4af37; margin-top: 0;"><i class="fas fa-handshake" style="margin-right: 10px;"></i> Available for Freelance & Contract Work</h3>'
    '<p style="color: #c9b78a; line-height: 1.6;">'
    'I provide custom dashboard building and data services for startups and small-to-medium businesses. '
    'If you have messy Excel files or SQL tables, I can transform them into a clean, auto-updating dashboard. '
    'I also develop custom predictive models to help forecast sales, stock requirements, or client retention.'
    '</p>'
    '</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="timeline">'
    '  <div class="timeline-item">'
    '    <div class="timeline-date">2025 - Present</div>'
    '    <div class="timeline-title">Freelance BI Developer & Data Analyst</div>'
    '    <div class="timeline-company">Self-Employed</div>'
    '    <p style="color: #c9b78a; font-size: 0.95rem;">'
    '      Designing and developing custom Power BI dashboard suites for diverse business segments. '
    '      Writing efficient DAX calculations, resolving data relationships, and cleaning client data pipelines using Python/Pandas.'
    '    </p>'
    '  </div>'
    '  <div class="timeline-item">'
    '    <div class="timeline-date">2024 - 2025</div>'
    '    <div class="timeline-title">Data Projects Developer</div>'
    '    <div class="timeline-company">Independent Work</div>'
    '    <p style="color: #c9b78a; font-size: 0.95rem;">'
    '      Built end-to-end data pipelines for retail (Menswear collection metrics, Paint business KPIs) and healthcare (emergency room performance datasets). '
    '      Implemented Machine Learning regression algorithms to forecast real estate and housing markets.'
    '    </p>'
    '  </div>'
    '</div>',
    unsafe_allow_html=True
)
# 6. CONTACT SECTION
st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown('<h2 style="background: linear-gradient(135deg, #d4af37, #f5e27a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem;">✉️ Contact Me</h2>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown(
        '<div class="glass-card" style="height: 100%;">'
        '<h3 style="color: #d4af37; margin-top: 0;">Get in Touch</h3>'
        '<p style="color: #c9b78a; margin-bottom: 25px; line-height: 1.6;">'
        'Have a project in mind, a job opportunity, or a dashboard you need built? '
        'Feel free to send a message or contact me directly via email. I look forward to working with you!'
        '</p>'
        '<div style="margin-bottom: 15px;">'
        '  <strong style="color: #f5e27a;"><i class="fas fa-envelope" style="margin-right: 10px;"></i> Email:</strong><br>'
        f'  <a href="mailto:{email}" style="color: #c9b78a; text-decoration: none;">{email}</a>'
        '</div>'
        '<div style="margin-bottom: 15px;">'
        '  <strong style="color: #f5e27a;"><i class="fab fa-github" style="margin-right: 10px;"></i> GitHub:</strong><br>'
        f'  <a href="{github_url}" target="_blank" style="color: #c9b78a; text-decoration: none;">github.com/{github_username}</a>'
        '</div>'
        '<div style="margin-bottom: 15px;">'
        '  <strong style="color: #f5e27a;"><i class="fab fa-linkedin" style="margin-right: 10px;"></i> LinkedIn:</strong><br>'
        f'  <a href="{linkedin_url}" target="_blank" style="color: #c9b78a; text-decoration: none;">{linkedin_url.replace("https://www.", "")}</a>'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #f5e27a; margin-top: 0; margin-bottom: 15px;">Send a Message</h3>', unsafe_allow_html=True)
    
    with st.form("contact_form", clear_on_submit=True):
        contact_name = st.text_input("Your Name")
        contact_email = st.text_input("Your Email Address")
        message = st.text_area("Your Message", height=120, placeholder="Tell me about your project or enquiry...")

        submitted = st.form_submit_button("📨 Send Message")
        if submitted:
            if contact_name and contact_email and message:
                try:
                    response = requests.post(
                        f"https://formsubmit.co/ajax/{email}",
                        json={
                            "name": contact_name,
                            "email": contact_email,
                            "message": message,
                            "_subject": f"Portfolio Contact from {contact_name}",
                            "_captcha": "false"
                        },
                        headers={"Content-Type": "application/json", "Accept": "application/json"},
                        timeout=10
                    )
                    if response.status_code == 200:
                        st.success("✅ Message sent! I'll get back to you soon at " + email)
                    else:
                        st.warning("⚠️ Could not deliver right now. Please email me directly at " + email)
                except Exception:
                    st.warning("⚠️ Network issue. Please email me directly at " + email)
            else:
                st.error("Please fill in all fields before submitting.")
    st.markdown('</div>', unsafe_allow_html=True)
