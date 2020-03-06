while True:
    k = int(input())
    if k == 0:
        break
    Matriz = []
    for i in range(4):
        Elementos = []
        for j in range(4):
            Elemento = 0
            Elementos.append(Elemento)
        Matriz.append(Elementos)
    for i in range(len(Matriz)):
        for j in range(len(Matriz)):
            Termo = int(input())
            if i == j:
                Matriz[j][i] = Termo * k
            else:
                Matriz[j][i] = Termo
    for i in range(len(Matriz)):
        for j in range(len(Matriz)):
            if j < len(Matriz):
                print(Matriz[i][j], end=' ')
            else:
                print(Matriz[i][j], end=' ')
        print('')
