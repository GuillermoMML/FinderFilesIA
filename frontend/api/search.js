export async function searchDocuments(query) {
  const formData = new FormData();
  formData.append("query", query);

  try {
    const response = await fetch("http://127.0.0.1:8000/search", {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("Error en la búsqueda");
    }

    return await response.json();
  } catch (error) {
    console.error("❌ Error al buscar documentos:", error);
    return [];
  }
}
