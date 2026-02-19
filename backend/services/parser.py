from pypdf import PdfReader
import docx


def parse_pdf(path):

    reader = PdfReader(path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def parse_docx(path):

    doc = docx.Document(path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def parse_file(path):

    if path.endswith(".pdf"):
        return parse_pdf(path)

    elif path.endswith(".docx"):
        return parse_docx(path)

    return ""