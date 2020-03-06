def LMInt(L = []):
    for x in range(len(L)):
        L[x] = int(L[x])
    return L
ordem = int(input())
Matriz = []
Diagonal = []
for i in range(ordem):
        Elementos = input().split()
        Matriz.append(LMInt(Elementos))
for i in range(len(Matriz)):
    for j in range(len(Matriz)):
        if i == j:
            Diagonal.append(Matriz[i][j])
resultado = ''
for i in range(len(Diagonal)):
    if i == 0:
        resultado = 'tr(A) = (' + '%.2f' % Diagonal[i] + ')'
    else:
        resultado += ' + (' + '%.2f' % Diagonal[i] + ')'
resultado += ' = ' + '%.2f' % sum(Diagonal)
print(resultado)
