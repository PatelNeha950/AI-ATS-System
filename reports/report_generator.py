from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


def generate_report(best, feedback, questions):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>AI Resume Screening Report</b>", styles["Title"]))

    elements.append(Paragraph(f"Candidate: {best['name']}", styles["Normal"]))
    elements.append(Paragraph(f"Final ATS Score: {best['score']}%", styles["Normal"]))
    elements.append(Paragraph(f"Similarity: {best['similarity']}%", styles["Normal"]))
    elements.append(Paragraph(f"Recommendation: {feedback['decision']}", styles["Normal"]))

    elements.append(Paragraph("<br/><b>Matched Skills</b>", styles["Heading2"]))

    for skill in best["result"]["matched"]:
        elements.append(Paragraph(f"• {skill}", styles["Normal"]))

    elements.append(Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"]))

    for skill in best["result"]["missing"]:
        elements.append(Paragraph(f"• {skill}", styles["Normal"]))

    elements.append(Paragraph("<br/><b>Interview Questions</b>", styles["Heading2"]))

    for i, q in enumerate(questions, start=1):
        elements.append(Paragraph(f"{i}. {q}", styles["Normal"]))

    doc.build(elements)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf