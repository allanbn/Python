a = str(input())
b = float(input())
c = str(input())
d = str(input())
f = b / 2
e = b / 3
g = b * 3
i = b * 2
dia = ['seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
produto = ['prata', 'ouro']
if a in dia[0:3] and c in produto[1]:
    print('O preco do produto {} no dia {} eh {}'.format(d, a, round(f, 2)))
elif a in dia[3:5] and 10.00 <= b <= 100 and c in produto:
    print('O preco do produto {} no dia {} eh {}'.format(d, a, round(e, 2)))
elif a in dia[5] and c in produto[0]:
    print('O preco do produto {} no dia {} eh {}'.format(d, a, round(g, 2)))
else:
    print('O preco do produto {} no dia {} eh {}'.format(d, a, round(i, 2)))
