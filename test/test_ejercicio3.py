import ejercicio3
import unittest

class TestEjercicio3(unittest.TestCase):

    def testRecibirUnaListaVaciaDeberiaDevolverUnaPalabraVacia(self):
        #ARRANGE
        listaVacia = []

        #ACT
        resultado = ejercicio3.funcionPrincipalLiga(listaVacia)

        #ASSERT
        self.assertEqual(resultado,"")



    def testRecibirUnaListaDeTuplasConEquiposYpuntajesDeberiaDevolverElEquipoConMayorPuntaje(self):
        #ARRANGE
        listaDeTuplasConEquiposYpuntajes = [("a", 1, "b", 0)]

        #ACT
        resultado = ejercicio3.funcionPrincipalLiga(listaDeTuplasConEquiposYpuntajes)

        #ASSERT
        self.assertEqual(resultado,"a")



    def testRecibirUnaListaDeTuplasDeTresElementosConEquiposYpuntajesDeberiaDevolverElEquipoConMayorPuntaje(self):
        #ARRANGE
        listaDeTuplasDeTresElementosConEquiposYpuntajes = [("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]

        #ACT
        resultado = ejercicio3.funcionPrincipalLiga(listaDeTuplasDeTresElementosConEquiposYpuntajes)

        #ASSERT
        self.assertEqual(resultado,"c")



    def testRecibirUnaListaDeTuplasDeTresElementosConEquiposYpuntajesIgualesDeberiaDevolverElEquipoEnElPrimerOrdenDelAlfabeto(self):
        #ARRANGE
        listaDeTuplasDeTresElementosConEquiposYpuntajesIguales = [("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]

        #ACT
        resultado = ejercicio3.funcionPrincipalLiga(listaDeTuplasDeTresElementosConEquiposYpuntajesIguales)

        #ASSERT
        self.assertEqual(resultado,"Almagro")



    def testRecibirUnaListaDeTuplasDeCuatroElementosConEquiposYpuntajesDeberiaDevolverElEquipoGanador(self):
        #ARRANGE
        listaDeTuplasDeCuatroElementosConEquiposYpuntajes = [("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]

        #ACT
        resultado = ejercicio3.funcionPrincipalLiga(listaDeTuplasDeCuatroElementosConEquiposYpuntajes)

        #ASSERT
        self.assertEqual(resultado,"a")