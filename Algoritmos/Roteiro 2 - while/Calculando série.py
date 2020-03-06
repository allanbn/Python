cont = 0
termos = int(input())
ultimot = 1 / 3 + (termos - 1) * 1 / 3
a = 1
b = 3
saida = ''
while cont < termos:
    saida += str(a) + '/' + str(b)
    if cont < (termos - 1):
        saida += ' + '
    a += 1
    b += 3
    cont += 1
print(saida)
print(round(ultimot, 2))
