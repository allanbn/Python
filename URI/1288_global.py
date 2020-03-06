from sys import stdin, stdout

N = 0
RES = 0
K = 0
pp = [[0 for i in range(2)] for x in range(102)]
matriz = []
flag = 1


def sol(i, pos, PODER=0, PESO=1):
    global K, RES, N, pp, matriz

    if i >= N+1:
        return 0  

    if matriz[i][pos] != -1:
        return matriz[i][pos]

    matriz[i][pos] = sol(i+1, pos)
    if pos + pp[i][PESO] <= K:
        matriz[i][pos] = max(matriz[i][pos], pp[i][PODER] + sol(i + 1, pos + pp[i][PESO]))

    return matriz[i][pos]


def main():
    global K, RES, N, pp, matriz, flag


    cases = int(stdin.readline().rstrip())
    while (cases > 0):
        N = int(stdin.readline().rstrip())
        for i in range(1, N + 1):
            TMP = stdin.readline().strip().split()
            if (len(TMP) == 1):
                pp[i][0] = int(TMP[0])
                pp[i][1] = int(stdin.readline().rstrip())
            else:
                pp[i][0] = int(TMP[0])
                pp[i][1] = int(TMP[1])

        
        TMP = stdin.readline().strip().split()
        if (len(TMP) == 1):
            K = int(TMP[0])
            RES = int(stdin.readline().rstrip())
        else:
            K = int(TMP[0])
            RES = int(TMP[1])

        if flag == 1:
            matriz = [[-1 for i in range(102)] for x in range(55)]
            flag = 0
        else:
            for i in range(1, 55):
                for j in range(1, 102):
                    matriz[i][j] = -1

        ans = sol(1, 1)
        if (ans >= RES):
            stdout.write("Missao completada com sucesso\n")
        else:
            stdout.write("Falha na missao\n")
        cases -= 1


if __name__ == "__main__":
    main()