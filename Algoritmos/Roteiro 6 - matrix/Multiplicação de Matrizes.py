def MatrizInt(L = []):
    for x in range(len(L)):
        L[x] = int(L[x])
    return L


Matriz1 = []
Matriz2 = []
MatrizSoma = []
MatrizResultado = []
Resultado = []
dimensoes = input().split()
N = int(dimensoes[0])  # linhas da matriz A
M = int(dimensoes[1])  # colunas da matriz A e linhas da matriz B
O = int(dimensoes[2])  # colunas da matriz B
for i in range(N):
    Matriz = input().split()
    Matriz1.append(MatrizInt(Matriz))
for i in range(M):
    Matriz = input().split()
    Matriz2.append(MatrizInt(Matriz))
for x in range(N):
    for y in range(O):  # Colunas A / Linhas B
        for z in range(M):
            Resultado.append(Matriz1[x][z] * Matriz2[z][y])
        MatrizSoma.append(sum(Resultado))
        Resultado = []
    MatrizResultado.append(MatrizSoma)
    MatrizSoma = []
for x in range(len(MatrizResultado)):
    print('')
    for y in range(len(MatrizResultado[x])):
        if y < (len(MatrizResultado[x])-1):
            print(MatrizResultado[x][y], end=' ')
        else:
            print(MatrizResultado[x][y], end='')
