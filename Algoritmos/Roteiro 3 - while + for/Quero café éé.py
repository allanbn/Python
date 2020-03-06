contp = 0
contg = 0
for i in range(1, 8):
    caixas = int(input())
    tipo_caixa = input()
    if tipo_caixa == 'p' or tipo_caixa == 'P':
        contp += caixas
    else:
        contg += caixas
total = ((contp * 10) + (contg * 16))
print('{}\n{}'.format(total, ((total // 7) * 2)))
