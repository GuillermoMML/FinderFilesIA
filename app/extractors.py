import fitz
from odf.opendocument import load
from odf.text import P, H
from docx import Document

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    return "".join(page.get_text() for page in doc)

def extract_text_from_odt(path):
    odt = load(path)
    elements = odt.getElementsByType(P) + odt.getElementsByType(H)
    text = ""
    for element in elements:
        if element.firstChild:
            for child in element.childNodes:
                if hasattr(child, 'data'):
                    text += child.data + "\n"
    return text

def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join(para.text for para in doc.paragraphs)
