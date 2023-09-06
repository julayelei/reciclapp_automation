import pandas as pd
# from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyPDF2
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Montserrat', 'Montserrat/static/Montserrat-Light.ttf'))

letter = (1080,1920)

# 1. Leer el archivo CSV
dataframe = pd.read_csv("archivo.csv")

# 2. Crear un PDF con el texto desde el CSV
def create_text_pdf(dataframe, output_filename):
    c = canvas.Canvas(output_filename, pagesize=letter)
    c.setFont("Montserrat", 35)
    width, height = letter

    for index, row in dataframe.iterrows():
        text = f"Nombre: {row['nombre']}, Dirección: {row['direccion']}, Teléfono: {row['telefono']}"
        c.drawString(110, 1390 - index*100, text)

    c.save()

create_text_pdf(dataframe, "temp_text.pdf")

# 3. Combinar el PDF "maqueta" con el PDF del texto
def overlay_pdfs(input_pdf, overlay_pdf, output_pdf):
    with open(input_pdf, "rb") as main_file, open(overlay_pdf, "rb") as overlay_file, open(output_pdf, "wb") as output_file:
        # Leer los PDFs
        main_pdf = PyPDF2.PdfFileReader(main_file)
        overlay_pdf = PyPDF2.PdfReader(overlay_file)

        # Crear un PDF de salida
        pdf_writer = PyPDF2.PdfFileWriter()

        # Asegurarse de que ambos PDFs tengan la misma cantidad de páginas
        num_pages = min(main_pdf.getNumPages(), overlay_pdf.getNumPages())

        for i in range(num_pages):
            # Combinar las páginas
            page = main_pdf.getPage(i)
            page.mergePage(overlay_pdf.getPage(i))
            pdf_writer.addPage(page)

        # Guardar el PDF combinado
        pdf_writer.write(output_file)

overlay_pdfs("maqueta.pdf", "temp_text.pdf", "resultado.pdf")

