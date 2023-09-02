from docx import Document
from constants import COMMERCIAL_TERMS
from docx.shared import Pt, Cm  # Import the required utility functions
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT  # Import alignment utility
from docx.oxml.ns import qn
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.shared import RGBColor
from datetime import datetime

def calculate_cost(added_services):
    total_cost = 0
    for service_data in added_services:
        total_cost += service_data['cost']
    return total_cost

def add_bold_before_colon(doc, text, font_size=None):
    # Split the text at the colon
    parts = text.split(':', 1)
    if len(parts) == 2:
        # If there's a colon in the text
        para = doc.add_paragraph()
        
        run = para.add_run(parts[0] + ':')
        run.bold = True
        if font_size:
            run.font.size = Pt(font_size)
        
        run = para.add_run(' ' + parts[1].strip())  # Add the part after the colon
        if font_size:
            run.font.size = Pt(font_size)
    else:
        # If there's no colon, just add the text normally
        p = doc.add_paragraph(text)
        if font_size:
            for run in p.runs:
                run.font.size = Pt(font_size)

def generate_word_quote(name, dni, email, address, phone, selected_services, total_cost):
    doc = Document()
    
    # Create a table with 3 rows and 2 columns for the top section
    table = doc.add_table(rows=3, cols=2)
    table.style = 'Table Grid'

    # Set the cell background to transparent and remove borders
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(12)  # Set default font size
            
            # Remove shading (background color) from cells
            cell._element.get_or_add_tcPr().append(parse_xml(r'<w:shd {} w:fill="auto"/>'.format(nsdecls('w'))))
            
            # Remove cell borders
            tcPr = cell._element.get_or_add_tcPr()
            tcBorders = tcPr.get_or_add_tcBorders()
            for border in ['top', 'left', 'bottom', 'right']:
                element = tcBorders.find(qn('w:' + border))
                if element is not None:
                    element.set(qn('w:val'), 'none')
    
    # Populate the table cells as per given specification

    # Cell 1-a
    cell_1a = table.cell(0, 0)
    p = cell_1a.add_paragraph("Presupuesto")
    for run in p.runs:
        run.bold = True
        run.font.size = Pt(18)  # Make the font size larger

    # Cell 1-b
    cell_1b = table.cell(0, 1)
    logo_path = "logo.jpeg"  # Use the logo's filename since it's in the same directory
    
    # Directly use the default paragraph of the cell to add the image
    paragraph = cell_1b.paragraphs[0]
    r = paragraph.add_run()
    r.add_picture(logo_path, height=Pt(70))
    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT


    # Cell 2-a
    cell_2a = table.cell(1, 0)
    company_details = [
        "Sandra Badillo Fonseca",
        "NIE Y9072864-E",
        "Paseo de la Chopera, 51",
        "28045, Madrid",
        ""
    ]
    # Clear the default empty paragraph and use the first one for the first detail
    cell_2a.text = company_details[0]
    for detail in company_details[1:]:
        cell_2a.add_paragraph(detail)

    # Cell 2-b
    cell_2b = table.cell(1, 1)
    cell_2b.text = "Presupuesto N.: XXXX"

    # Cell 3-a
    cell_3a = table.cell(2, 0)
    client_details = [
        f"Nombre: {name}",
        f"DNI o NIE: {dni}",
        f"Dirección: {address}",
        f"Teléfono: {phone}"
    ]
    # Clear the default empty paragraph and use the first one for the first detail
    cell_3a.text = client_details[0]
    for detail in client_details[1:]:
        cell_3a.add_paragraph(detail)

    # Cell 3-b
    cell_3b = table.cell(2, 1)
    cell_3b.text = "Descripción del Proyecto: XXXX"

    # Spacer between the tables
    doc.add_paragraph()

    # Rest of the content remains the same

    # Table with services
    service_table = doc.add_table(rows=1, cols=5)
    hdr_cells = service_table.rows[0].cells
    headers = ["Item", "Descripción", "Cantidad", "Precio", "Total"]
    for idx, header in enumerate(headers):
        hdr_cells[idx].text = header
    
    for idx, service in enumerate(selected_services):
        cells = service_table.add_row().cells
        cells[0].text = str(idx + 1)
        cells[1].text = service["description"]
        cells[2].text = "1"
        cells[3].text = str(service["cost"])
        cells[4].text = str(service["cost"])

    # Total calculations
    iva = total_cost * 0.21
    final_total = total_cost + iva

    doc.add_paragraph(f"Total: €{total_cost}")
    doc.add_paragraph(f"IVA (21%): €{iva}")
    doc.add_paragraph(f"Total Final: €{final_total}")

    # Terms
    doc.add_paragraph("Términos y condiciones:")
    doc.add_paragraph("XXXX")  # Placeholder for actual terms

    # Footer
    footer = doc.sections[0].footer
    p = footer.paragraphs[0]
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    p.add_run("SB Reformas Madrid. Paseo de la Chopera, 51. 28045, Madrid. Página web: www.sbreformas-madrid.com - Instagram: @sbreformasmadrid")  # Footer text

    # Save the document
    file_path = f"quote_{name.replace(' ', '_')}.docx"
    doc.save(file_path)

    return file_path

