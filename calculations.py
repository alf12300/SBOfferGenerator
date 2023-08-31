from docx import Document
from constants import COMMERCIAL_TERMS
from docx.shared import Pt  # Import the required utility functions
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT  # Import alignment utility
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
    
    # Add logo to the top of the document
    logo_path = "logo.jpeg"  # Use the logo's filename since it's in the same directory
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT  # Right align the paragraph
    
    # Add the picture to the centered paragraph and set the height to 40px
    r = paragraph.add_run()
    r.add_picture(logo_path, height=Pt(60))
 
    doc.add_heading('SB REFORMAS - Presupuesto', 0)
    
    current_date = datetime.now().strftime("%d/%m/%Y")
    add_bold_before_colon(doc, f"Fecha: {current_date}")
    add_bold_before_colon(doc, f"Nombre: {name}")
    add_bold_before_colon(doc, f"DNI o NIE: {dni}")
    add_bold_before_colon(doc, f"Email: {email}")
    add_bold_before_colon(doc, f"Dirección: {address}")
    add_bold_before_colon(doc, f"Teléfono: {phone}")
    for index, service_data in enumerate(selected_services, start=1):
        service_name = service_data['name']
        
        # Service name and cost remain left-aligned
        add_bold_before_colon(doc, f"Servicio {index} - {service_name}:", font_size=12)

        # Justify-align the description
        p_desc = doc.add_paragraph(f"Descripción: {service_data['description']}")
        p_desc.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        doc.add_paragraph(f"Costo: €{service_data['cost']:.2f}")

    add_bold_before_colon(doc, f"Total: €{total_cost:.2f}", font_size=12)    
    doc.add_paragraph()
    
    terms = COMMERCIAL_TERMS.split("\n")
    for line in terms:
        if line.endswith(':'):
            para = doc.add_paragraph(line)
            for run in para.runs:
                run.bold = True
        else:
            doc.add_paragraph(line)
    
    # Add logo to the bottom of the document
    doc.add_paragraph()
    doc.add_paragraph()
    paragraph2 = doc.add_paragraph()
    paragraph2.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER  # Center align the paragraph
    
    # Add the picture to the centered paragraph and set the height to 40px
    r2 = paragraph2.add_run()
    r2.add_picture(logo_path, height=Pt(60))
    
    file_path = f"quote_{name.replace(' ', '_')}.docx"
    doc.save(file_path)
    
    return file_path