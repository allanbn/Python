ano = int(input())
qntd = int(input())
cont = 3
saida = ''
while cont > 0:
    ano += qntd
    if cont > 0:
        saida += str(ano)
        cont -= 1
        saida += ' '
print(saida)
