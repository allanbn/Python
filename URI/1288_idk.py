from sys import stdin, stdout

def main():
    pp = [[0 for i in range(2)] for x in range(102)]
    matriz = []
    flag = 1

    cases = int(stdin.readline().rstrip())
    while (cases > 0):
        N = int(stdin.readline().rstrip())
        for i in range(1, N+1):
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
            matriz = [-1 for i in range(102)]
            flag = 0
        else:
            for j in range(1, 102):
                matriz[j] = -1

        
        for i in range(1, N+1):
            for j in range(1, K+1):
                if matriz[i] != -1:
                    if (i >= pp[i][1]):
                        at = matriz[i - pp[i][1]]
                        matriz[i - pp[i][1]] = max(at, matriz[i]+pp[i][0])
            if (pp[i][1] <= K):
                at = matriz[K - pp[i][1]]
                matriz[K - pp[i][1]] = max(at, pp[i][0])
        ok = False
        
        for i in range(1, K+1):
            if matriz[i] >= RES:
                ok = True
                break
        
        if ok is True:
            stdout.write("Missao completada com sucesso\n")
        else:
            stdout.write("Falha na missao\n")
        cases -= 1


if __name__ == "__main__":
    main()