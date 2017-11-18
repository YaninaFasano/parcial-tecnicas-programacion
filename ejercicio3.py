def puntajeEquipos(lista):
    tabla = []
    for tupla in lista:
        if tupla[1] == tupla[3]:
            tabla.append([tupla[0], 1])
            tabla.append([tupla[2], 1])
        if tupla[1] < tupla[3]:
            tabla.append([tupla[0], 0])
            tabla.append([tupla[2], 2])
        if tupla[1] > tupla[3]:
            tabla.append([tupla[0], 2])
            tabla.append([tupla[2], 0])
    return tabla


def sumarPuntaje(resultados):
    tabla = {}
    for lista in resultados:
        if lista[0] not in tabla:
            tabla[lista[0]] = lista[1]
        else:
            tabla[lista[0]] = tabla[lista[0]] + lista[1]
    return tabla


def elegirCampeonLiga(diccionario):
    maximoPuntaje = max(diccionario.values())
    for equipo in diccionario:
        if diccionario[equipo] == maximoPuntaje:
            return equipo


def chequeaEmpate(diccionario):
    puntajes = list(diccionario.values())
    puntaje1 = puntajes[0]
    for puntaje in puntajes[:1]:
        if puntaje == puntaje1:
            puntaje1 = False
        else:
            puntaje1 = True
    return puntajes


def OrdenarDiccionario(diccionario):
    equipos = sorted(list(diccionario.keys()))
    return equipos[0]


def funcionPrincipalLiga(lista):
    if len(lista) < 1:
        return ""
    listaDeTuplas = puntajeEquipos(lista)
    diccionario = sumarPuntaje(listaDeTuplas)
    if chequeaEmpate(diccionario) == False:
        return OrdenarDiccionario(diccionario)
    return elegirCampeonLiga(diccionario)




def ejercicio3(var1):
    return funcionPrincipalLiga(var1)




assert (ejercicio3([]) == "")
assert (ejercicio3([("a", 1, "b", 0)]) == "a")
assert (ejercicio3([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]) == "c")
assert (ejercicio3([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]) == "Almagro")
#assert (ejercicio3([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]) == "a")
