cont = 0
while True:
    n = int(input())
    if n < 0:
        break
    for i in range(1, n + 1):
        primo = n % i
        if primo == 0:
            cont += 1
    if cont == 2:
        print('1')
        cont = 0
    else:
        print('0')
        cont = 0
