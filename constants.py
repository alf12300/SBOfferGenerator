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
Recargos:
Todos los servicios están sujetos a un recargo del 10% por concepto de servicio.
Cotización: Cualquier requerimiento adicional fuera de la cotización inicial podría generar cargos extra.
Disponibilidad:
El inicio de los trabajos está sujeto a disponibilidad y programación. Se recomienda reservar con anticipación para garantizar las fechas deseadas.
Pago:
El pago debe realizarse dentro de los 30 días posteriores a la finalización del servicio.
Aceptamos pagos a través de transferencia bancaria, cheque o efectivo.
Para proyectos que excedan un monto de €5,000, se requiere un adelanto del 50% para comenzar los trabajos.
Cancelaciones:
Las cancelaciones hechas con menos de 10 días de anticipación pueden estar sujetas a una tarifa de cancelación equivalente al 10% del costo total del proyecto.
Las postergaciones o reprogramaciones deben ser comunicadas con al menos 5 días de anticipación.
Garantía:
Todos nuestros trabajos de remodelación cuentan con una garantía de 12 meses, asegurando la calidad y durabilidad de los mismos.
Seguridad:
Todos nuestros empleados están asegurados y capacitados para garantizar la seguridad en cada proyecto.

Información de Contacto:
Nombre de la Empresa: Remodelaciones XYZ
Dirección: Calle Falsa 123, Ciudad, Provincia
Teléfono: +34 123 456 789
Email: contacto@remodelacionesxyz.es
Horario de Atención: Lunes a Viernes de 09:00 a 18:00'''

# Mapping of services to their associated tools
TOOLS_MAPPING = {
    'PINTURA EXTERNA': ['Latas de Pintura', 'Brochas', 'Rodillos', 'Cinta de Enmascarar'],
    'PINTURA INTERNA': ['Latas de Pintura', 'Brochas', 'Rodillos', 'Paños de Caída'],
    'REFORMA DE BAÑO': ['Azulejos', 'Grifos', 'Cabezal de Ducha', 'Inodoro'],
    'REFORMA DE COCINA': ['Armarios', 'Encimeras', 'Fregadero', 'Grifo'],
    'REPARACION DE PUERTA': ['Pomos de Puerta', 'Bisagras', 'Sello de Puerta'],
    'REPARACION DE VENTANA': ['Paneles de Vidrio', 'Sellos de Ventana', 'Cerraduras'],
    'REEMPLAZO DE MOBILIARIO': ['Tablones de Madera', 'Clavos/Tornillos', 'Tapicería'],
}

