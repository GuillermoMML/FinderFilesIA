from finder import buscar_documentos
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Form

app = FastAPI()  

@app.post("/search")
async def search(query: str = Form(...)):
    resultados = buscar_documentos(query)
    return JSONResponse(content=resultados)
