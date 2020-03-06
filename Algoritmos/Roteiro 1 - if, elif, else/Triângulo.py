a = int(input())
b = int(input())
c = int(input())
if a + b < c or c + a < b or b + c < a:
    print('Nao eh triangulo')
elif a != b and b != c and a != c:
    print('Escaleno')
elif a == b and a != c or a == c and a != b or b == c and b != a:
    print('Isosceles')
else:
    print('Equilatero')
