import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):
    
    def setUp(self):
        """Configuración"""
        self.objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
    
    # ===== Pruebas para ObtieneValencia =====
    def test_ObtieneValencia_denumero_con_ceros(self):
        """Prueba para ver si los 0 no se cuenten como numeros impares"""
        res=self.objeto.ObtieneValencia(10000)
        self.assertEqual(res,1)


    def test_ObtieneValencia_numero_sin_impares(self):
        """Debe retornar 0 cuando no haya digitos impares"""
        res=self.objeto.ObtieneValencia(824620)
        self.assertEqual(res,0)

    # ===== Pruebas para DivisibleTempo =====
    def test_DivisibleTempo_numero_unico_divisor(self):
        """Retorna el divisor unico de el numero"""
        res = self.objeto.DivisibleTempo(1)
        self.assertEqual(res,[1])

    
    def test_DivisibleTempo_numero_muchos_divisores(self):
        """Retorna todos los divisores de un numero grande"""
        res = self.objeto.DivisibleTempo(30)
        self.assertEqual(res,[1,2,3,5,6,10,15,30])

    # ===== Pruebas para ObtieneMasBailable =====
    def test1_ObtieneMasBailable(self):
        """Retorna el valor máximo de una lista de números positivos"""
        resultado = self.objeto.ObtieneMasBailable([0.8, 0.9, 0.7])
        self.assertEqual(resultado, 0.7)
    
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


    #=====Prueba para Encurntra=====
    def test_Encuentra_numero_lista_vacia(self):
        """Debe retornar porque lista esta vacia"""
        res=self.objeto.Encuentra([],5)
        self.assertEqual(res,False)


if __name__ == '__main__':
    unittest.main()
    