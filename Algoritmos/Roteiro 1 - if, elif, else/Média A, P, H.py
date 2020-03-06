a = str(input())
if a == 'a':
    a = int(input())
    b = int(input())
    c = int(input())
    d = (a + b + c) / 3
    if 0 <= d <= 40:
        print('{}\nReprovado'.format(round(d, 2)))
    elif 40 <= d <= 70:
        print('{}\nFinal'.format(round(d, 2)))
    elif 70 <= d <= 100:
        print('{}\nAprovado'.format(round(d, 2)))
    else:
        print('Media invalida')
elif a == 'p':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    f = int(input())
    g = ((a * d) + (b * e) + (c * f)) / (d + e + f)
    if 0 <= g <= 40:
        print('{}\nReprovado'.format(round(g, 2)))
    elif 40 <= g <= 70:
        print('{}\nFinal'.format(round(g, 2)))
    elif 70 <= g <= 100:
        print('{}\nAprovado'.format(round(g, 2)))
    else:
        print('Media invalida')
elif a == 'h':
    a = int(input())
    b = int(input())
    c = int(input())
    d = 3 / (1/a + 1 / b + 1/c)
    if 0 <= d <= 40:
        print('{}\nReprovado'.format(round(d, 2)))
    elif 40 <= d <= 70:
        print('{}\nFinal'.format(round(d, 2)))
    elif 70 <= d <= 100:
        print('{}\nAprovado'.format(round(d, 2)))
    else:
        print('Media invalida')
else:
    print('Escolha um tipo de media valida.')
