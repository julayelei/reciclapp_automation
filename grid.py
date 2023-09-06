from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyPDF2

# 1. Crear un PDF con la cuadrícula
def create_grid_pdf(output_file):
    c = canvas.Canvas(output_file, pagesize=(1080,1920))
    width, height = (1080,1920)

    # Dibuja una cuadrícula
    for i in range(0, int(width), 10):  # Ajusta el '10' si necesitas una cuadrícula más densa
        # c.drawRightString(i, 0, str(i))
        if i % 25 == 0:
            c.drawRightString(i, 0, str(i))
        c.line(i, 0, i, height)

    for j in range(0, int(height), 10):  # Ajusta el '10' si necesitas una cuadrícula más densa
        c.drawString(0, j, str(j))
        c.line(0, j, width, j)

    c.save()

# 2. Combinar la cuadrícula con el PDF maqueta
def overlay_pdfs(input_pdf, overlay_pdf, output_pdf):
    with open(input_pdf, "rb") as main_file, open(overlay_pdf, "rb") as overlay_file, open(output_pdf, "wb") as output_file:
        main_pdf = PyPDF2.PdfFileReader(main_file)
        overlay_pdf = PyPDF2.PdfFileReader(overlay_file)
        pdf_writer = PyPDF2.PdfFileWriter()

        # Asegurarse de que ambos PDFs tengan la misma cantidad de páginas
        num_pages = min(len(main_pdf.pages), len(overlay_pdf.pages))

        for i in range(num_pages):
            page = main_pdf.pages[i]
            page.mergePage(overlay_pdf.pages[i])
            pdf_writer.addPage(page)

        pdf_writer.write(output_file)

# Crear el PDF de la cuadrícula
create_grid_pdf("grid.pdf")

# Combinar la cuadrícula con el PDF maqueta
overlay_pdfs("certificado_ejemplo.pdf", "grid.pdf", "maqueta_with_grid.pdf")

