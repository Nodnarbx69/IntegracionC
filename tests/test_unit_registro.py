import pytest
from src.registro import validar_nombre, validar_telefono, agregar_contacto, buscar_contacto, contactos

def test_validar_nombre_valido():
    assert validar_nombre("Juan Perez") is True

""" def test_validar_nombre_invalido():
    assert validar_nombre("Juan123") is False
    assert validar_nombre("") is False """

def test_validar_telefono_valido():
    assert validar_telefono("0987654321") is True
""" 
def test_validar_telefono_invalido():
    assert validar_telefono("12345") is False
    assert validar_telefono("123456789a") is False """

def test_agregar_contacto_valido():
    contactos.clear()
    assert agregar_contacto("Ana", "0987654321") is True
    assert contactos["Ana"] == "0987654321"

def test_agregar_contacto_nombre_invalido():
    with pytest.raises(ValueError, match="El nombre solo debe contener letras y espacios."):
        agregar_contacto("Ana123", "0987654321")

def test_agregar_contacto_telefono_invalido():
    with pytest.raises(ValueError, match="El número debe contener exactamente 10 dígitos."):
        agregar_contacto("Pedro", "12345")

def test_buscar_contacto_existente():
    contactos.clear()
    agregar_contacto("Luis", "0987654321")
    agregar_contacto("Julio", "0968133795")
    assert buscar_contacto("Luis") == "0987654321"

""" def test_buscar_contacto_inexistente():
    assert buscar_contacto("Carlos") is None
 """