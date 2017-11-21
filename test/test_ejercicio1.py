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



    def testRecibirUnCaracterDeberiaDevolverUnaListaConUnCaracter(self):
        #ARRANGE
        caracter = "a"

        #ACT
        resultado = ejercicio1.rotarPalabra(caracter)

        #ASSERT
        self.assertEqual(resultado,['a'])



    def testRecibirDosCaracteresDeberiaDevolverUnaListaDeDosElementosConLaPalabraOriginalYrotada(self):
        #ARRANGE
        dosCaracteres = "ab"

        #ACT
        resultado = ejercicio1.rotarPalabra(dosCaracteres)

        #ASSERT
        self.assertEqual(resultado,['ab','ba'])



    def testRecibirTresCaracteresDeberiaDevolverUnaListaDeTresElementosConLaPalabraOriginalYrotada(self):
        #ARRANGE
        tresCaracteres = "paz"

        #ACT
        resultado = ejercicio1.rotarPalabra(tresCaracteres)

        #ASSERT
        self.assertEqual(resultado,['paz','azp','zpa'])



    def testRecibirTresCaracteresYunEspacioDeberiaDevolverUnaListaDeCuatroElementosConLaPalabraOriginalYrotada(self):
        #ARRANGE
        tresCaracteresYunEspacio = "so l"

        #ACT
        resultado = ejercicio1.rotarPalabra(tresCaracteresYunEspacio)

        #ASSERT
        self.assertEqual(resultado,['so l','o ls',' lso','lso '])



    def testRecibirCincoCaracteresDeberiaDevolverUnaListaDeCincoElementosConLaPalabraOriginalYrotada(self):
        #ARRANGE
        cincoCaracteres = "rotar"

        #ACT
        resultado = ejercicio1.rotarPalabra(cincoCaracteres)

        #ASSERT
        self.assertEqual(resultado,['rotar','otarr','tarro','arrot','rrota'])

