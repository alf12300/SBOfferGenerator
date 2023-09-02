# Service reference costs and descriptions
COSTS_DESCRIPTIONS = {
    'Pintura Externa': {
        'cost': 350,  # cost per square meter
        'description': 'Pintura de grado premium resistente al clima, ideal para superficies exteriores. Formulada para durabilidad contra diversas condiciones climáticas, garantizando la retención del color y resistencia al descascarillado. Proporciona un acabado suave con adhesión superior.'
    },
    'Pintura Interna': {
        'cost': 200,  # cost per square meter
        'description': 'Pintura de alta calidad diseñada para superficies interiores. Ofrece un acabado suave y uniforme con excelente adhesión. El bajo contenido de VOC garantiza un mínimo impacto ambiental y mantiene una calidad de aire interior segura.'
    },
    'Reforma de Baño': {
        'cost': 650,  # cost per bathroom
        'description': 'Servicio de renovación para baños, incluyendo modernización de instalaciones, optimización del espacio y acabados de alta calidad para garantizar durabilidad y estética.'
    },
    'Reforma de Cocina': {
        'cost': 1500,  # cost per kitchen
        'description': 'Transformación completa de cocinas, adaptando espacios a las necesidades actuales, incorporando soluciones de almacenamiento innovadoras y seleccionando materiales de la más alta calidad para un resultado excepcional y duradero.'
    },
    'Reparacion de Puerta': {
        'cost': 250,  # cost per door
        'description': 'Servicio especializado en la restauración y mantenimiento de puertas. Atendemos desde fallos menores hasta reparaciones complejas, asegurando que las puertas funcionen correctamente y mantengan su apariencia original.'
    },
    'Reparacion de Ventana': {
        'cost': 250,  # cost per door
        'description': 'Servicio experto en la restauración y arreglo de ventanas. Desde solucionar filtraciones y sellados hasta reemplazar cristales dañados, garantizamos que cada ventana opere de manera eficiente y segura.'
    },
    'Reemplazo de Mobiliario': {
        'cost': 1500,  # custom cost
        'description': 'Servicio dedicado a la sustitución y renovación de muebles. Ya sea por desgaste o para actualizar estilos, ofrecemos soluciones que realzan el confort y estética de cualquier espacio.'
    },
}

# Commercial terms 
COMMERCIAL_TERMS = '''Términos Comerciales:
- Sin crédito, presupuesto válido por 30 días 			
- Horario de trabajo: 9h - 14h / 15h - 18h. Días de trabajo: acordar con cliente
- Informar si existe horario especial de obras en la comunidad.	'''

# Mapping of services to their associated tools
TOOLS_MAPPING = {
    'Pintura Externa': ['Latas de Pintura', 'Brochas', 'Rodillos', 'Cinta de Enmascarar'],
    'Pintura Interna': ['Latas de Pintura', 'Brochas', 'Rodillos', 'Paños de Caída'],
    'Reforma de Baño': ['Azulejos', 'Grifos', 'Cabezal de Ducha', 'Inodoro'],
    'Reforma de Cocina': ['Armarios', 'Encimeras', 'Fregadero', 'Grifo'],
    'Reparación de Puerta': ['Pomos de Puerta', 'Bisagras', 'Sello de Puerta'],
    'Reparacion de Ventana': ['Paneles de Vidrio', 'Sellos de Ventana', 'Cerraduras'],
    'Reemplazo de Mobiliario': ['Tablones de Madera', 'Clavos/Tornillos', 'Tapicería'],
}

