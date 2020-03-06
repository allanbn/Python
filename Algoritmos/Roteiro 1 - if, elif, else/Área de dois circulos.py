a = float(input())
b = float(input())
pi = 3.14
x = pi * (a ** 2)
z = pi * (b ** 2)
if x > z:
    print('Primeiro circulo')
elif z > x:
    print('Segundo circulo')
else:
    print('Iguais')
