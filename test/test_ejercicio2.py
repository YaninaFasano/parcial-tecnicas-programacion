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



    def testRecibirUnaListaConTresPalabrasYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        listaConTresPalabras = ["soy NO valido"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = ejercicio2.batallaDeBotesMain(listaConTresPalabras, posicionesDeDisparosDePrueba)

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


