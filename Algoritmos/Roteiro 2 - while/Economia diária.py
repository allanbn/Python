valor_anterior = 0
valort = 0
cont = 0
cont2 = 0
while cont2 < 7:
    valor = float(input())
    if valor_anterior == 0:
        valor_anterior = valor
    elif valor >= valor_anterior + 0.5:
        valor_anterior = valor
        cont += 1
    if valor < valor_anterior:
         valor_anterior = valor
    cont2 += 1
    valort += valor
print('R$ {}\n{}'.format('%.2f' % valort, cont))
