a = str(input())
nt = 0
mv = 0
mn = 0
v = 0
if a == 's':
    while a == 's':
        b = int(input())
        c = float(input())
        a = str(input())
        nt += 1
        v += c
        if b > mn:
            mn = b
        if c > mv:
            mv = c
    print('{}\n{}\n{}'.format('%.2f' % mv, mn, '%.2f' % (v / nt)))
else:
    print('zero')
