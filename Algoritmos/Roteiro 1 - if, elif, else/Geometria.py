a = str(input())
pi = 3.14
if a == 'Q':
    b = float(input())
    z = b ** 2
    print('{}\n{}'.format(round(z, 2), round(b * 4, 2)))
elif a == 'R':
    b = float(input())
    h = float(input())
    a = b * h
    c = (b * 2) + (h * 2)
    print('{}\n{}'.format(round(a, 2), (round(c, 2))))
elif a == 'C':
    a = float(input())
    b = pi * (a ** 2)
    c = 2 * pi * a
    print('{}\n{}'.format(round(b, 2), (round(c, 2))))
else:
    print('Nenhuma figura selecionada')
