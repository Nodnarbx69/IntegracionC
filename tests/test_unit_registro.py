# test unitario de registro y búsqueda de contactos

from src.registro import registrar_contacto, buscar_contacto, contactos

def test_registrar_contacto_valido():
    resultado = registrar_contacto("Juan", "1234567891")
    assert resultado == "Contacto Juan registrado correctamente."
    assert "Juan" in contactos
    assert contactos["Juan"] == "1234567891"

def test_registrar_contacto_nombre_vacio():
    resultado = registrar_contacto("", "123456789")
    assert resultado == "Error: El nombre no puede estar vacío."

def test_registrar_contacto_numero_invalido():
    resultado = registrar_contacto("Ana", "12a45")
    assert resultado == "Error: Número inválido."

def test_buscar_contacto_existente():
    registrar_contacto("Pedro", "1234567891")
    resultado = buscar_contacto("Pedro")
    assert resultado == "Pedro: 1234567891"

def test_buscar_contacto_inexistente():
    resultado = buscar_contacto("Maria")
    assert resultado == "Error: Contacto no encontrado."
