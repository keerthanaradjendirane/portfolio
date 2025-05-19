import streamlit as st
from PIL import Image
import time
import warnings
warnings.filterwarnings("ignore")

# --- Page Config ---
st.set_page_config(page_title="Keerthana Portfolio", layout="wide")

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
        color: #00e2e2; /* teal */
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
        color: #00e2e2;
        transition: color 0.5s ease, font-size 0.3s ease;
        font-size: 20px;
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
    <a href="#passion">Passion</a>
    <a href="#contact-me">Contact Me</a>
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
        
        "description": "A virtual classroom with all the basic features and with real time summarization and sending the summarized content to the host using flask, gemini api and react",
        "achievement":"1st prize at Sri Manakula Vinayagar Engineering College Technical Symposium and Semifinalist for a national level hackathon",
        "link": "https://meet-minds-ai-fea6.vercel.app/"
    },
    {
        "title": "Diet Plan Generator based on Medical History",
       
        "description": "A personalized AI-powered diet planner that takes the patients medical data to consideration and generates diet plan with customization using machine learning, flask, html,streamlit.",
        "achievement":"Shortlisted for Round 2 in Prestigious Product War Room competition organized by IIM! 🏆",
        "link": "https://dazzling-cranachan-8e85f3.netlify.app/"
    },
    {
        "title": "Virtual Data Analyst",
       
        "description": "Python-based virtual data analyst that replicates all data analysis tasks, including data visualization, model prediction, report generation, and dashboard creation. Integrated with the Gemini API, it features a chatbot for seamless interaction and automation of data-driven insights",
        "achievement":"Shortlisted among 25 teams for informatica global hackathon",
        "link": "https://chandiyafinal-kf6w6wgaqrdlvcrzuvzp6j.streamlit.app/"
    },
]

proj_cols = st.columns(3)

for i, project in enumerate(project_data):
    with proj_cols[i]:
        
        st.markdown(f"**{project['title']}**")
        st.write(project['description'])
        st.write(f"**Achievement:** {project['achievement']}")
        st.markdown(f"[🔗 Try This]({project['link']})")

st.markdown("---")

# --- TECHNICAL ACHIEVEMENTS SECTION ---
st.markdown("## Technical Achievements", unsafe_allow_html=True)

tachieve_data = [
    {
        "title": "1st Prize at the Technical Symposium",
        "image": "mech.png",
        "description": "We were awarded first prize at technical symposium  which was organized at Sri Manakula Vinayagar Engineering College for our virtual classroom with real time summarization project.",
        "link": "https://www.linkedin.com/posts/keerthana-radjendirane_hello-everyone-thrilled-to-share-activity-7187474443940642816-LV1h?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9fCjkBqZV7dZCK9S5KKBkvLbTU1emBJ_A"
    },
    {
        "title": "1st Prize at Science & Technology Quiz",
        "image": "quiz.jpeg",
        "description": "We were awarded first prize at Science and Technology quiz which was at organized at Sri Manakula Vinayagar Engineering College during the academic year 2024-2025.",
        "link": "https://www.linkedin.com/posts/keerthana-radjendirane_sciencequiz-technologyquiz-teamwork-activity-7177208105783480320-xz0b?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9fCjkBqZV7dZCK9S5KKBkvLbTU1emBJ_A"
    },
    {
        "title": "1st Prize at Technical Connection",
        "image": "symp2.png",
        "description": "We were awarded first prize at Technical Conection which was based on Science and Technology and was organized at Rajiv Gandhi Engineering College.",
        "link": "https://www.linkedin.com/posts/keerthana-radjendirane_hello-everyone-this-is-my-certificate-for-activity-7127328398707724289-xhe8?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9fCjkBqZV7dZCK9S5KKBkvLbTU1emBJ_A"
    },
]

achieve_cols = st.columns(3)

for i, item in enumerate(tachieve_data):
    with achieve_cols[i]:
        st.image(item["image"], use_container_width=True)
        st.markdown(f"**{item['title']}**")
        st.write(item['description'])
        st.markdown(f"[🔗 Know More]({item['link']})")

st.markdown("---")

# --- SOFT SKILL ACHIEVEMENTS SECTION ---
st.markdown("## Soft Skill Achievements", unsafe_allow_html=True)

softskill_data = [
    {"title": "Unstop Student Director", "description": "Campus Ambassador for Unstop at Sri Manakula Vinayagar Engineering College for the academic year 2024-2025.", "link": "https://www.linkedin.com/posts/keerthana-radjendirane_beunstoppable-unstop-campusambassador-activity-7259155730635595776-7QvV?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9fCjkBqZV7dZCK9S5KKBkvLbTU1emBJ_A"},
    {"title": "Secretary at SMVEC TM", "description": "Secretary at SMVEC Toastmasters Club from April 2024- Novembet 2024", "link": "https://www.linkedin.com/posts/keerthana-radjendirane_toastmasters-leadership-publicspeaking-activity-7233761040495222784-KAqS?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9fCjkBqZV7dZCK9S5KKBkvLbTU1emBJ_A"},
    {"title": "President at SMVEC TM",  "description": "President at SMVEC Toastmasters Club from November 2024- April 2025", "link": "https://www.linkedin.com/posts/keerthana-radjendirane_toastmasters-publicspeaking-leadership-activity-7295286174661623808-7aBz?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9fCjkBqZV7dZCK9S5KKBkvLbTU1emBJ_A"},
    {"title": "Youth Talk Finalist",  "description": "Finalist at Youth Talk Reginal Finale which was organized by ICT Academy 2024", "link": "https://www.linkedin.com/posts/keerthana-radjendirane_ictacademy-youthtalk2024-top10-activity-7258890296464146433--WGT?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9fCjkBqZV7dZCK9S5KKBkvLbTU1emBJ_A"},
    {"title": "Top 100 among 5000 speakers",  "description": "Was Sected as Top 100 among 5000 competetiors in ICT Youth Talk 2024", "link": "https://www.linkedin.com/posts/keerthana-radjendirane_ictacademy-youthtalk2024-top100-activity-7258888788578336768-RiWh?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9fCjkBqZV7dZCK9S5KKBkvLbTU1emBJ_A"},
    {"title": "Club Level Winner",  "description": "Was awarded Club Level Best Speaker for Humouous Speech Contest", "link": "https://www.linkedin.com/posts/keerthana-radjendirane_publicspeaking-toastmasters-proudmoment-activity-7258887344588562433-rIsp?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9fCjkBqZV7dZCK9S5KKBkvLbTU1emBJ_A"}
]

for i in range(0, len(softskill_data), 3):
    row = st.columns(3)
    for j in range(3):
        if i + j < len(softskill_data):
            item = softskill_data[i + j]
            with row[j]:
                
                st.markdown(f"**{item['title']}**")
                st.write(item['description'])
                st.markdown(f"[🔗 Know More]({item['link']})")

st.markdown("---")

# --- VOLUNTEERING SECTION ---
st.markdown("## Volunteering", unsafe_allow_html=True)

volunteering_data = [
    {"title": "IDSc", "description": "Mangaement Lead at Innovators and Developers Club(College Level Club)", "link": "https://www.linkedin.com/in/keerthana-radjendirane/"},
    {"title": "GDSC",  "description": "Volunteered myself for Event Organization at Google Developers and Students Club", "link": "https://www.linkedin.com/in/keerthana-radjendirane/"},
    {"title": "SMVEC TM", "description": "Organized Toastmasters 100 Years Celebration at SMVEC Toastmasters Club", "link": "https://www.linkedin.com/posts/keerthana-radjendirane_toastmasters-leadership-publicspeaking-activity-7233761040495222784-KAqS?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD9fCjkBqZV7dZCK9S5KKBkvLbTU1emBJ_A"}
]

vol_cols = st.columns(len(volunteering_data))

for i, item in enumerate(volunteering_data):
    with vol_cols[i]:
        
        st.markdown(f"**{item['title']}**")
        st.write(item['description'])
        st.markdown(f"[🔗 Know More]({item['link']})")

st.markdown("---")


# --- PASSION SECTION ---
st.markdown('<h2 id="Passion">Passion</h2>', unsafe_allow_html=True)


# Introductory Text
st.markdown("""
As a proficient public speaker and passionate tech enthusiast, I have transformed my love for technology and communication into a purpose-driven journey as a tech YouTuber. On my channel, I strive to bridge the gap between complexity and clarity by teaching emerging technologies such as Artificial Intelligence, Machine Learning, and Data Science in the most accessible way possible.

My content is crafted not only to educate but to empower learners of all levels—from beginners curious about coding to aspiring professionals eager to explore advanced concepts. I cover fundamental topics like Python programming and problem-solving techniques, complemented by real-world applications and project-based learning.

Beyond tutorials, I aim to spark curiosity, promote continuous learning, and build a vibrant community of tech-driven minds. Whether you're taking your first steps in programming or aiming to sharpen your skills in cutting-edge domains, my goal is to guide, motivate, and uplift you throughout the journey.

Because technology isn’t just a tool—it’s a platform to transform ideas into impact. Let’s innovate, learn, and grow together. """)

# Center-align YouTube video using HTML
youtube_video_url = "https://www.youtube.com/embed/53EIf_fgcnk"  # Embedded video URL

st.markdown(f"""
<div style="text-align: center;">
    <iframe width="560" height="315" src="{youtube_video_url}" 
    title="YouTube video player" frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen></iframe>
</div>
""", unsafe_allow_html=True)

# Link to YouTube Channel
youtube_channel_url = "https://www.youtube.com/@keerthanaradjendiraneaids"  # Your channel URL

st.markdown(f"""
<div style="text-align: center; padding-top: 15px;">
    <a href="{youtube_channel_url}" target="_blank" style="font-size: 18px; color: #008080; font-weight: bold;">
        🔗 Visit My Tech YouTube Channel
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# --- CONTACT ME SECTION ---
st.markdown('<h2 id="social-media-links">Contact Me</h2>', unsafe_allow_html=True)


st.markdown("""
Get in touch with me through email or connect on my social media platforms:

<p>📧 <a href="mailto:keerthanaradjendirane@gmail.com" style="color:#008080; font-weight:bold;">keerthanaradjendirane@gmail.com</a></p>

<p>
<a href="https://www.linkedin.com/in/keerthanaradjendirane" target="_blank" style="text-decoration:none; margin-right: 20px;">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="#0077B5" viewBox="0 0 24 24" style="vertical-align: middle;">
        <path d="M4.98 3.5a2.5 2.5 0 11-5 0 2.5 2.5 0 015 0zm.02 4.5H0v13h5v-13zm7.98 0H8v13h5v-6.78c0-3.18 4.17-3.44 4.17 0V21h5v-7.68c0-7.23-7.18-6.97-9.15-3.41V8z"/>
    </svg>
    <span style="color:#0077B5; font-weight:bold; vertical-align: middle;">LinkedIn</span>
</a>

<a href="https://github.com/keerthanaradjendirane" target="_blank" style="text-decoration:none;">
    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" fill="#ffffff" viewBox="0 0 24 24" style="vertical-align: middle;">
        <path d="M12 .3C5.4.3 0 5.7 0 12c0 5.3 3.4 9.8 8.2 11.4.6.1.8-.3.8-.6V21c-3.3.7-4-1.6-4-1.6-.5-1.3-1.3-1.7-1.3-1.7-1.1-.7.1-.7.1-.7
                 1.2.1 1.8 1.2 1.8 1.2 1.1 1.9 2.9 1.3 3.6 1 
                 .1-.8.4-1.3.7-1.6-2.7-.3-5.5-1.3-5.5-5.9 
                 0-1.3.5-2.4 1.2-3.3-.1-.3-.5-1.5.1-3.2 
                 0 0 1-.3 3.3 1.3 1-.3 2.1-.4 3.2-.4 
                 1.1 0 2.2.1 3.2.4 2.3-1.6 3.3-1.3 
                 3.3-1.3.6 1.7.2 2.9.1 3.2.8.9 
                 1.2 2 1.2 3.3 0 4.6-2.8 5.6-5.5 5.9
                 .4.3.8 1 .8 2v3c0 .3.2.7.8.6 
                 4.8-1.6 8.2-6.1 8.2-11.4C24 5.7 18.6.3 12 .3z"/>
    </svg>
    <span style="color:#ffffff; font-weight:bold; vertical-align: middle; margin-left: 10px;">GitHub</span>
</a>
</p>
""", unsafe_allow_html=True)

# Optional: Confirmation


# --- Typing Effect for About Me Text ---
about_me_text = (
    """ I'm Keerthana Radjendirane, an aspiring AI and Data Science professional passionate about solving real-world problems through cutting-edge technologies like Generative AI, Machine Learning, and LLMs. I specialize in building end-to-end AI applications using tools like LangChain, Flask, Streamlit, and the Gemini API.

Beyond the code, I thrive in collaborative spaces—having led award-winning projects such as a Real-Time Virtual Classroom Summarizer, a Medical-Aware Diet Planner, and an AI Virtual Data Analyst, recognized at national hackathons.

As President of SMVEC Toastmasters and Unstop Student Director, I bring strong communication and leadership skills. I was a Top 100 finalist in ICT Academy Youth Talk 2024, chosen from over 5000+ participants.  “I build AI models and deliver talks — proving that both humans and machines can learn to communicate better! 🤓🤖🎤”"""
)
text_so_far = ""
for char in about_me_text:
    text_so_far += char
    about_me_placeholder.markdown(text_so_far)
    time.sleep(0.00005)

# Load your resume file
with open("resume.pdf", "rb") as file:
    resume_data = file.read()

# Add a professional download button with accent color
st.download_button(
    label="📄 Download My Resume",
    data=resume_data,
    file_name="Keerthana_Radjendirane_Resume.pdf",
    mime="application/pdf",
    key="download-resume",
    help="Click to download my resume",
    # Optional styling (works with themes, you can customize)
    # You can wrap in st.markdown for more CSS if needed
)


