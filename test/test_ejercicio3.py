import ejercicio3
import unittest

class TestEjercicio3(unittest.TestCase):

    def testRecibirValoresVaciosDeberiaDevolverUnaPalabraVacia(self):
        #ARRANGE
        valoresVacios = []

        #ACT
        resultado = ejercicio3.calcularCampeonDeLaLiga(valoresVacios)

        #ASSERT
        self.assertEqual(resultado,"")



    def testRecibirLetrasRepresentandoEquiposYNumerosRepresentandoPuntajesParaCadaEquipoDeberiaDevolverElEquipoConMayorPuntaje(self):
        #ARRANGE
        letrasRepresentandoEquiposYNumerosRepresentandoPuntajesParaCadaEquipo = [("a", 1, "b", 0)]

        #ACT
        equipoConMayorPuntaje = ejercicio3.calcularCampeonDeLaLiga(letrasRepresentandoEquiposYNumerosRepresentandoPuntajesParaCadaEquipo)

        #ASSERT
        self.assertEqual(equipoConMayorPuntaje,"a")



    def testRecibirPuntajesDeLosEquiposEnDiferentesPartidosDeberiaDevolverElEquipoConMayorPuntajePromedio(self):
        #ARRANGE
        puntajesDeLosEquiposEnDiferentesPartidos = [("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]

        #ACT
        equipoConMayorPuntajePromedio = ejercicio3.calcularCampeonDeLaLiga(puntajesDeLosEquiposEnDiferentesPartidos)

        #ASSERT
        self.assertEqual(equipoConMayorPuntajePromedio,"c")



    def testRecibirPuntajesEmpatadosDeLosEquiposEnDiferentesPartidosDeberiaDevolverElEquipoEnElPrimerOrdenDelAlfabeto(self):
        #ARRANGE
        puntajesEmpatadosDeLosEquiposEnDiferentesPartidos = [("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]

        #ACT
        equipoEnElPrimerOrdenDelAlfabeto = ejercicio3.calcularCampeonDeLaLiga(puntajesEmpatadosDeLosEquiposEnDiferentesPartidos)

        #ASSERT
        self.assertEqual(equipoEnElPrimerOrdenDelAlfabeto,"Almagro")



    def testRecibirPuntajesTotalesDeEquiposEnDiferentesPartidosDeberiaDevolverElEquipoGanador(self):
        #ARRANGE
        puntajesTotalesDeEquiposEnDiferentesPartidos= [("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]

        #ACT
        equipoGanador = ejercicio3.calcularCampeonDeLaLiga(puntajesTotalesDeEquiposEnDiferentesPartidos)

        #ASSERT
        self.assertEqual(equipoGanador,"a")