Matriz1 = []
Matriz2 = []
MatrizSoma1 = []
MatrizSoma2 = []
MatrizResultado = []
Resultado = []
dimensoes = input().split()
N = int(dimensoes[0])  # linhas da matriz A
M = int(dimensoes[1])  # colunas da matriz A e linhas da matriz B
O = int(dimensoes[2])  # colunas da matriz B
for i in range(N):
    Matriz = input().split()
    for x in range(len(Matriz)):
        Matriz[x] = int(Matriz[x])
    Matriz1.append(Matriz)
for i in range(M):
    Matriz = input().split()
    for x in range(len(Matriz)):
        Matriz[x] = int(Matriz[x])
    Matriz2.append(Matriz)
for y in range(M):  # Colunas A / Linhas B
    Resultado.append(Matriz1[0][y] * Matriz2[y][0])
MatrizSoma1.append(sum(Resultado))
Resultado = []
for y in range(M):  # Colunas A / Linhas B
    Resultado.append(Matriz1[0][y] * Matriz2[y][1])
MatrizSoma1.append(sum(Resultado))
Resultado = []
MatrizResultado.append(MatrizSoma1)
for y in range(M):  # Colunas A / Linhas B
    Resultado.append(Matriz1[1][y] * Matriz2[y][0])
MatrizSoma2.append(sum(Resultado))
Resultado = []
for y in range(M):  # Colunas A / Linhas B
    Resultado.append(Matriz1[1][y] * Matriz2[y][1])
MatrizSoma2.append(sum(Resultado))
Resultado = []
MatrizResultado.append(MatrizSoma2)
for x in range(len(MatrizResultado)):
    print("")
    for y in range(len(MatrizResultado[x])):
        if y < (len(MatrizResultado[x])-1):
            print(MatrizResultado[x][y], end=" ")
        else:
            print(MatrizResultado[x][y], end="")