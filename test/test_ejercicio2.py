import ejercicio2
import unittest

class TestEjercicio2(unittest.TestCase):

    def testRecibirUnMapaVacioYPosicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        mapaVacio = []
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        posiciones = ejercicio2.calcularPosicionesBarcosSobrevivientes(mapaVacio, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(posiciones,[])



    def testRecibirUnMapaConUnaPalabraVaciaYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        mapaConUnaPalabraVacia = [""]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        posiciones = ejercicio2.calcularPosicionesBarcosSobrevivientes(mapaConUnaPalabraVacia, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(posiciones, [])



    def testRecibirUnMapaConCadenaDeCaracteresDeEspaciosYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        mapaConCadenaDeCaracteresDeEspacios = ["      "]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        posiciones = ejercicio2.calcularPosicionesBarcosSobrevivientes(mapaConCadenaDeCaracteresDeEspacios, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(posiciones,[])



    def testRecibirUnMapaNoValidoYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        mapaNoValido = ["soy NO valido"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        posiciones = ejercicio2.calcularPosicionesBarcosSobrevivientes(mapaNoValido, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(posiciones,[])



    def testRecibirUnMapaNoValidoYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        mapaNoValido = ["yo","tambien","soy","invalido"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        posiciones = ejercicio2.calcularPosicionesBarcosSobrevivientes(mapaNoValido, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(posiciones,[])



    def testRecibirUnMapaConFilasDeDistintasCantidadDeElementosYposicionesDeDisparosDePruebaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        mapaConFilasDeDistintasCantidadDeElementos = ["b.b.","....","..bb","b.b"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        posiciones = ejercicio2.calcularPosicionesBarcosSobrevivientes(mapaConFilasDeDistintasCantidadDeElementos, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(posiciones,[])



    def testRecibirUnMapaDePuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotesYposicionesDeDisparosDePruebaDeberiaDevolverLasPosicionesDeBotesQueNoFueronHundidos(self):
        #ARRANGE
        mapaConPuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotes= ["b.b..","b...b",".....","....b"]
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        posiciones = ejercicio2.calcularPosicionesBarcosSobrevivientes(mapaConPuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotes, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(posiciones,[(2,1),(2,5)])



    def testRecibirUnMapaConPuntosRepresentandoElAguaYdeLetrasBeLargaRepresentandoLosBotesYunMapaVacioDeberiaDevolverlasPosicionesDeBotesQueNoFueronHundidos(self):
        #ARRANGE
        mapaConPuntosRepresentandoElAguaYletrasBeLargaRepresentandoLosBotes= ["b..","...","..b"]
        mapaVacio = []

        #ACT
        resultado = ejercicio2.calcularPosicionesBarcosSobrevivientes(mapaConPuntosRepresentandoElAguaYletrasBeLargaRepresentandoLosBotes, mapaVacio)

        #ASSERT
        self.assertEqual(resultado,[(1,1),(3,3)])
