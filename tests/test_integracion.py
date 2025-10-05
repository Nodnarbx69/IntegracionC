

from src.registro import validar_nombre, validar_telefono, agregar_contacto, buscar_contacto, contactos

def test_flujo_agregar_y_buscar_contacto():
    datos_prueba = {
        "Ana Lopez": "0981111111",
        "Juan Perez": "0982222222",
        "Maria Vega": "0983333333"
    }

    # Agregar contactos
    for nombre, telefono in datos_prueba.items():
        agregar_contacto(nombre, telefono)

    # Verificar búsqueda
    for nombre, telefono in datos_prueba.items():
        assert buscar_contacto("Juan Perez") == "0982222222"