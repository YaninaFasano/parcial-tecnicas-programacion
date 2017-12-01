import ejercicio1
import unittest

class TestEjercicio1(unittest.TestCase):

    def testRecibirUnaPalabraVaciaDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        palabraVacia = ""

        #ACT
        resultado = ejercicio1.rotarPalabra(palabraVacia)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaCadenaDeCaracteresDeEspaciosDeberiaDevolverUnaListaVacia(self):
        #ARRANGE
        cadenaDeCaracteresDeEspacios = "     "

        #ACT
        resultado = ejercicio1.rotarPalabra(cadenaDeCaracteresDeEspacios)

        #ASSERT
        self.assertEqual(resultado,[])



    def testRecibirUnaPalabraDeUnCaracterDeberiaDevolverUnaListaDeUnElementoConLaPalabraRecibida(self):
        #ARRANGE
        palabraDeUnCaracter = "a"

        #ACT
        resultado = ejercicio1.rotarPalabra(palabraDeUnCaracter)

        #ASSERT
        self.assertEqual(resultado,['a'])



    def testRecibirUnaPalabraDeDosCaracteresDeberiaDevolverUnaListaDeDosElementosConLaPalabraRecibidaYrotada(self):
        #ARRANGE
        palabraDeDosCaracteres = "ab"

        #ACT
        resultado = ejercicio1.rotarPalabra(palabraDeDosCaracteres)

        #ASSERT
        self.assertEqual(resultado,['ab','ba'])



    def testRecibirUnaPalabraDeTresCaracteresDeberiaDevolverUnaListaDeTresElementosConLaPalabraRecibidaYrotada(self):
        #ARRANGE
        palabraDeTresCaracteres = "paz"

        #ACT
        resultado = ejercicio1.rotarPalabra(palabraDeTresCaracteres)

        #ASSERT
        self.assertEqual(resultado,['paz','azp','zpa'])



    def testRecibirUnaPalabraDeCuatroCaracteresDeberiaDevolverUnaListaDeCuatroElementosConLaPalabraRecibidaYrotada(self):
        #ARRANGE
        palabraDeCuatroCaracteres = "so l"

        #ACT
        resultado = ejercicio1.rotarPalabra(palabraDeCuatroCaracteres)

        #ASSERT
        self.assertEqual(resultado,['so l','o ls',' lso','lso '])



    def testRecibirUnaPalabraDeCincoCaracteresDeberiaDevolverUnaListaDeCincoElementosConLaPalabraRecibidaYrotada(self):
        #ARRANGE
        palabraDeCincoCaracteres = "rotar"

        #ACT
        resultado = ejercicio1.rotarPalabra(palabraDeCincoCaracteres)

        #ASSERT
        self.assertEqual(resultado,['rotar','otarr','tarro','arrot','rrota'])