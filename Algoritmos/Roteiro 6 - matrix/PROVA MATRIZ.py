linhas = int(input())
colunas = int(input())
if linhas != colunas or linhas <= 0 or colunas <= 0:
    print('erro')
else:
    Matriz = []
    Elementos = []
    Soma = 0
    Dif = 0
    MaioresLinha = []
    MaioresColuna = []
    for i in range(linhas):
        for j in range(colunas):
            termos = int(input())
            Elementos.append(termos)
        Matriz.append(Elementos)
        Elementos = []
    for i in range(len(Matriz)):
        for j in range(len(Matriz)):
            if j == 0:
                MaiorLinha = Matriz[i][j]
                MaiorColuna = Matriz[j][i]
            elif Matriz[i][j] > MaiorLinha:
                MaiorLinha = Matriz[i][j]
            if Matriz[j][i] >= MaiorColuna:
                MaiorColuna = Matriz[j][i]
        MaioresColuna.append(MaiorColuna)
        MaioresLinha.append(MaiorLinha)
    cont = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz)):
            if i == 0 and j == 0:
                MaiordaMatriz = Matriz[i][j]
            elif Matriz[i][j] > MaiordaMatriz:
                MaiordaMatriz = Matriz[i][j]
            if i == j and Matriz[i][j] > 0:
                Soma += Matriz[i][j]
            if i + j == (len(Matriz) - 1) and cont == 0:
                Dif = Matriz[i][j]
                cont += 1
            elif i + j == (len(Matriz) - 1) and cont > 0:
                Dif -= Matriz[i][j]
    print(MaioresLinha)
    print(MaioresColuna)
    print(MaiordaMatriz)
    print(Soma)
    print(Dif)
