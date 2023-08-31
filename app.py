
import streamlit as st
from constants import COSTS_DESCRIPTIONS, COMMERCIAL_TERMS
from calculations import calculate_cost, generate_word_quote
from PIL import Image

# Set page config
st.set_page_config(layout="wide")

if "added_services" not in st.session_state:
    st.session_state.added_services = []

# Open the image using PIL
img = Image.open("logo.jpeg")

# Resize the image
base_width = img.width
new_height = 120
new_width = int((new_height / img.height) * base_width)
img_resized = img.resize((new_width, new_height))

# Using a container to center content
with st.container():
    # Logo Row
    col1, col2, col3 = st.columns([6,1,6])
    col2.image(img_resized, width=new_width)


# Title Row
spacer_left, title_col, spacer_right = st.columns([1,6,1])
title_col.title("Generador de Ofertas")

    
# Create spacer and main columns for the top row
spacer_col1, col1, col2, spacer_col2 = st.columns([1,3,3,1])

# Column 1: Customer Data
with col1:
    st.subheader("Datos del cliente")
    name = st.text_input("Nombre:")
    dni = st.text_input("DNI o NIE:")
    email = st.text_input("Email:")
    address = st.text_input("Dirección:")
    phone = st.text_input("Teléfono:")

# Dictionary to store user input for each service
user_inputs = {}

# Column 2: Each Service as an individual expander
with col2:
    st.subheader("Servicios disponibles")
    
    # Dropdown menu for services
    service_options = list(COSTS_DESCRIPTIONS.keys())
    selected_service = st.selectbox("Seleccione un servicio:", service_options)
    
    details = COSTS_DESCRIPTIONS[selected_service]
    user_inputs[f"{selected_service}_description"] = st.text_area("Descripción:", value=details['description'], height=160)

    
    # Unit Cost
    user_inputs[f"{selected_service}_cost"] = st.number_input(f"Costo para {selected_service}:", value=details['cost'])
    
    # Add to Quote Button
    if st.button(f"Agregar {selected_service} a la oferta"):
        service_data = {
            "name": selected_service,
            "description": user_inputs[f"{selected_service}_description"],
            "cost": user_inputs[f"{selected_service}_cost"]
        }
        st.session_state.added_services.append(service_data)
        
# Create spacer and main column for the bottom row
spacer_col3, col3, spacer_col4 = st.columns([1,6,1])

# Column 3: List of Services Added to Quote
# Column 3: List of Services Added to Quote
with col3:
    st.markdown("---")
    st.subheader("Servicios agregados a la oferta")
    for idx, service_data in enumerate(st.session_state.added_services):
        service_name = service_data['name']
        st.markdown(f"### {service_name}")
        st.write(f"Descripción: {service_data['description']}")
        st.write(f"Costo: €{service_data['cost']:.2f}")

        # Add a "Remove" button for each service
        if st.button(f"Eliminar {service_name}", key=f"remove_{idx}"):
            # If button is pressed, remove the service from the list
            st.session_state.added_services = [service for i, service in enumerate(st.session_state.added_services) if i != idx]
            st.experimental_rerun()  # Rerun the app to refresh the list


# Generate quote button
spacer_button, button_col, _, _ = st.columns([1,3,3,1])
with button_col:
    total_cost = calculate_cost(st.session_state.added_services)
    st.markdown(f"## Costo Total: **€{total_cost:.2f}**")
    
    
    
# Edit Commercial Terms
spacer_terms, terms_col, _ = st.columns([1,6,1])
with terms_col:
    st.markdown("---")
    st.subheader("Términos Comerciales")
    edited_terms = st.text_area("Editar términos comerciales:", value=COMMERCIAL_TERMS, height=150)
st.markdown("---")
# Create a row with two centered columns and spacers on the side
spacer_left, generate_col, download_col, spacer_right = st.columns([1, 3, 3, 1])

# "Generar Oferta" button in the left column
if generate_col.button("Generar Oferta", use_container_width=True):
    selected_services = st.session_state.added_services

    # Generate Word quote
    file_path = generate_word_quote(name, dni, email, address, phone, selected_services, total_cost)

    with open(file_path, "rb") as file:
        # "Descargar Oferta" button in the right column
        download_col.download_button(
            "Descargar Oferta",
            file,
            file_name=f"Oferta_{name.replace(' ', '_')}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True  # Make button span the entire column width
        )


# Using a container to center content
with st.container():
    # Logo Row
    colspc, collogo, col2spc= st.columns([6,1,6])
    collogo.image(img_resized, width=new_width)

