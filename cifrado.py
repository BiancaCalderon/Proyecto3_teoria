def cifrar(mensaje, desplazamiento):
    resultado = ""
    for char in mensaje:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char  # No cifrar caracteres no alfabéticos
    return resultado

def descifrar(mensaje, desplazamiento):
    return cifrar(mensaje, -desplazamiento)
