r = float(input())
a = float(input())
pi = 3.14
l = (a * pi * r) / 180
z = pi * (r ** 2) * (a / 360)
print('{}\n{}'.format(round(l, 2), round(z, 2)))
