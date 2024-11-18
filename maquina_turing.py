from cifrado import cifrar, descifrar

class MaquinaTuring:
    def __init__(self, desplazamiento):
        self.desplazamiento = desplazamiento

    def encriptar(self, mensaje):
        return cifrar(mensaje, self.desplazamiento)

    def desencriptar(self, mensaje):
        return descifrar(mensaje, self.desplazamiento)
