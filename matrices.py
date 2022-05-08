print('Multiplicador de matrices')
cantidad = input('Cuántas matrices desea multiplicar?: ')

cantidad = int(cantidad)

orden = []
for i in range(cantidad + 1):
    if i == 0:
        continue
    filas = input(f'Ingrese la cantidad de filas de la matriz nro. {i}: ')
    filas = int(filas)
    columnas = input(f'Ingrese la cantidad de columnas de la matriz nro. {i}: ')
    columnas = int(columnas)
    orden.append((filas, columnas))

matrices = {}
elementos = {}
letra = 0
letras = 'abcdefghijk'
for fila, columna in orden:
    for numero_fila in range(fila + 1):
        if numero_fila == 0:
            continue
        for numero_columna in range(columna + 1):
            if numero_columna == 0:
                continue
            elementos[letras[letra] + str(numero_fila) + str(numero_columna)] = input(
                f'Ingrese el elemento {letras[letra]}{numero_fila}{numero_columna}: ')
            elementos[letras[letra] + str(numero_fila) + str(numero_columna)] = int(
                elementos[letras[letra] + str(numero_fila) + str(numero_columna)])
    matrices[letras[letra]] = elementos
    elementos = {}
    letra = letra + 1

matriz_resultado = {}


def calcular_producto(contador, filac, columnac):
    global matriz
    global matriz2
    global matriz_a
    global matriz_b
    resultado = 0
    for contador in range(contador + 1):
        if contador == 0:
            continue
        resultado = resultado + (
                matriz_a[matriz + str(filac) + str(contador)] * matriz_b[matriz2 + str(contador) + str(columnac)])
    return resultado


for i in range(cantidad - 1):
    matriz = letras[i]
    matriz2 = letras[i + 1]
    matriz_a = matrices[matriz]
    matriz_b = matrices[matriz2]
    orden_a = orden[i]
    orden_b = orden[i + 1]
    orden_resultado = (orden_a[0], orden_b[1])

    for numero_fila in range(orden_resultado[0] + 1):
        if numero_fila == 0:
            continue
        for numero_columna in range(orden_resultado[1] + 1):
            if numero_columna == 0:
                continue
            elementos[letras[letra] + str(numero_fila) + str(numero_columna)] = calcular_producto(orden_a[1],
                                                                                                  numero_fila,
                                                                                                  numero_columna)

    print(elementos)
