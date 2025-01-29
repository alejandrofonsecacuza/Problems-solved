def find_mex(arr):
    """
    Encuentra el MEX (Minimum Excluded Value) de una lista de números enteros no negativos.

    Parámetros:
        nums (list): Lista de números enteros no negativos.

    Retorna:
        int: El MEX de la lista.
    """
    # Convertir la lista a un set para búsquedas eficientes (O(1))
    arr_set = set(arr)
    mex = 0
    while mex in arr_set:
        mex += 1
    return mex

