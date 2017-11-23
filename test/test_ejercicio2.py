import ejercicio2
import unittest

class TestEjercicio2(unittest.TestCase):

    def testRecibirUnaListaVaciaYPosicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaVacia = []
        PosicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaVacia, PosicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaListaConUnaPalabraVaciaYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaConUnaPalabraVacia = [""]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaConUnaPalabraVacia, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado, [])



    def testRecibirUnaListaConCadenaDeCaracteresDeEspaciosYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaConCadenaDeCaracteresDeEspacios = ["      "]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaConCadenaDeCaracteresDeEspacios, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaListaConPalabrasYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaConPalabras = ["soy NO valido"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaConPalabras, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaListaDeCuatroElementosConPalabrasYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaDeCuatroElementosConPalabras = ["yo","tambien","soy","invalido"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeCuatroElementosConPalabras, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaListaDeCuatroElementosConVariacionesDePuntosYLetrasYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaDeCuatroElementosConVariacionesDePuntosYLetras = ["b.b.","....","..bb","b.b"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeCuatroElementosConVariacionesDePuntosYLetras, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaListaDeCuatroElementosConVariacionesDePuntosYletrasYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaDeDosTuplasConPosicionesResultantes(self):
        #ARRANGE
        listaDeCuatroElementosConVariacionesDePuntosYletras = ["b.b..","b...b",".....","....b"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeCuatroElementosConVariacionesDePuntosYletras, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado,[(2,1),(2,5)])



    def testRecibirUnaListaDeTresElementosConVariacionesDePuntosYletrasYunaListaVaciaDeberiaDevolverUnaListaDeDosTuplasConPosicionesResultantes(self):
        #ARRANGE
        listaDeTresElementosConVariacionesDePuntosYletras = ["b..","...","..b"]
        listaVacia = []

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaDeTresElementosConVariacionesDePuntosYletras, listaVacia)

        #ASSERT
        self.assertEqual(resultado,[(1,1),(3,3)])
