import os
import subprocess

def convertir_a_pdf(input_path: str, output_folder: str = "temp_pdfs") -> str:
    os.makedirs(output_folder, exist_ok=True)
    output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + ".pdf")

    try:
        subprocess.run([
            "soffice", "--headless", "--convert-to", "pdf", "--outdir", output_folder, input_path
        ], check=True)
        return output_path if os.path.exists(output_path) else None
    except Exception as e:
        print(f"❌ Error al convertir a PDF: {e}")
        return None
