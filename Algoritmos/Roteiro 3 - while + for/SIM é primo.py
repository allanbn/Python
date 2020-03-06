cont = 0
n = int(input())
for i in range(1, n + 1):
    primo = n % i
    if primo == 0:
        cont += 1
if cont == 2:
    print('SIM')
    cont = 0
else:
    print('NAO')
    cont = 0
