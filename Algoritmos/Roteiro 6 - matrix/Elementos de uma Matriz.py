Matriz = []
Elementos = []
ContMaior = 0
ContMenor = 0
SomaPri = 0
SomaSec = 0
Linhas, Colunas = input().split()
Linhas = int(Linhas)
Colunas = int(Colunas)
for i in range(Linhas):
    for j in range(Colunas):
        Elemento = int(input())
        if Elemento > 0:
            ContMaior += 1
        else:
            ContMenor += 1
        Elementos.append(Elemento)
    Matriz.append(Elementos)
    Elementos = []
if Linhas == Colunas:
    for i in range(len(Matriz)):
        for j in range(len(Matriz)):
                if i == j:
                    SomaPri += Matriz[i][j]
                if i + j == (len(Matriz) - 1):
                    SomaSec += Matriz[i][j]
print('Matriz formada:')
for i in range(len(Matriz)):
    for j in range(len(Matriz[i])):
        if j < len(Matriz[i]) - 1:
            print(Matriz[i][j], end=' ')
        else:
            print(Matriz[i][j], end='')
    print('')
if Linhas == Colunas:
    print('A diagonal principal e secundaria tem valor(es) {} e {} respectivamente.'.format(SomaPri, SomaSec))
    print('A matriz possui {} numero(s) menor(es) que zero.'.format(ContMenor))
    print('A matriz possui {} numero(s) maior(es) que zero.'.format(ContMaior))
else:
    print('A diagonal principal e secundaria nao pode ser obtida.')
    print('A matriz possui {} numero(s) menor(es) que zero.'.format(ContMenor))
    print('A matriz possui {} numero(s) maior(es) que zero.'.format(ContMaior))
