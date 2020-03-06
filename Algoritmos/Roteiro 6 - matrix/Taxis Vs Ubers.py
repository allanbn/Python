def LMInt(L = []):
    for x in range(len(L)):
        L[x] = int(L[x])
    return L
Pnaves = []
Pbombas = []
Matriz = []
MatrizFinal = []
N, M = input().split()  # dimensão da matriz
N = int(N)  # linhas
M = int(M)  # colunas
if 2 <= N <= 100 and 2 <= M <= 100:
    K = int(input())  # naves
    for i in range(K):
        CoordN = input().split()
        Pnaves.append(LMInt(CoordN))
H, B = input().split()
H = int(H)
B = int(B)
if 1 <= H <= 100 and 1 <= B <= N*M:
    for i in range(H):
        for j in range(B):
            CoordB = input().split()
            Pbombas.append(LMInt(CoordB))
for i in range(N):
    for j in range(M):
        Matriz.append(0)
    MatrizFinal.append(Matriz)
    Matriz = []
for x in range(N):
    for y in range(M):
        for i in range(len(Pnaves)):
            for j in range(len(Pnaves)):
                if x == i and j == i:
                    MatrizFinal[x][j] = 1
if N == M:
    for x in range(len(MatrizFinal)):
        print('')
        for y in range(len(MatrizFinal)):
            if y < len(MatrizFinal) - 1:
                print(MatrizFinal[x][y], end=' ')
            else:
                print(MatrizFinal[x][y], end='')
else:
    for x in range(len(MatrizFinal)):
        print('')
        for y in range(len(MatrizFinal) - 1):
            if y < len(MatrizFinal) - 1:
                print(MatrizFinal[x][y], end=' ')
            else:
                print(MatrizFinal[x][y], end='')
