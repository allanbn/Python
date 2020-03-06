a = int(input())
b = int(input())
c = int(input())
multiplicador = 1
d = 0
if a > c:
    print('INEXISTENTE')
else:
    while c >= d:
        d = a * multiplicador
        if b < d <= c:
            print(d)
        multiplicador += 1
