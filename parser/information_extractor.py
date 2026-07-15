import re
import spacy

nlp = spacy.load("en_core_web_sm")


SKILLS = [
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "HTML",
    "CSS",
    "React",
    "Node.js",
    "Express",
    "MongoDB",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "NLP",
    "Computer Vision",
    "TensorFlow",
    "PyTorch",
    "Keras",
    "Scikit-Learn",
    "Pandas",
    "NumPy",
    "Matplotlib",
    "Seaborn",
    "Flask",
    "Django",
    "FastAPI",
    "Docker",
    "Kubernetes",
    "Git",
    "GitHub",
    "Linux",
    "AWS",
    "Azure",
    "GCP",
    "Power BI",
    "Tableau",
    "Excel"
]

# -------------------------------
# Education Database
# -------------------------------

EDUCATION = [
    "B.E",
    "B.Tech",
    "BCA",
    "B.Sc",
    "M.E",
    "M.Tech",
    "MCA",
    "M.Sc",
    "Bachelor",
    "Master",
    "Computer Engineering",
    "Computer Science",
    "Information Technology",
    "Electronics",
    "Mechanical",
    "Civil"
]

# -------------------------------
# Extract Name
# -------------------------------

def extract_name(text):
    doc = nlp(text)

    for entity in doc.ents:
        if entity.label_ == "PERSON":
            return entity.text

    return "Not Found"


# -------------------------------
# Extract Email
# -------------------------------

def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -------------------------------
# Extract Phone
# -------------------------------

def extract_phone(text):
    pattern = r"(\+91[- ]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -------------------------------
# Extract GitHub
# -------------------------------

def extract_github(text):
    pattern = r"(https?://github\.com/\S+|github\.com/\S+)"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -------------------------------
# Extract LinkedIn
# -------------------------------

def extract_linkedin(text):
    pattern = r"(https?://(www\.)?linkedin\.com/in/\S+|linkedin\.com/in/\S+)"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


# -------------------------------
# Extract Skills
# -------------------------------

def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))


# -------------------------------
# Extract Education
# -------------------------------

def extract_education(text):
    found_education = []

    text = text.lower()

    for edu in EDUCATION:
        if edu.lower() in text:
            found_education.append(edu)

    return sorted(list(set(found_education)))


# -------------------------------
# Master Function
# -------------------------------

def extract_information(text):

    candidate = {

        "Name": extract_name(text),

        "Email": extract_email(text),

        "Phone": extract_phone(text),

        "GitHub": extract_github(text),

        "LinkedIn": extract_linkedin(text),

        "Education": extract_education(text),

        "Skills": extract_skills(text)

    }

    return candidate