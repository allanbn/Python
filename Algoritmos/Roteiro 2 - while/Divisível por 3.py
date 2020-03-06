cont = 0
i = 1
n = int(input())
while i <= n:
	a = n % i
	if a == 0:
		b = i % 3
		if b == 0:
			cont += 1
	i += 1
if cont == 0:
	print('O numero nao possui divisores multiplos de 3!')
else:
	print(cont)
