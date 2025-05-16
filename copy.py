import streamlit as st
from PIL import Image
import time

# --- Page Config ---
st.set_page_config(page_title="AI Portfolio", layout="wide")

# --- Custom CSS Styling ---
st.markdown("""
<style>
    /* Reduce container width to ~50% and center */
    .css-18e3th9 {
        max-width: 700px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding: 20px 10px 40px 10px !important;
    }

    body {
        font-family: 'Segoe UI', sans-serif;
        background-color: #0e1117; /* dark background */
        color: #fff;
    }

    /* Images styling */
    .css-1cpxqw2 img, .stImage > img {
        border-radius: 16px;
        object-fit: cover;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        width: 100% !important;
        max-height: 150px !important;
        height: auto !important;
    }

    /* Headings colors changed to teal */
    .stMarkdown h2 {
        color: #008080; /* teal */
        font-weight: 700;
    }

    .stMarkdown h3 {
        color: #20B2AA; /* light teal */
        font-weight: 600;
    }

    /* Paragraph and list text */
    .stMarkdown p, .stMarkdown li {
        font-size: 16px;
        line-height: 1.6;
        color: #fff;
    }

    /* Nav menu: bigger size, teal colors */
    .nav-menu {
        background-color: transparent;
        padding: 25px 0;
        text-align: center;
        margin-bottom: 40px;
        box-shadow: none;
        border-radius: 0;
        font-size: 18px;
        font-weight: 700;
    }

    .nav-menu a {
        margin: 0 30px;
        text-decoration: none;
        color: #008080;
        transition: color 0.2s ease;
    }

    .nav-menu a:hover {
        color: #20B2AA;
    }

    /* Section title style */
    .section-title {
        margin-top: 30px;
        font-size: 28px;
        font-weight: bold;
        color: #008080;
    }

    /* Card hover effect */
    .card:hover {
        transform: scale(1.02);
        transition: transform 0.2s ease;
    }
</style>
""", unsafe_allow_html=True)

# --- Navigation Bar ---
st.markdown("""
<div class="nav-menu">
    <a href="#about-me">About Me</a>
    <a href="#projects">Projects</a>
    <a href="#technical-achievements">Technical Achievements</a>
    <a href="#soft-skill-achievements">Soft Skill Achievements</a>
    <a href="#volunteering">Volunteering</a>
    <a href="#contact-me">Contact Me</a>
    <a href="#social-media-links">Social Media Links</a>
</div>
""", unsafe_allow_html=True)

# --- Load Profile Image ---
profile_image = Image.open("image.png")

# --- ABOUT ME SECTION ---
st.markdown("## About Me", unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Keerthana Radjendirane")
    about_me_placeholder = st.empty()  # Placeholder for typing effect

with col2:
    st.image(profile_image, width=280, caption="Keerthana")

st.markdown("---")

# --- PROJECTS SECTION ---
st.markdown("## Projects", unsafe_allow_html=True)

project_data = [
    {
        "title": "Virtual Classroom with AI Summarization",
        "image": "image.png",
        "description": "A virtual classroom with all the basic features and with real time summarization and sending the summarized content to the host using flask, gemini api and react",
        "achievemnent":"1st prize at Sri Manakula Vinayagar Engineering College Technical Symposium and Semifinalist for a national level hackathon",
        "link": "https://example.com/virtual-classroom"
    },
    {
        "title": "Diet Plan Generator based on Medical History",
        "image": "image.png",
        "description": "A personalized AI-powered diet planner that takes the patients medical data to consideration and generates diet plan with customization using machine learning, flask, html,streamlit.",
        "achievemnent":"Shortlisted for Round 2 in Prestigious Product War Room competition organized by IIM! 🏆",
        "link": "https://example.com/diet-generator"
    },
    {
        "title": "Virtual Data Analyst",
        "image": "image.png",
        "description": "Python-based virtual data analyst that replicates all data analysis tasks, including data visualization, model prediction, report generation, and dashboard creation. Integrated with the Gemini API, it features a chatbot for seamless interaction and automation of data-driven insights",
        "achievemnent":"Shortlisted among 25 teams for informatica global hackathon",
        "link": "https://example.com/virtual-analyst"
    },
]

proj_cols = st.columns(3)

for i, project in enumerate(project_data):
    with proj_cols[i]:
        st.image(project["image"], use_column_width=True)
        st.markdown(f"**{project['title']}**")
        st.write(project['description'])
        st.write(f"**Achievement:** {project['achievemnent']}")
        st.markdown(f"[🔗 Try This]({project['link']})")

st.markdown("---")

# --- TECHNICAL ACHIEVEMENTS SECTION ---
st.markdown("## Technical Achievements", unsafe_allow_html=True)

tachieve_data = [
    {
        "title": "1st Prize at the Technical Symposium",
        "image": "mech.png",
        "description": "We were awarded first prize at technical symposium  which was organized at Sri Manakula Vinayagar Engineering College for our virtual classroom with real time summarization project.",
        "link": "https://example.com/tech-symposium"
    },
    {
        "title": "1st Prize at Science & Technology Quiz",
        "image": "quiz.jpeg",
        "description": "We were awarded first prize at Science and Technology quiz which was at organized at Sri Manakula Vinayagar Engineering College during the academic year 2024-2025.",
        "link": "https://example.com/tech-quiz"
    },
    {
        "title": "1st Prize at Technical Connection",
        "image": "symp2.png",
        "description": "We were awarded first prize at Technical Conection which was based on Science and Technology and was organized at Rajiv Gandhi Engineering College.",
        "link": "https://example.com/tech-connection"
    },
]

achieve_cols = st.columns(3)

for i, item in enumerate(tachieve_data):
    with achieve_cols[i]:
        st.image(item["image"], use_column_width=True)
        st.markdown(f"**{item['title']}**")
        st.write(item['description'])
        st.markdown(f"[🔗 Try This]({item['link']})")

st.markdown("---")

# --- SOFT SKILL ACHIEVEMENTS SECTION ---
st.markdown("## Soft Skill Achievements", unsafe_allow_html=True)

softskill_data = [
    {"title": "Unstop Student Director", "image": "unstop.png", "description": "Campus Ambassador for Unstop at Sri Manakula Vinayagar Engineering College for the academic year 2024-2025.", "link": "https://example.com/hackathon"},
    {"title": "Secretary at SMVEC TM", "image": "secretary.png", "description": "Secretary at SMVEC Toastmasters Club from April 2024- Novembet 2024", "link": "https://example.com/event"},
    {"title": "President at SMVEC TM", "image": "president.png", "description": "President at SMVEC Toastmasters Club from November 2024- April 2025", "link": "https://example.com/speaker"},
    {"title": "Youth Talk Finalist", "image": "youth2.png", "description": "Finalist at Youth Talk Reginal Finale which was organized by ICT Academy 2024", "link": "https://example.com/public-speaking"},
    {"title": "Top 100 among 5000 speakers", "image": "youth1.png", "description": "Was Sected as Top 100 among 5000 competetiors in ICT Youth Talk 2024", "link": "https://example.com/mentoring"},
    {"title": "Club Level Winner", "image": "clubcontest.png", "description": "Was awarded Club Level Best Speaker for Humouous Speech Contest", "link": "https://example.com/moderator"}
]

for i in range(0, len(softskill_data), 3):
    row = st.columns(3)
    for j in range(3):
        if i + j < len(softskill_data):
            item = softskill_data[i + j]
            with row[j]:
                st.image(item["image"], use_column_width=True)
                st.markdown(f"**{item['title']}**")
                st.write(item['description'])
                st.markdown(f"[🔗 Try This]({item['link']})")

st.markdown("---")

# --- VOLUNTEERING SECTION ---
st.markdown("## Volunteering", unsafe_allow_html=True)

volunteering_data = [
    {"title": "Management Lead", "image": "idsc.jpeg", "description": "Mangaement Lead at Innovators and Developers Club(College Level Club)", "link": "https://example.com/tech-club"},
    {"title": "Event Organizer", "image": "gdsc.png", "description": "Volunteered myself for Event Organization at Google Developers and Students Club", "link": "https://example.com/tutor"},
    {"title": "Event Organizer and Public Speaker", "image": "100.png", "description": "Organized Toastmasters 100 Years Celebration at SMVEC Toastmasters Club", "link": "https://example.com/ngo"}
]

vol_cols = st.columns(len(volunteering_data))

for i, item in enumerate(volunteering_data):
    with vol_cols[i]:
        st.image(item["image"], use_column_width=True)
        st.markdown(f"**{item['title']}**")
        st.write(item['description'])
        st.markdown(f"[🔗 Try This]({item['link']})")

st.markdown("---")

# --- CONTACT SECTION ---
st.markdown("## Contact Me", unsafe_allow_html=True)
st.markdown("""
- 📧 **Email**: your.email@example.com  
- 📱 **Phone**: +91-XXXXXXXXXX
""")

st.markdown("---")

# --- SOCIAL MEDIA LINKS SECTION ---
st.markdown("## Social Media Links", unsafe_allow_html=True)
st.markdown("""
- [🔗 LinkedIn](https://www.linkedin.com/in/yourprofile)
- [🔗 GitHub](https://github.com/yourprofile)
- [🔗 Twitter](https://twitter.com/yourprofile)
""")

st.success("✅ Portfolio Loaded Successfully!")

# --- Typing Effect for About Me Text ---
about_me_text = (
    "Aspiring AI and Data Science student with expertise in generative AI, machine learning, and data science. "
    "Skilled in designing and deploying AI solutions with Deep Learning, NLP, LLM and LangChain. "
    "Demonstrated project leadership and event coordination, with a strong academic record. "
    "Passionate about applying technical skills and collaborative problem-solving to drive innovation in AI and technology."
)

text_so_far = ""
for char in about_me_text:
    text_so_far += char
    about_me_placeholder.markdown(text_so_far)
    time.sleep(0.00005)
