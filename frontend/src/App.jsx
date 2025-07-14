import { useState, useEffect } from "react";
import SearchForm from "../components/SearchForm";
import ModalViewer from "../components/ModalViewer";

function App() {
  const [results, setResults] = useState([]);
  const [previewFile, setPreviewFile] = useState(null);

  useEffect(() => {
    document.body.classList.toggle("overflow-hidden", !!previewFile);
    return () => document.body.classList.remove("overflow-hidden");
  }, [previewFile]);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-blue-300">
      <header className="bg-white shadow py-6 mb-8">
        <h1 className="text-4xl font-extrabold text-center text-blue-700 tracking-tight">
          FinderFilesIA
        </h1>
        <p className="text-center text-gray-500 mt-2">
          Encuentra y previsualiza tus documentos fácilmente
        </p>
      </header>
      <main className="max-w-4xl mx-auto px-4">
        <SearchForm onResults={setResults} />

        {results.length > 0 && (
          <div className="mt-10">
            <h2 className="text-2xl font-semibold mb-6 text-blue-800">
              Resultados:
            </h2>
            <ul className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {results.map((doc, idx) => (
                <li
                  key={idx}
                  className="bg-white border border-blue-100 rounded-xl shadow-lg p-6 flex flex-col gap-2 hover:shadow-xl transition"
                >
                  <p className="font-bold text-blue-700 text-lg flex items-center gap-2">
                    <span role="img" aria-label="document">
                      📄
                    </span>{" "}
                    {doc.filename}
                  </p>
                  <div className="flex flex-wrap gap-4 text-sm text-gray-600">
                    <span>
                      🔢 <b>Puntuación:</b> {doc.puntuacion_total}
                    </span>
                    <span>
                      💡 <b>Keywords:</b> {doc.coincidencias_keywords}
                    </span>
                    <span>
                      🧠 <b>IA:</b> {doc.score_ia}
                    </span>
                  </div>
                  <div className="mt-4 flex gap-4">
                    <button
                      className="px-4 py-2 bg-gray-200 text-blue-700 rounded-lg shadow hover:bg-gray-300 transition"
                      onClick={() => window.open(`http://localhost:8000/preview/${doc.filename}`, "_blank")}
                    >
                      Previsualizar
                    </button>
                    <a
                      href={`http://localhost:8000/download/${doc.filename}`}
                      className="px-4 py-2 bg-gray-200 text-blue-700 rounded-lg shadow hover:bg-gray-300 transition"
                      target="_blank"
                      rel="noreferrer"
                    >
                      Descargar
                    </a>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
