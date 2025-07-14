import subprocess
from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import JSONResponse, FileResponse
from app.convert import convertir_a_pdf
from app.search import buscar_documentos
from fastapi.middleware.cors import CORSMiddleware
from app.extractors import extract_text_from_pdf, extract_text_from_odt, extract_text_from_docx
import os

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # O usa ["*"] para desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FOLDER = "data"

@app.post("/search")
async def search(query: str = Form(...)):
    return buscar_documentos(query)


DATA_FOLDER = "data"
PREVIEW_FOLDER = "previews"

@app.get("/preview/{filename}")
async def preview_document(filename: str):
    path = os.path.join(DATA_FOLDER, filename)

    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")

    # Si ya es PDF, devolver directamente con tipo correcto
    if filename.lower().endswith(".pdf"):
        return FileResponse(
            path,
            media_type="application/pdf",
            filename=filename,
            headers={"Content-Disposition": "inline"}
        )

    # Convertir otros formatos a PDF
    os.makedirs(PREVIEW_FOLDER, exist_ok=True)
    try:
        subprocess.run([
            "soffice",
            "--headless",
            "--convert-to", "pdf",
            "--outdir", PREVIEW_FOLDER,
            path
        ], check=True)
    except subprocess.CalledProcessError:
        raise HTTPException(status_code=500, detail="Error al convertir archivo")

    pdf_filename = os.path.splitext(filename)[0] + ".pdf"
    pdf_path = os.path.join(PREVIEW_FOLDER, pdf_filename)

    if not os.path.exists(pdf_path):
        raise HTTPException(status_code=500, detail="No se generó el PDF correctamente")

    # 🔥 Clave: usar Content-Disposition: inline para que no se descargue
    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename=pdf_filename,
        headers={"Content-Disposition": "inline"}
    )



@app.get("/download/{filename}")
async def download_document(filename: str):
    path = os.path.join(DATA_FOLDER, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return FileResponse(path, filename=filename)

