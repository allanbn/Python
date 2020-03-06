import math
def Result(A):
    Resultados = []
    for i in range(A):
        Total = math.factorial(i) / math.sqrt(2 * i + 1)
        Resultados.append(Total)
    return Resultados
def Total(A):
    Soma = math.factorial(A) / math.sqrt(2 * A + 1)
    return Soma
N = int(input())
lista = Result(N)[::-1]
del lista[-1]
print('S:', ('%.12f' % (Total(N) + sum(lista))))
if len(lista) == 0:
    print('%.12f' % (Total(N) + sum(lista)))
else:
    for i in lista:
        print('%.12f' % i)
