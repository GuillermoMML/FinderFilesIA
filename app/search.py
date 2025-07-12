import os
import numpy as np
from app.extractors import extract_text_from_pdf, extract_text_from_odt, extract_text_from_docx
from app.utils import normalizar, expand_query_with_wordnet, load_keywords
from app.models import get_embedding_model
from sentence_transformers import util

def extract_text_from_docs(folder="data"):
    docs, filenames = [], []
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
        except:
            continue
    return docs, filenames

def buscar_documentos(query: str):
    docs, filenames = extract_text_from_docs()
    keywords = load_keywords()
    if not docs:
        return []

    model = get_embedding_model()
    query = normalizar(query)
    expanded_terms = expand_query_with_wordnet(query)
    query_embedding = model.encode(query, convert_to_tensor=True)
    doc_embeddings = model.encode(docs, convert_to_tensor=True)

    resultados = []
    for i, filename in enumerate(filenames):
        kw = keywords.get(filename, [])
        if isinstance(kw, str): kw = kw.split()
        kw = [normalizar(k) for k in kw]

        matches = len(set(kw) & expanded_terms)
        score_ia = float(util.cos_sim(query_embedding, doc_embeddings[i])[0])
        score_total = matches * 1.0 + score_ia * 0.8

        resultados.append({
            "filename": filename,
            "puntuacion_total": round(score_total, 4),
            "coincidencias_keywords": matches,
            "score_ia": round(score_ia, 4)
        })

    return sorted(resultados, key=lambda r: r["puntuacion_total"], reverse=True)
