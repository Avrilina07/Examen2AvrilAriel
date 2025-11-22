import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):
    
    def setUp(self):
        """Configuración"""
        self.objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    
    # ===== Pruebas para ObtieneMasBailable =====
    def test1_ObtieneMasBailable(self):
        """Retorna el valor máximo de una lista de números positivos"""
        resultado = self.objeto.ObtieneMasBailable([0.8, 0.9, 0.7])
        self.assertEqual(resultado, 0.9)
    
    def test2_ObtieneMasBailable(self):
        """Retorna el valor máximo de una lista de números negativos"""
        resultado = self.objeto.ObtieneMasBailable([-5, -1, -10, -3])
        self.assertEqual(resultado, -1)
    
    # ===== Pruebas para VerificaListaCanciones =====
    def test1_VerificaListaCanciones(self):
        """Prueba que retorna True cuando todas las canciones son válidas"""
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"])
        self.assertTrue(resultado)
    
    def test2_VerificaListaCanciones(self):
        """Prueba que retorna False cuando hay un elemento None en la lista"""
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", None, "Canción 3"])
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()