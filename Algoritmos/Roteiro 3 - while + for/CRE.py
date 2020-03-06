cont = 0
am = ''
bm = 0
media = 0
while True:
    a = input()
    if a == '999':
        break
    b = float(input())
    media += b
    if cont == 0:
        am = a
        bm = b
    if b < bm:
        bm = b
        am = a
    cont += 1
print('{}\n{}'.format(am, '%.2f' % (media / cont)))
