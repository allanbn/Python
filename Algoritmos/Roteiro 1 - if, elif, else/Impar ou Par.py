a = int(input())
if a > 0 and a % 2 == 0:
    print('POSITIVO PAR\n')
elif a < 0 and a % 2 == 0:
    print('NEGATIVO PAR\n')
elif a > 0 and a % 2 == 1:
    print('POSITIVO IMPAR\n')
elif a < 0 and a % 2 == 1:
    print('NEGATIVO IMPAR\n')
else:
    print('NULO\n')
