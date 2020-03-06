gt = 0
cont = 0
while True:
	g = int(input())
	if g == 0:
		break
	gt += g
	cont += 1
media = gt / cont
if media < 110:
	print('Glicose Normal')
elif  110 <= media < 200:
	print('Glicose Alterada')
else:
	print('Glicose Muito Alta')
