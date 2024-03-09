from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume Manu Sharma.pdf"
profile_pic = current_dir / "assets" / "profile-pic-b.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Manu Sharma"
PAGE_ICON = "random"
DESCRIPTION = """
As a recent CS graduate I am eager to embark on my professional journey.
With a strong foundation in programming and a passion for problem solving, 
I am enthusiastically pursuing opportunities in both **software development engineering** and **data science**. 
Whether it's crafting elegant code to build robust applications or delving into complex data analysis to derive actionable insights, I am open to starting my career in either role.
"""

SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/manu-sharma229/",
    "GitHub": "https://github.com/r-ocke-r",
    "Twitter": "https://twitter.com/Manusharma79105",
    "Leetcode": "https://leetcode.com/r_ocke_r"
}
platform_icons = {
    "LinkedIn": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
    "GitHub": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
    "Twitter": "https://cdn-icons-png.flaticon.com/512/124/124021.png",
    "Leetcode": "https://assets.leetcode.com/static_assets/public/icons/favicon.ico"
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide", initial_sidebar_state="collapsed")


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns([1,3], gap="small")
with col1:
    st.image(profile_pic)

st.markdown("""
    <style>
    .large-text {
        font-size: 4em; 
    }
    </style>
""", unsafe_allow_html=True)

with col2:
    st.markdown('<p class ="large-text">Manu Sharma</p>', unsafe_allow_html=True)
    st.write(DESCRIPTION)
    st.write(" ")


    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    

# --- EXPERIENCE & QUALIFICATIONS ---
    
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
st.write("02/2020 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
- ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | Chegg**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
