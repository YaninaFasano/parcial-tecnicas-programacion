import ejercicio2
import unittest

class TestEjercicio2(unittest.TestCase):

    def testRecibirUnaListaVaciaYunaListaDeCuatroTuplasDeDosElementosCadaUnaConNumerosRepresentandoLasPosicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaVacia = []
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaVacia, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaListaDeUnElementoConUnaPalabraVaciaYunaListaDeCuatroTuplasDeDosElementosCadaUnaConNumerosRepresentandoLasPosicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaDeUnElementoConUnaPalabraVacia = [""]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeUnElementoConUnaPalabraVacia, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado, [])



    def testRecibirUnaListaDeUnElementoConCadenaDeCaracteresDeEspaciosYunaListaDeCuatroTuplasDeDosElementosCadaUnaConNumerosRepresentandoLasPosicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaDeUnElementoConCadenaDeCaracteresDeEspacios = ["      "]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeUnElementoConCadenaDeCaracteresDeEspacios, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaListaDeUnElementoConPalabrasYunaListaDeCuatroTuplasDeDosElementosCadaUnaConNumerosRepresentandoLasPosicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaDeUnElementoConPalabras = ["soy NO valido"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeUnElementoConPalabras, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaListaDeCuatroElementosConUnaPalabraPorElementoYunaListaDeCuatroTuplasDeDosElementosCadaUnaConNumerosRepresentandoLasPosicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaDeCuatroElementosConUnaPalabraPorElemento = ["yo","tambien","soy","invalido"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeCuatroElementosConUnaPalabraPorElemento, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaListaDeCuatroElementosConCuatroCaracteresPorElementoConVariacionesDePuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotesFormandoConjuntamenteElMapaDelJuegoYunaListaDeCuatroTuplasDeDosElementosCadaUnaConNumerosRepresentandoLasPosicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaDeCuatroElementosConCuatroCaracteresPorElementoConVariacionesDePuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotesFormandoConjuntamenteElMapaDelJuego = ["b.b.","....","..bb","b.b"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeCuatroElementosConCuatroCaracteresPorElementoConVariacionesDePuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotesFormandoConjuntamenteElMapaDelJuego, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaListaDeCuatroElementosConCincoCaracteresPorElementoConVariacionesDePuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotesFormandoConjuntamenteElMapaDelJuegoYunaListaDeCuatroTuplasDeDosElementosCadaUnaConNumerosRepresentandoLasPosicionesDeDisparosDePruebaDeberiaDevolverUnaListaDeDosTuplasDeDosElementosCadaUnaConNumerosRepresentandoLasPosicionesDeBotesQueNoFueronHundidos(self):
        #ARRANGE
        listaDeCuatroElementosConCincoCaracteresPorElementoConVariacionesDePuntosRepresentandoElAguaYdeLetrasBeLargaReprsentandolosBotesFormandoConjuntamenteElMapaDelJuego = ["b.b..","b...b",".....","....b"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeCuatroElementosConCincoCaracteresPorElementoConVariacionesDePuntosRepresentandoElAguaYdeLetrasBeLargaReprsentandolosBotesFormandoConjuntamenteElMapaDelJuego, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[(2,1),(2,5)])



    def testRecibirUnaListaDeTresElementosConTresCaracteresPorElementoConVariacionesDePuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotesFormandoConjuntamenteElMapaDelJuegoYunaListaVaciaDeberiaDevolverUnaListaDeDosTuplasDeDosElementosCadaUnaConNumerosRepresentandoLasPosicionesDeBotesQueNoFueronHundidos(self):
        #ARRANGE
        listaDeTresElementosConTresCaracteresPorElementoConVariacionesDePuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotesFormandoConjuntamenteElMapaDelJuego = ["b..","...","..b"]
        listaVacia = []

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeTresElementosConTresCaracteresPorElementoConVariacionesDePuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotesFormandoConjuntamenteElMapaDelJuego, listaVacia)

        #ASSERT
        self.assertEqual(resultado,[(1,1),(3,3)])
