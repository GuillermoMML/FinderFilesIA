import React from "react";

export default function Modal({ open, onClose, children, filename }) {
  if (!open) return null;
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-40">
      <div className="bg-white rounded-lg shadow-lg p-6 max-w-md w-full relative">
        <button
          onClick={onClose}
          className="absolute top-2 right-2 text-gray-500 hover:text-gray-700"
        >
          &times;
        </button>
        <iframe
          src={`http://localhost:8000/preview/${filename}`}
          title="Documento"
          className="w-full h-[70vh] border-0"
        />
      </div>
    </div>
  );
}