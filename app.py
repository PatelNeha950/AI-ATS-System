import streamlit as st
import os
from auth.database import create_table
from auth.database import *
from ai.recruiter import (
    generate_feedback,
    generate_questions
)
from reports.report_generator import generate_report
from auth.login import login_page
from auth.signup import signup_page
from parser.parser import parse_resume
from parser.job_parser import parse_job_description
from parser.information_extractor import (
    extract_information,
    extract_skills
)

from ai.similarity import calculate_similarity
from ai.score import skill_match, calculate_score
from ai.recommendation import recommend
from ai.ranking import rank_candidates

from dashboard.charts import circular_score
from dashboard.metrics import show_candidate


# =====================================================
# Page Configuration
# =====================================================
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🤖",
    layout="wide"
)
def load_css():

    with open("style.css") as f:

        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()
# =====================================================
# Database Initialization
# =====================================================

create_table()
# =====================================================
# Session State
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

# Hide sidebar before login
if not st.session_state.logged_in:
    st.markdown("""
    <style>
    section[data-testid="stSidebar"]{
        display:none;
    }
    </style>
    """, unsafe_allow_html=True)

# =====================================================
# Authentication
# =====================================================

if not st.session_state.logged_in:

    auth = st.segmented_control(
        "",
        ["Login", "Sign Up"],
        default="Login",
        key="auth_selector"
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if auth == "Login":
        login_page()
    else:
        signup_page()

    st.stop()
# =====================================================
# Title
# =====================================================

st.title(
    "🤖 AI Resume Screening System"
)


# =====================================================
# Sidebar
# =====================================================

st.sidebar.title("Navigation")

st.sidebar.success(
    f"👋 Welcome {st.session_state.user['name']}"
)

if st.sidebar.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.session_state.user = None

    st.rerun()


page = st.sidebar.radio(
    "Choose Page",
    [
        "Home",
        "About"
    ]
)



# =====================================================
# HOME PAGE
# =====================================================

if page == "Home":


    st.header(
        "📂 Upload Multiple Resumes & Job Description"
    )


    resumes = st.file_uploader(

        "Upload Candidate Resumes",

        type=[
            "pdf",
            "docx"
        ],

        accept_multiple_files=True
    )


    job = st.file_uploader(

        "Upload Job Description",

        type=[
            "txt",
            "pdf",
            "docx"
        ]
    )


    candidates = []


    job_text = None

    job_skills = []



    # =====================================================
    # Job Processing
    # =====================================================


    if job is not None:


        os.makedirs(
            "jobs",
            exist_ok=True
        )


        with open(

            os.path.join(
                "jobs",
                job.name
            ),

            "wb"

        ) as f:

            f.write(
                job.getbuffer()
            )


        st.success(
            "✅ Job Description Uploaded Successfully"
        )


        job_text = parse_job_description(
            job
        )


        job_skills = extract_skills(
            job_text
        )



    # =====================================================
    # Resume Processing
    # =====================================================


    if resumes:


        os.makedirs(
            "resumes",
            exist_ok=True
        )


        for resume in resumes:


            with open(

                os.path.join(
                    "resumes",
                    resume.name
                ),

                "wb"

            ) as f:

                f.write(
                    resume.getbuffer()
                )


            resume_text = parse_resume(
                resume
            )


            candidate = extract_information(
                resume_text
            )


            score = 0

            similarity = 0


            result = {

                "percentage":0,

                "matched":[],

                "missing":[]

            }



            if job_text:


                similarity = calculate_similarity(

                    resume_text,

                    job_text

                )


                result = skill_match(

                    candidate["Skills"],

                    job_skills

                )


                score = calculate_score(

                    similarity,

                    result["percentage"]

                )



            candidates.append({

                "name":resume.name,

                "text":resume_text,

                "candidate":candidate,

                "similarity":similarity,

                "result":result,

                "score":score

            })



        st.success(

            f"✅ {len(candidates)} Resume(s) Processed"

        )
    # =====================================================
    # Candidate Ranking Dashboard
    # =====================================================


    if candidates and job_text:


        ranked_candidates = rank_candidates(
            candidates
        )


        st.divider()


        st.header(
            "🏆 Candidate Ranking"
        )


        for index, candidate in enumerate(
            ranked_candidates
        ):


            with st.container():


                st.subheader(
                    f"#{index+1} {candidate['name']}"
                )


                col1, col2, col3 = st.columns(3)


                col1.metric(

                    "AI Score",

                    f"{candidate['score']}%"

                )


                col2.metric(

                    "Similarity",

                    f"{candidate['similarity']}%"

                )


                col3.metric(

                    "Recommendation",

                    recommend(
                        candidate["score"]
                    )

                )


        st.divider()



        # =====================================================
        # Best Candidate Analysis
        # =====================================================


        best = ranked_candidates[0]


        st.header(
            "🥇 Best Candidate Analysis"
        )


        show_candidate(
            best["candidate"]
        )


        st.subheader(
            "🛠 Extracted Skills"
        )


        cols = st.columns(3)


        for i, skill in enumerate(

            best["candidate"]["Skills"]

        ):

            cols[
                i % 3
            ].success(skill)



        # =====================================================
        # Score Gauge
        # =====================================================


        fig = circular_score(

            best["score"]

        )


        st.plotly_chart(

            fig,

            use_container_width=True

        )



        # =====================================================
        # Metrics
        # =====================================================


        col1, col2 = st.columns(2)



        with col1:


            st.metric(

                "Similarity",

                f"{best['similarity']}%"

            )


            st.metric(

                "Skill Match",

                f"{best['result']['percentage']}%"

            )



        with col2:


            st.metric(

                "Final ATS Score",

                f"{best['score']}%"

            )


            st.metric(

                "Recommendation",

                recommend(
                    best["score"]
                )

            )



        # =====================================================
        # Skill Comparison
        # =====================================================


        left, right = st.columns(2)



        with left:


            st.subheader(
                "✅ Matched Skills"
            )


            if best["result"]["matched"]:


                for skill in best["result"]["matched"]:

                    st.success(skill)


            else:

                st.info(
                    "No matched skills found"
                )



        with right:


            st.subheader(
                "❌ Missing Skills"
            )


            if best["result"]["missing"]:


                for skill in best["result"]["missing"]:

                    st.error(skill)


            else:

                st.success(
                    "No missing skills"
                )



        # =====================================================
        # MODULE 7
        # AI Recruiter Feedback
        # =====================================================


        feedback = generate_feedback(

            best["candidate"],

            best["result"]["matched"],

            best["result"]["missing"],

            best["score"]

        )


        st.divider()


        st.header(
            "🤖 AI Recruiter Feedback"
        )


        st.success(
            feedback["decision"]
        )


        st.write(
            feedback["message"]
        )



        col1, col2 = st.columns(2)



        with col1:


            st.subheader(
                "💪 Candidate Strengths"
            )


            for skill in feedback["strengths"]:

                st.success(skill)



        with col2:


            st.subheader(
                "📉 Improvement Areas"
            )


            for skill in feedback["weakness"]:

                st.error(skill)

        # =====================================================
        # Interview Question Generator
        # =====================================================


                # =====================================================
        # Interview Question Generator
        # =====================================================

        st.divider()

        st.header("🎯 AI Interview Question Generator")

        questions = generate_questions(
            best["candidate"]["Skills"]
        )

        for i, question in enumerate(questions):
            st.write(f"**{i+1}.** {question}")

        # =====================================================
        # PDF Report Generator
        # =====================================================

        st.divider()

        st.header("📄 AI Resume Screening Report")

        if st.button("📄 Generate PDF Report"):

            pdf_bytes = generate_report(
                best,
                feedback,
                questions
            )

            st.success("✅ PDF Generated Successfully!")

            st.download_button(
                label="⬇ Download AI Resume Report",
                data=pdf_bytes,
                file_name=f"{best['name']}_AI_Report.pdf",
                mime="application/pdf"
            )
# =====================================================
# ABOUT PAGE
# =====================================================


elif page == "About":


    st.header(
        "🤖 About AI Resume Screening System"
    )


    st.write(
"""
This project uses Artificial Intelligence to screen resumes and rank candidates based on job requirements.

## Completed Features

✅ Multiple Resume Upload

✅ PDF/DOCX Resume Parsing

✅ NLP Information Extraction

✅ Skill Extraction

✅ AI Semantic Similarity

✅ Skill Matching

✅ ATS Score Calculation

✅ Candidate Ranking

✅ AI Recruiter Feedback

✅ Interview Question Generator


## Upcoming Features

🚀 Resume PDF Report Generator

🚀 Candidate Database

🚀 Authentication System

🚀 Cloud Deployment

🚀 Advanced AI Interview Analysis

"""
)