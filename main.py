from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import JSONResponse, FileResponse
from app.search import buscar_documentos
from app.extractors import extract_text_from_pdf, extract_text_from_odt, extract_text_from_docx
import os

app = FastAPI()
DATA_FOLDER = "data"

@app.post("/search")
async def search(query: str = Form(...)):
    return buscar_documentos(query)

@app.get("/preview/{filename}")
async def preview_document(filename: str):
    path = os.path.join(DATA_FOLDER, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(path)
    elif filename.endswith(".odt"):
        text = extract_text_from_odt(path)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(path)
    else:
        raise HTTPException(status_code=400, detail="Tipo de archivo no soportado")
    return {"preview": text[:500].replace("\n", " ")}

@app.get("/download/{filename}")
async def download_document(filename: str):
    path = os.path.join(DATA_FOLDER, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return FileResponse(path, filename=filename)
