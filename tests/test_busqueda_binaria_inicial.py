
from cobertura.busqueda_binaria import busqueda_binaria

class TestBusquedaBinaria:

    
    def test_elemento_en_medio(self):
        arr = [1, 3, 5, 7, 9]
        assert busqueda_binaria(arr, 5) == 2
    
    def test_elemento_al_inicio(self):
        arr = [2, 4, 6, 8, 10]
        assert busqueda_binaria(arr, 2) == 0
