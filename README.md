# 🤖 AI Resume Screening System

An AI-powered Applicant Tracking System (ATS) that automates resume screening, candidate ranking, recruiter feedback, and interview question generation. This project helps recruiters identify the most suitable candidates by comparing resumes with job descriptions using Natural Language Processing (NLP) and Machine Learning.

---

## 📌 Overview

The AI Resume Screening System streamlines the recruitment process by automatically extracting information from resumes, matching candidate skills with job requirements, calculating ATS scores, ranking multiple applicants, generating recruiter feedback, and creating downloadable PDF reports.

This project demonstrates the practical application of Artificial Intelligence in Human Resource Management and Recruitment.

---

# ✨ Features

### 🔐 Authentication

* Secure Recruiter Login
* Recruiter Registration
* Password Hashing using bcrypt
* Session Management
* Logout Functionality

### 📄 Resume Processing

* Upload PDF Resume
* Upload DOCX Resume
* Resume Parsing
* Resume Preview
* Resume Statistics

### 💼 Job Description Processing

* Upload TXT Job Description
* Upload PDF Job Description
* Upload DOCX Job Description

### 🧠 AI & NLP

* Candidate Information Extraction
* Skill Extraction
* ATS Similarity Score
* Skill Matching
* Final AI Candidate Score
* Intelligent Candidate Ranking

### 👨‍💼 Recruiter Dashboard

* Recruiter Analytics
* Interactive Score Gauge
* Candidate Metrics
* Matched Skills
* Missing Skills

### 🤖 AI Assistance

* AI Recruiter Feedback
* Hiring Recommendation
* AI Interview Question Generator

### 📑 Reports

* Generate Recruiter Report
* Download PDF Report

---

# 🛠 Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## Machine Learning

* Scikit-learn

## Natural Language Processing

* SpaCy

## Data Processing

* Pandas
* NumPy

## Resume Parsing

* pdfplumber
* python-docx

## Visualization

* Plotly

## PDF Generation

* ReportLab

## Database

* SQLite

## Security

* bcrypt

---

# 📂 Project Structure

```text
AI_Resume_Screening_System/
│
├── ai/
│   ├── similarity.py
│   ├── score.py
│   ├── ranking.py
│   ├── recommendation.py
│   └── recruiter.py
│
├── auth/
│   ├── auth.py
│   ├── database.py
│   ├── login.py
│   └── signup.py
│
├── dashboard/
│   ├── charts.py
│   └── metrics.py
│
├── parser/
│   ├── parser.py
│   ├── pdf_parser.py
│   ├── docx_parser.py
│   ├── job_parser.py
│   └── information_extractor.py
│
├── reports/
│   └── report_generator.py
│
├── database/
│   └── users.db
│
├── app.py
├── style.css
├── requirements.txt
├── packages.txt
└── README.md
```

---

# 🚀 Installation


Install dependencies

```bash
pip install -r requirements.txt
```

Download the SpaCy model

```bash
python -m spacy download en_core_web_sm
```

Run the application

```bash
streamlit run app.py
```

---

# 📊 Workflow

1. Recruiter Login
2. Upload Job Description
3. Upload One or More Candidate Resumes
4. Resume Parsing
5. Candidate Information Extraction
6. Skill Extraction
7. ATS Similarity Calculation
8. Skill Matching
9. AI Candidate Ranking
10. Recruiter Feedback Generation
11. Interview Question Generation
12. Download PDF Screening Report

---

# 📈 Future Enhancements

* Email OTP Authentication
* Google Login
* Recruiter Dashboard Analytics
* Candidate Database
* Resume History
* AI Resume Improvement Suggestions
* Resume Keyword Optimization
* Cloud Database Integration
* Docker Deployment
* Multi-language Resume Parsing

---


# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

* Python Programming
* Natural Language Processing
* Machine Learning
* Information Extraction
* Resume Parsing
* Applicant Tracking Systems
* Data Visualization
* Authentication
* Streamlit Development


**Neha Patel**

AI & Machine Learning Enthusiast


⭐ If you found this project helpful, consider giving it a star on GitHub!
