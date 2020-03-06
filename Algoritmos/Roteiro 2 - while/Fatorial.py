a = int(input('Digite um numero inteiro:'))
z = 1
total = 1
if a >= 0:
    while z <= a:
        total *= z
        z += 1
    print('\nFatorial:', total)
else:
    print('\nFatorial: -1')
