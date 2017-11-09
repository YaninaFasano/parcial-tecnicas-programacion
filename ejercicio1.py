def rotarPalabra(palabra):
    rotacion = []
    lista = "no_espacio"
    for letra in palabra:
        if palabra == "":
            rotacion.append(letra)
        else:
            rotacion.append(lista)





def ejercicio1(var1):
    return rotarPalabra(var1)

assert (ejercicio1("") == [])
assert (ejercicio1("     ") == [])
assert (ejercicio1("a") == ['a'])
assert (ejercicio1("ab") == ['ab','ba'])
assert (ejercicio1("paz") == ['paz','azp','zpa'])
assert (ejercicio1("so l") == ['so l','o ls',' lso','lso '])
assert (ejercicio1("rotar") == ['rotar','otarr','tarro','arrot','rrota'])

