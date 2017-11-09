def puntajeEquipos(lista):
    tabla = []
    for tupla in lista:
        if tupla[1] == tupla[3]:
            lista.append([tupla[0], 1])
            lista.append([tupla[2], 1])
        if tupla[1] < tupla[3]:
            lista.append([tupla[0], 0])
            lista.append([tupla[2], 2])
        if tupla[1] > tupla[3]:
            lista.append([tupla[0], 2])
            lista.append([tupla[2], 0])
    return tabla

def sumarPuntaje()

def ejercicio3(var1):
    return puntajeEquipos(var1)


assert (ejercicio3([]) == "")
assert (ejercicio3([("a", 1, "b", 0)]) == "a")
assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")
