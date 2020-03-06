n = int(input())
a = 1
b = 4
un = 0.0
saida = ''
for i in range(1, n + 1):
    if i % 2 == 1:
        un += (a / b)
        saida += str(a) + '/' + str(b)
        a += 1
        b += 2
    if i % 2 == 0:
        un += 1
        saida += '1'
        a += 1
        b += 2
    if i < n:
        saida += ' + '
print(round(un, 2))
print(saida)
