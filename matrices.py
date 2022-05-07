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
i = 0
letras = 'abcdefghijk'
for fila, columna in orden:
    for numero_fila in range(fila + 1):
        if numero_fila == 0:
            continue
        for numero_columna in range(columna + 1):
            if numero_columna == 0:
                continue
            elementos[letras[i] + str(numero_fila) + str(numero_columna)] = input(f'Ingrese el elemento {letras[i]}{numero_fila}{numero_columna}: ')
            elementos[letras[i] + str(numero_fila) + str(numero_columna)] = int(elementos[letras[i] + str(numero_fila) + str(numero_columna)])
    matrices[letras[i]] = elementos
    elementos = {}
    i = i + 1

print(matrices)
print(matrices['a'])

# resultado = {}


# for fila, columna in orden:
#     for numero_fila in range(fila + 1):
#         if numero_fila == 0:
#             continue
#         for numero_columna in range(columna + 1):
#             if numero_columna == 0:
#                 continue
#             resultado[letras[i + 1] + str(numero_fila) + str(numero_columna)] = elementos['a11'] * elementos['b11']
