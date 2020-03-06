from sys import stdin, stdout


def sol(i, pos, knapsack, pp, N, PODER=0, PESO=1):

    if knapsack[i][pos] != -1:
        return knapsack[i][pos]

    if i >= N or pos <= 0:
        knapsack[i][pos] = 0
        return knapsack[i][pos]    

    knapsack[i][pos] = sol(i+1, pos, knapsack, pp, N)
    if pos >= pp[i][PESO]:
        knapsack[i][pos] = max(knapsack[i][pos], pp[i][PODER] + sol(i + 1, pos - pp[i][PESO], knapsack, pp, N))

    return knapsack[i][pos]


def main():
    pp = [[0 for i in range(2)] for x in range(102)]
    matriz = []
    flag = 1

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

        K = 0
        RES = 0
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

        ans = sol(1, K, matriz, pp, N+1)
        if (ans >= RES):
            stdout.write("Missao completada com sucesso\n")
        else:
            stdout.write("Falha na missao\n")
        cases -= 1


if __name__ == "__main__":
    main()