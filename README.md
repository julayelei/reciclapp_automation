# Script de Certificación Reciclapp
El script tiene como objetivo generar certificados PDF para cada cliente basado en la data de reciclaje contenida en un archivo CSV. Estos certificados son sobre la cantidad y tipo de residuos reciclados por el cliente durante un mes específico.

Bibliotecas Importadas:
pandas: Usada para manipular y analizar la data estructurada.
reportlab: Biblioteca para generar PDFs.
PyPDF2: Usada para manipular archivos PDF existentes.
os: Proporciona funciones para interactuar con el sistema operativo, principalmente para operaciones relacionadas con el sistema de archivos.
yaml: Usada para leer archivos de configuración en formato YAML.
PIL (Pillow): Usada para operaciones de imágenes.
Funcionalidades Principales:
Configuración de Fuentes:
Se registran dos fuentes (Montserrat regular y Montserrat negrita) desde archivos TTF para ser utilizadas en la generación del PDF.

Lectura y Agrupación de Datos:
Se lee un archivo CSV y se agrupan los datos según RUT, Comuna, Mes, Nombre del cliente, Dirección y Tipo de residuo. Luego, se suma el peso de los residuos para cada grupo.

Funciones Auxiliares:

get_image_with_transparency(): Esta función se encarga de procesar imágenes para asegurarse de que si es un PNG, tenga transparencia.

read_configuration(): Lee un archivo de configuración en formato YAML.

draw_text(): Una función robusta para escribir texto en el PDF. Esta función es capaz de manejar textos largos, rompiéndolos en múltiples líneas si es necesario y también de resaltar ciertas frases en negrita.

insert_residue_icons(): Inserta íconos (imágenes) relacionados con el tipo de residuo reciclado en el PDF. Junto a cada ícono, se muestra el tipo de residuo y su peso.

create_text_pdf_conestilo(): Función principal que genera el PDF con toda la información relevante.

overlay_pdfs(): Función para superponer un PDF (contenido generado) sobre otro PDF (una plantilla preexistente) y guardar el resultado.

Generación de PDFs:
Finalmente, se generan certificados en formato PDF para cada cliente basado en sus datos de reciclaje. Cada certificado se superpone a una plantilla preexistente y se guarda en un directorio específico.
