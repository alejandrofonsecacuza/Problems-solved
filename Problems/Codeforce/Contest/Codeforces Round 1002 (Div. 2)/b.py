def encontrar_solucion():
    cantidad_elementos, cantidad_subarreglos = map(int, input().split())
    lista_elementos = list(map(int, input().split()))
    
    if cantidad_subarreglos == cantidad_elementos:
        contador = 0
        for indice in range(1, cantidad_elementos, 2):
            if lista_elementos[indice] != contador + 1:
                print(contador + 1)
                return
            contador += 1
        print((cantidad_elementos // 2) + 1)
        return
    
    if lista_elementos[0] != 1:
        if lista_elementos[0] != 1 and lista_elementos[1] != 1:
            print(1)
            return
        for indice in range(1, cantidad_elementos):
            if lista_elementos[indice] != 1 and cantidad_elementos - indice >= cantidad_subarreglos - 1:
                print(1)
                return
    else:
        for indice in range(cantidad_elementos):
            if lista_elementos[indice] != 1 and cantidad_elementos - indice >= cantidad_subarreglos - 1:
                print(1)
                return
    
    print(2)

def ejecutar_programa():
    casos_prueba = int(input())
    for _ in range(casos_prueba):
        encontrar_solucion()

if __name__ == "__main__":
    ejecutar_programa()