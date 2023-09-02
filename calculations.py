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


    # Remove borders and shading
    for row in table.rows:
        for cell in row.cells:
            # Set font size
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(12)
            
            # Set borders to invisible
            tcPr = cell._tc.get_or_add_tcPr()
            tcBorders = parse_xml(r'<w:tcBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:top w:val="nil"/><w:left w:val="nil"/><w:bottom w:val="nil"/><w:right w:val="nil"/></w:tcBorders>')
            tcPr.append(tcBorders)

            # Set shading to transparent
            cell_shading = parse_xml(r'<w:shd {} w:fill="FFFFFF" w:val="clear"/>'.format(nsdecls('w')))
            tcPr.append(cell_shading)
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
        "NIE: Y-9072864-E",
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
    dark_blue = RGBColor(0, 0, 139)  # Dark blue color

    # Formatting the header row
    for idx, header in enumerate(headers):
        hdr_cells[idx].text = header
        hdr_cells[idx].paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        shading_element = parse_xml(r'<w:shd {} w:fill="1F5C8B"/>'.format(nsdecls('w')))
        hdr_cells[idx]._tc.get_or_add_tcPr().append(shading_element)
        for run in hdr_cells[idx].paragraphs[0].runs:
            run.font.color.rgb = RGBColor(255, 255, 255)  # White font color

    # Setting all table borders to be dark blue
    for row in service_table.rows:
        for cell in row.cells:
            tcPr = cell._tc.get_or_add_tcPr()
            tcBorders = parse_xml(r'<w:tcBorders xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:top w:val="single"/><w:left w:val="single"/><w:bottom w:val="single"/><w:right w:val="single"/></w:tcBorders>')
            tcPr.append(tcBorders)
            for border in tcBorders:
                border.set(qn('w:color'), dark_blue.hexval[2:])

    for idx, service in enumerate(selected_services):
        cells = service_table.add_row().cells
        cells[0].text = str(idx + 1)
        cells[1].text = service["description"]
        cells[2].text = "1"
        cells[3].text = "€{:.2f}".format(service["cost"])
        cells[4].text = "€{:.2f}".format(service["cost"])

    # Total calculations
    iva = total_cost * 0.21
    final_total = total_cost + iva

    # Right-align the Total, IVA, and Total Final rows
    for text in [f"Total: €{total_cost:.2f}", f"IVA (21%): €{iva:.2f}", f"Total Final: €{final_total:.2f}"]:
        para = doc.add_paragraph(text)
        para.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

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
