import streamlit as st
import pandas as pd
from constants import COSTS_DESCRIPTIONS, COMMERCIAL_TERMS
from constants import TOOLS_MAPPING
from calculations import calculate_cost, generate_word_quote
from PIL import Image

# Set page config
st.set_page_config(layout="wide")

# Side Panel Tab Selection
tab_selection = st.sidebar.radio("Choose a Tab", ["Generador de Propuestas", "Estimador de Costos"])

if tab_selection == "Generador de Propuestas":
    if "added_services" not in st.session_state:
        st.session_state.added_services = []

    # Open the image using PIL
    img = Image.open("logo.jpeg")
    
    clients_df = pd.read_excel("CLIENTS.xlsx")
      
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
    st.title("Generador de Ofertas")
    # Create spacer and main columns for the top row
    col1, col2= st.columns([6,6])
    
    # Column 1: Customer Data
    with col1:
        st.subheader("Datos del cliente")
        client_names = clients_df["NOMBRE"].tolist()
        selected_client = st.selectbox("Seleccione o genere un nuevo cliente:", [""] + client_names)
        
        if selected_client:
            client_data = clients_df[clients_df["NOMBRE"] == selected_client].iloc[0]
            name = st.text_input("Nombre:", value=client_data["NOMBRE"])
            dni = st.text_input("DNI o NIE:", value=client_data["NIF/CIF"])
            email = st.text_input("Email:", value=client_data["EMAIL"])
            address = st.text_input("Dirección:", value=client_data["DIRECCION"])
            phone = st.text_input("Teléfono:", value=str(client_data["TELEFONO"]))
        else:
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
        user_inputs[f"{selected_service}_description"] = st.text_area("Descripción:", value=details['description'], height=170)
    
        
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
    total_cost = calculate_cost(st.session_state.added_services)
    st.markdown(f"## Costo Total: **€{total_cost:.2f}**")
            
    # Edit Commercial Terms

    st.markdown("---")
    st.subheader("Términos Comerciales")
    edited_terms = st.text_area("Editar términos comerciales:", value=COMMERCIAL_TERMS, height=150)
    st.markdown("---")
    # Create a row with two centered columns and spacers on the side
    generate_col, download_col = st.columns([6,6])
    
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
    
    
elif tab_selection == "Estimador de Costos":
    if "added_costs" not in st.session_state:
        st.session_state.added_costs = []
    
    title_col = st.title("Estimador de Costos")
    if "total_estimated_costs" not in st.session_state:
        st.session_state.total_estimated_costs = 0
    
    # Dropdown for service selection
    selected_service = st.selectbox("Seleccione un servicio:", list(COSTS_DESCRIPTIONS.keys()))

    # Retrieve tools for the selected service
    tools_for_service = TOOLS_MAPPING.get(selected_service, [])

    # Dictionary to store user inputs for each tool
    tool_inputs = {}
    
    for tool in tools_for_service:
        col_name, col_unit_price, col_quantity, col_total = st.columns([2, 2, 2, 2])
            
        with col_name:
            st.text("")
            st.write(f"{tool}")
        
        with col_unit_price:
            unit_price = st.number_input("Precio unitario (€)", min_value=0.0, value=0.0, step=0.01, key=f"unit_{tool}")
        
        with col_quantity:
            quantity = st.number_input("Cantidad", min_value=0, value=0, step=1, key=f"qty_{tool}")
        
        total_for_item = unit_price * quantity
        with col_total:
            st.text("Costo Total")
            st.write(f"€{total_for_item:.2f}")
            
        tool_inputs[tool] = {"quantity": quantity, "unit_price": unit_price}
    # Before the button condition, initialize the variable
    custom_tool_name = ""
    # Add Custom Tool button
    if st.button("Agregar Herramienta Personalizada"):
        # If clicked, show input fields for custom tool
        col_name, col_unit_price, col_quantity, col_total = st.columns([2, 2, 2, 2])
            
        with col_name:
        custom_tool_name = st.text_input("Nombre de la herramienta")
        
        with col_unit_price:
            custom_tool_unit_price = st.number_input("Precio unitario (€)", min_value=0.0, value=0.0, step=0.01, key="unit_custom_tool")
        
        with col_quantity:
            custom_tool_quantity = st.number_input("Cantidad", min_value=0, value=0, step=1, key="qty_custom_tool")
    
        custom_tool_total = custom_tool_unit_price * custom_tool_quantity
        with col_total:
            st.text("Costo Total")
            st.write(f"€{custom_tool_total:.2f}")

    # Only add the custom tool if a name is provided
    if custom_tool_name:
        tool_inputs[custom_tool_name] = {"quantity": custom_tool_quantity, "unit_price": custom_tool_unit_price}

    tool_inputs[custom_tool_name] = {"quantity": custom_tool_quantity, "unit_price": custom_tool_unit_price}


    
    # Dictionary to store calculated costs for each tool
    tool_costs = {}
    for tool, inputs in tool_inputs.items():
        cost = inputs["quantity"] * inputs["unit_price"]
        tool_costs[tool] = cost
    
    # Calculating the total sum for all tools (including custom tool)
    total_cost_tools = sum(tool_costs.values())
    st.markdown(f"### Costo Total: **€{total_cost_tools:.2f}**")


    # For services
    if st.button("Agregar al total"):
        st.session_state.total_estimated_costs += sum(tool_costs.values())
        for tool, cost in tool_costs.items():
            st.session_state.added_costs.append({
                "name": tool,
                "quantity": tool_inputs[tool]["quantity"],
                "unit_price": tool_inputs[tool]["unit_price"],
                "total_cost": cost
            })

    # Custom Materials
    st.markdown("### Materiales Personalizados")
    custom_material = st.text_input("Nombre del material")
    custom_quantity = st.number_input("Cantidad", min_value=0, value=0, step=1)
    custom_unit_price = st.number_input("Precio unitario (€)", min_value=0.0, value=0.0, step=0.01)
    custom_cost = custom_quantity * custom_unit_price
    
# For custom materials
    if st.button("Agregar material personalizado al total"):
        st.session_state.total_estimated_costs += custom_cost
        st.session_state.added_costs.append({
            "name": custom_material,
            "quantity": custom_quantity,
            "unit_price": custom_unit_price,
            "total_cost": custom_cost
        })

    st.markdown("### Costos Agregados al Proyecto")
    for entry in st.session_state.added_costs:
        st.write(f"{entry['name']} (Cantidad: {entry['quantity']}, Precio unitario: €{entry['unit_price']:.2f}): €{entry['total_cost']:.2f}")
