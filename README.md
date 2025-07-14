# 📁 FinderFilesIA

FinderFilesIA es una aplicación web inteligente para buscar, previsualizar y descargar documentos de texto (PDF, DOCX, ODT) utilizando inteligencia artificial y diseño moderno responsivo.

---

## 🚀 Tecnologías utilizadas

### 🧠 Backend (FastAPI)
- **FastAPI** + **Uvicorn** para la API REST.
- **SentenceTransformers** para búsqueda semántica.
- **NLTK WordNet** para expansión de sinónimos.
- **PyMuPDF**, **python-docx**, **odfpy** para extracción de texto.
- **LibreOffice CLI** para conversión de documentos a PDF.

### 💻 Frontend (React + Vite)
- **React** con hooks (`useState`, `useEffect`).
- **Vite** para desarrollo rápido.
- **Tailwind CSS** para estilos modernos y responsivos.
- **Flowbite** para componentes UI adicionales.

---

## 🔍 Funcionalidad principal

1. **Búsqueda inteligente**
   - El usuario introduce una consulta.
   - Se expande la búsqueda con sinónimos usando WordNet.
   - Se compara con keywords y vectores semánticos de los documentos.

2. **Resultados**
   - Lista de documentos más relevantes.
   - Muestra puntuación total, coincidencias de keywords y relevancia IA.

3. **Acciones**
   - ✅ Previsualizar: muestra el documento como PDF en una ventana modal o nueva pestaña.
   - ⬇️ Descargar: descarga directa del archivo.

---

## 📦 Instalación y ejecución

### Backend

```bash
# Instala dependencias
pip install -r requirements.txt

# Arranca el servidor FastAPI
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🖼️ Diseño

- Interfaz moderna y responsiva con Tailwind CSS.
- Buscador destacado y fácil de usar.
- Resultados en tarjetas con acciones rápidas.
- Modal para previsualización de documentos.

---

## 📄 Licencia

MIT

---
