# algoritmo de busqueda binaria

def busqueda_binaria(arr, objetivo):
    bajo = 0
    alto = len(arr) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2 # Calcula el índice medio
        
        if arr[medio] == objetivo:
            return medio # Objetivo encontrado, devuelve el índice
        
        elif arr[medio] < objetivo:
            bajo = medio + 1 # El objetivo está en la mitad derecha
        
        else:
            alto = medio - 1 # El objetivo está en la mitad izquierda
            
    return -1 # Objetivo no encontrado en la lista