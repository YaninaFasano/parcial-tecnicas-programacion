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




def ejercicio1(var1):
    return rotarPalabra(var1)

assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])
assert (ejercicio1("ab") == ['ab','ba'])
assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])

