from sys import stdin, stdout


def main():
    
    matriz = [[0 for i in range(105)] for x in range(55)]

    cases = int(stdin.readline().rstrip())
    while (cases > 0):
        N = int(stdin.readline().rstrip())

        for i in range(1, N+1):
            
            TMP = stdin.readline().strip().split()
            if (len(TMP) == 1):
                PODER = int(TMP[0])
                PESO = int(stdin.readline().rstrip())
            else:
                PODER = int(TMP[0])
                PESO = int(TMP[1])
            
            for j in range(1, PESO+1):
                if (j < PESO):
                    matriz[i][j] = matriz[i-1][j]
                else:
                    if matriz[i-1][j] < PODER + matriz[i-1][j-PESO]:
                        matriz[i][j] = PODER + matriz[i-1][j-PESO]
                    else:
                        matriz[i][j] = matriz[i-1][j]
        
        K = 0
        RES = 0
        TMP = stdin.readline().strip().split()
        if (len(TMP) == 1):
            K = int(TMP[0])
            RES = int(stdin.readline().rstrip())
        else:
            K = int(TMP[0])
            RES = int(TMP[1])

        if (matriz[N][K] >= RES):
            stdout.write("Missao completada com sucesso\n")
        else:
            stdout.write("Falha na missao\n")
        cases -= 1

if __name__ == "__main__":
    main() 