from maquina_turing import MaquinaTuring

def leer_configuracion(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    
    # Leer la llave y el mensaje
    for linea in lineas:
        if linea.startswith("w ="):
            return linea.split('=')[1].strip()  # Retorna la cadena de entrada

def main():
    ejemplos = [
        "2 # HOLA MUNDO",
        "B # HOLA MUNDO",
        "4 # PROGRAMACION",
        "E # PROGRAMACION",
        "1 # CIFRADO CESAR",
        "C # CIFRADO CESAR",
    ]

    for ejemplo in ejemplos:
        print(f"Ejemplo: {ejemplo}")
        procesar_ejemplo(ejemplo)
        print()  # Línea en blanco para separar ejemplos

def procesar_ejemplo(cadena_input):
    primer_caracter = cadena_input.split()[0]  # Extraer el primer carácter
    if primer_caracter.isdigit():  # Si es un número
        desplazamiento = int(primer_caracter)  # Convertir a entero
    else:  # Si es una letra
        desplazamiento = ord(primer_caracter.upper()) - ord('A')  # Convertir letra a desplazamiento

    mensaje = cadena_input.split("#")[1].strip()  # Extraer el mensaje

    maquina = MaquinaTuring(desplazamiento)

    # Cifrado
    mensaje_cifrado = maquina.encriptar(mensaje)
    print(f"Cifrado: {mensaje_cifrado}")

    # Desencriptado
    mensaje_descifrado = maquina.desencriptar(mensaje_cifrado)
    print(f"Descifrado: {mensaje_descifrado}")

if __name__ == "__main__":
    main()
