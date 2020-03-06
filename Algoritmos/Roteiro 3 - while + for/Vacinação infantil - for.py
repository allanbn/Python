ano = int(input())
qntd = int(input())
saida = ''
for i in range(0, 3):
    ano += qntd
    saida += str(ano)
    saida += ' '
print(saida)
