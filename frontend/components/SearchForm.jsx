import { useState } from "react";
import { searchDocuments } from "../api/search";

export default function SearchForm({ onResults }) {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;
    setLoading(true);
    const results = await searchDocuments(query);
    onResults(results);
    setLoading(false);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col sm:flex-row items-stretch gap-4 max-w-2xl w-full mx-auto my-8 bg-white rounded-xl shadow-lg p-6 border border-blue-100"
    >
      <input
        type="text"
        placeholder="Buscar documentos..."
        className="f  lex-1 border-2 border-blue-300 rounded-lg p-3 text-lg shadow focus:outline-none focus:border-blue-500 transition w-full"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button
        type="submit"
        className="w-full sm:w-auto px-6 py-3 bg-blue-600 text-white text-lg font-semibold rounded-lg shadow hover:bg-blue-700 transition"
      >
        {loading ? "Buscando..." : "Buscar"}
      </button>
    </form>
  );
}
