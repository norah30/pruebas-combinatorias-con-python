# test busqueda binaria mejorado 

import pytest
from cobertura.busqueda_binaria import busqueda_binaria

class TestBusquedaBinariaMejorado:

    def test_un_elemento_encontrado(self):
        arr = [42]
        assert busqueda_binaria(arr, 42) == 0

    def test_un_elemento_no_encontrado(self):
        arr = [42]
        assert busqueda_binaria(arr, 0) == -1

    def test_negativos(self):
        arr = [-10, -5, 0, 5, 10]
        assert busqueda_binaria(arr, -5) == 1

    def test_grande(self):
        arr = list(range(0, 1000, 2))
        assert busqueda_binaria(arr, 500) == 250

    def test_intermedio_no_existe(self):
        arr = [10, 20, 30, 40, 50]
        assert busqueda_binaria(arr, 25) == -1

@pytest.mark.parametrize("arr,objetivo,esperado", [
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 6, -1),
    ([-5, -3, 0, 3, 5], 0, 2),
    ([42], 42, 0),
    ([42], 0, -1),
    ([], 10, -1),
])
def test_parametrizado(arr, objetivo, esperado):
    assert busqueda_binaria(arr, objetivo) == esperado
