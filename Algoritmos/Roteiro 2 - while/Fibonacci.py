a = 0
b = a
cont = 0
saida = ''
n = int(input())
while cont < n:
    saida += str(a)
    if cont < (n - 1):
        saida += ' '
    soma = a + b
    b = a
    a = soma
    if a == 0:
        a = 1
    cont += 1
    if n == 0:
        n = int(input())
        saida = ''
    if cont == n:
        print(saida)
        n = int(input())
        if n > 0:
            cont = 0
            saida = ''
            a = 0
            b = a
