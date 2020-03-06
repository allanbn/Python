cont = 0
c = []
d = []
somac = 0
somad = 0
while True:
    if cont > 100:
        break
    a = input().split()
    x = int(a[0])
    if x == -1:
        break
    b = float(a[1])
    if x == 1:
        c.append(b)
    else:
        d.append(b)
    cont += 1
for i in c:
    somac += i
for i in d:
    somad += i
print('Creditos: R$ {}\nDebitos: R$ {}'.format('%.2f' % somac, '%.2f' % somad))
print('Saldo: R$ {}'.format('%.2f' % (somac - somad)))
