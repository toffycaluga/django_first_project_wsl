# reports/views.py
from django.shortcuts import render
import markdown
import os

def informe_view(request):
    # Ruta del archivo .md (puedes moverlo a docs/ si quieres)
    md_path = os.path.join(os.path.dirname(__file__), "..", "informe_primer_proyecto.md")
    md_path = os.path.abspath(md_path)

    # Abrir el archivo y convertir a HTML
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    html_content = markdown.markdown(
        text,
        extensions=["fenced_code", "tables"]  # soporta bloques de código y tablas
    )

    return render(request, "reports/informe.html", {"content": html_content})
