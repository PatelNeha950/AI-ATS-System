import pdfplumber
from docx import Document


def parse_job_description(file):

    if file is None:
        return ""

    filename = file.name.lower()

    text = ""

    if filename.endswith(".txt"):
        text = file.read().decode("utf-8")

    elif filename.endswith(".pdf"):

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    elif filename.endswith(".docx"):

        document = Document(file)

        for para in document.paragraphs:
            text += para.text + "\n"

    return text