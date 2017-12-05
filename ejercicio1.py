def condiciones(cadena):
    verificacion = []
    lista = "no_espacio"
    for letra in cadena:
        if letra == " ":
            verificacion.append(letra)
        else:
            verificacion.append(lista)
    if lista not in verificacion or len(cadena) < 1:
        return False



def rotarPalabra(palabra):
    if condiciones(palabra) == False:
        return []
    lista = []
    rotacion = len(palabra)
    ultimaLetra = -1
    for vueltas in range(rotacion):
        rotar = palabra[ultimaLetra:] + palabra[:ultimaLetra]
        lista.append(rotar)
        ultimaLetra = ultimaLetra - 1
    lista = lista[::-1]
    return lista
