a = int(input())
b = int(input())
c = int(input())
d = (a + b + c) / 3
if 70 <= d <= 100:
    print('A media do aluno foi {} e ele foi APROVADO'.format('%.2f' % d))
elif 0 <= d <= 40:
    print('A media do aluno foi {} e ele foi REPROVADO'.format('%.2f' % d))
elif 40 <= d < 70:
    print('A media do aluno foi {} e ele foi FINAL'.format('%.2f' % d))
else:
    print('Media invalida')
