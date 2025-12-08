""" búsqueda binaria con anomalías """

def busqueda_binaria(arr, objetivo):
    """Realiza búsqueda binaria en un arreglo ordenado."""
    contador_iteraciones = 0  # anomalia 1
    bajo = 0
    alto = len(arr) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2

        if arr[medio] == objetivo:
            # anomalia 2
            print(f"Elemento encontrado después de {num_comparaciones} comparaciones")
            return medio

        if arr[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1
