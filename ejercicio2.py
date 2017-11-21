def verificaLongitudDeFilasEnMapa(mapa):
    if len(mapa) > 0:
        longitudes = []
        for fila in mapa:
            longitudes.append(len(fila))
            longitudGenerica = longitudes[0]
        for longitud in longitudes:
            if longitud != longitudGenerica:
                return []



def revisaValidezDelMapa(mapa):
    if verificaLongitudDeFilasEnMapa(mapa) == []:
        return []
    if type(mapa) != list or len(mapa) < 1:
        return []
    if len(mapa) > 0 and len(mapa[0]) > 0:
        verificarCaracter = mapa[0][:2]
        cadenaValida = '.b'
        for caracter in verificarCaracter:
            if caracter not in cadenaValida:
                return []



def encuentraBotes(mapa):
    botes = []
    for fila in mapa:
        if 'b' in fila:
            coordenada = 0
            for caracter in fila:
                if caracter == 'b':
                    bote = (mapa.index(fila) + 1, coordenada + 1)
                    coordenada = coordenada + 1
                else:
                    coordenada = coordenada + 1
                    continue
                botes.append(bote)
    return botes



def eliminaBotes(botes, disparos):
    for disparo in disparos:
        if disparo in botes:
            botes.remove(disparo)
    return botes



def batallaDeBotesMain(mapa, disparos):
    if revisaValidezDelMapa(mapa) == []:
        return []
    botesEnElMapa = encuentraBotes(mapa)
    sobrevivientes = eliminaBotes(botesEnElMapa, disparos)
    return sobrevivientes




def ejercicio2(var1,var2):
    return batallaDeBotesMain(var1,var2)

posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]


assert (ejercicio2(["b.b.","....","..bb","b.b"],posicionesDeDisparosDePrueba) == [])
assert (ejercicio2(["b.b..","b...b",".....","....b"],posicionesDeDisparosDePrueba) == [(2,1),(2,5)])
assert (ejercicio2(["b..","...","..b"],[]) == [(1,1),(3,3)])

