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



    def testRecibirUnaListaDeUnaTuplaDeCuatroElementosConLetrasRepresentandoAlosEquiposYnumerosRepresentandoLosPuntajesCorrespondientesParaCadaEquipoDeberiaDevolverElEquipoConMayorPuntaje(self):
        #ARRANGE
        listaDeUnaTuplaDeCuatroElementosConLetrasRepresentandoAlosEquiposYnumerosRepresentandoLosPuntajesCorrespondientesParaCadaEquipo = [("a", 1, "b", 0)]

        #ACT
        resultado = ejercicio3.funcionPrincipalLiga(listaDeUnaTuplaDeCuatroElementosConLetrasRepresentandoAlosEquiposYnumerosRepresentandoLosPuntajesCorrespondientesParaCadaEquipo)

        #ASSERT
        self.assertEqual(resultado,"a")



    def testRecibirUnaListaDeTresTuplasDeCuatroElementosCadaUnaConLetrasRepresentandoAlosEquiposYnumerosRepresentandoLosPuntajesCorrespondientesParaCadaEquipoDeberiaDevolverElEquipoConMayorPuntajeAlSumarseLosPuntajesDeLosElementosCorrespondientesApuntajesDeLasTresTuplas(self):
        #ARRANGE
        listaDeTresTuplasDeCuatroElementosCadaUnaConLetrasRepresentandoAlosEquiposYnumerosRepresentandoLosPuntajesCorrespondientesParaCadaEquipo = [("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]

        #ACT
        resultado = ejercicio3.funcionPrincipalLiga(listaDeTresTuplasDeCuatroElementosCadaUnaConLetrasRepresentandoAlosEquiposYnumerosRepresentandoLosPuntajesCorrespondientesParaCadaEquipo)

        #ASSERT
        self.assertEqual(resultado,"c")



    def testRecibirUnaListaDeTresTuplasDeCuatroElementosCadaUnaConNombresDeLosEquiposYPuntajesIgualesAunoParaTodosLosEquiposDeberiaDevolverElEquipoEnElPrimerOrdenDelAlfabeto(self):
        #ARRANGE
        listaDeTresTuplasDeCuatroElementosCadaUnaConNombresDeLosEquiposYPuntajesIgualesAunoParaTodosLosEquipos = [("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]

        #ACT
        resultado = ejercicio3.funcionPrincipalLiga(listaDeTresTuplasDeCuatroElementosCadaUnaConNombresDeLosEquiposYPuntajesIgualesAunoParaTodosLosEquipos)

        #ASSERT
        self.assertEqual(resultado,"Almagro")



    def testRecibirUnaListaDeCuatroTuplasDeCuatroElementosCadaUnaConLetrasRepresentandoAlosEquiposYnumerosRepresentandoLosPuntajesFinalesCorrespondientesParaCadaEquipoDeberiaDevolverElEquipoGanadorAlSumarseLosPuntajesDeLosElementosCorrespondientesAPuntajesDeLasCuatroTuplas(self):
        #ARRANGE
        listaDeCuatroTuplasDeCuatroElementosCadaUnaConLetrasRepresentandoAlosEquiposYnumerosRepresentandoLosPuntajesFinalesCorrespondientesParaCadaEquipo = [("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]

        #ACT
        resultado = ejercicio3.funcionPrincipalLiga(listaDeCuatroTuplasDeCuatroElementosCadaUnaConLetrasRepresentandoAlosEquiposYnumerosRepresentandoLosPuntajesFinalesCorrespondientesParaCadaEquipo)

        #ASSERT
        self.assertEqual(resultado,"a")