from docx import Document


def extract_text_from_docx(docx_file):
    """
    Extract text from DOCX.
    """

    document = Document(docx_file)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text