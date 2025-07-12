import json
import os
import fitz  # PyMuPDF
from odf.opendocument import load
from odf.text import P, H
import unicodedata  # Normalizar la busqueda no tildes ni mayusculas
from docx import Document

from sentence_transformers import SentenceTransformer, util
from nltk.corpus import wordnet as wn
import numpy as np


model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

# ======== Funciones de extracción =======

def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto


def expand_query_with_wordnet(query):
    synonyms = set()
    terms = normalizar(query).split()  # Normaliza y separa por palabra

    for word in terms:
        for syn in wn.synsets(word, lang='spa'):  # usa 'eng' si es en inglés
            for lemma in syn.lemmas(lang='spa'):
                name = lemma.name().replace('_', ' ')
                synonyms.add(name.lower())
       
    return set(terms).union(synonyms)

def load_keywords(path="metadata/keywords.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ No se pudieron cargar las palabras clave: {e}")
        return {}
    
def extract_text_from_docx(path):
    text = ""
    doc = Document(path)
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


def extract_text_from_pdf(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_odt(path):
    text = ""
    odt = load(path)
    all_elements = odt.getElementsByType(P) + odt.getElementsByType(H)

    for element in all_elements:
        if element.firstChild and hasattr(element.firstChild, 'data'):
            text += str(element.firstChild.data) + "\n"
        elif element.firstChild:
            # Si no tiene .data pero tiene hijos, los recorremos
            for child in element.childNodes:
                if hasattr(child, 'data'):
                    text += str(child.data) + "\n"

    return text


def extract_text_from_docs(folder):
    docs = []
    filenames = []
    keywords = load_keywords()

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        try:
            if file.endswith(".pdf"):
                text = extract_text_from_pdf(path)
            elif file.endswith(".odt"):
                text = extract_text_from_odt(path)
            elif file.endswith(".docx"):
                text = extract_text_from_docx(path)
            else:
                continue
            docs.append(text)
            filenames.append(file)
        except Exception as e:
            print(f"⚠️ Error al procesar '{file}': {e}")
            continue

    return docs, filenames


# ======== Función principal de búsqueda ======= 
def buscar_documentos(query: str):
    folder = "data"
    keywords = load_keywords()
    docs, filenames = extract_text_from_docs(folder)

    if not docs:
        return []

    query = normalizar(query.strip())
    total_query_terms = expand_query_with_wordnet(query)
    query_embedding = model.encode(query, convert_to_tensor=True)
    doc_embeddings = model.encode(docs, convert_to_tensor=True)

    resultados = []

    for i, filename in enumerate(filenames):
        kw = keywords.get(filename, [])
        if isinstance(kw, str):
            kw = [normalizar(k) for k in kw.split()]
        elif isinstance(kw, list):
            kw = [normalizar(k) for k in kw]
        else:
            kw = []

        coincidencias = len(set(kw) & total_query_terms)
        score_ia = float(util.cos_sim(query_embedding, doc_embeddings[i])[0])
        puntuacion_total = coincidencias * 1.0 + score_ia * 0.8

        resultados.append({
            "filename": filename,
            "puntuacion_total": round(puntuacion_total, 4),
            "coincidencias_keywords": coincidencias,
            "score_ia": round(score_ia, 4)
        })

    resultados.sort(key=lambda r: r["puntuacion_total"], reverse=True)
    return resultados[:5]


    
