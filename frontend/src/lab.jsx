import React, { useState } from "react";
import ModalViewer from "../components/ModalViewer";

export default function Lab() {
  const [viewerOpen, setViewerOpen] = useState(false);
  const [selectedFile, setSelectedFile] = useState(null);

  // Ejemplo: usa un archivo PDF fijo de /data
  const examplePdf = "H:\Proyectos personales 2025\FinderFilesIA\data\evaluacion_final_tic.pdf"; // Cambia esto por el nombre real de tu archivo PDF en /data

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-100 to-blue-300 flex flex-col items-center py-16">
      <h1 className="text-3xl font-bold text-blue-700 mb-6">
        Laboratorio FinderFilesIA
      </h1>
      <p className="max-w-xl text-gray-700 mb-8 text-center">
        Haz clic en el botón para abrir una ventana modal que previsualiza un PDF
        desde la carpeta <code>/data</code>.
      </p>
      <div className="grid grid-cols-2 gap-8 mb-12">
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-lg font-semibold mb-2">Sección 1</h2>
          <p className="text-gray-600">
            Contenido de la sección 1. Puedes agregar cualquier información aquí.
          </p>
        </div>
        <div className="bg-white rounded-lg shadow p-6">
          <h2 className="text-lg font-semibold mb-2">Sección 2</h2>
          <p className="text-gray-600">
            Contenido de la sección 2. Más texto para mostrar el efecto del
            modal.
          </p>
        </div>
      </div>
      <button
        className="px-6 py-2 bg-blue-600 text-white rounded shadow hover:bg-blue-700"
        onClick={() => {
          setSelectedFile(examplePdf);
          setViewerOpen(true);
        }}
      >
        Previsualizar PDF
      </button>
      {viewerOpen && (
        <ModalViewer
          filename={selectedFile}
          onClose={() => setViewerOpen(false)}
        />
      )}
    </div>
  );
}