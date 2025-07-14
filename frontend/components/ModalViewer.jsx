// src/components/ModalViewer.jsx
import { useEffect } from "react";

export default function ModalViewer({ filename, onClose }) {
  useEffect(() => {
    document.body.style.overflow = "hidden";
    return () => { document.body.style.overflow = ""; };
  }, []);

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-70 z-50 flex items-center justify-center"
      onClick={onClose}
    >
      <div
        className="relative bg-white rounded-lg w-[90vw] max-w-4xl h-[80vh] shadow-lg flex flex-col"
        onClick={e => e.stopPropagation()}
      >
        {/* Encabezado */}
        <div className="flex justify-between items-center p-4 border-b">
          <h2 className="text-lg font-semibold truncate">
            Previsualizando: {filename}
          </h2>
          <button
            className="text-gray-600 hover:text-red-500 text-2xl font-bold"
            onClick={onClose}
          >
            ✕
          </button>
        </div>
        {/* Contenido */}
        <div className="flex-grow overflow-hidden">
          <iframe
            src={`http://localhost:8000/preview/${filename}`}
            title="Documento"
            className="w-full h-full border-0"
          />
        </div>
      </div>
    </div>
  );
}
