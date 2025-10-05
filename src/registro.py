import re


def validar_nombre(self, nombre):
        return bool(re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$', nombre))

def validar_telefono(self, telefono):
        return telefono.isdigit() and len(telefono) == 10

def agregar_contacto(self, nombre, telefono):
        if not self.validar_nombre(nombre):
            raise ValueError("El nombre solo debe contener letras y espacios.")
        if not self.validar_telefono(telefono):
            raise ValueError("El número debe contener exactamente 10 dígitos.")
        self.contactos[nombre] = telefono
        return True

def buscar_contacto(self, nombre):
        return self.contactos.get(nombre, None)