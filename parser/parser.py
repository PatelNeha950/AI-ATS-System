from parser.pdf_parser import extract_text_from_pdf
from parser.docx_parser import extract_text_from_docx


def parse_resume(uploaded_file):

    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):

        return extract_text_from_pdf(uploaded_file)

    elif filename.endswith(".docx"):

        return extract_text_from_docx(uploaded_file)

    else:

        return "Unsupported File Format"