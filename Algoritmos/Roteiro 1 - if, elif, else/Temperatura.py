a = str(input())
t = float(input())
cf = t * 1.8 + 32  # C para F
fc = (t - 32) / 1.8  # F pra C
ck = t + 273.00  # C para K
kc = t - 273.00  # K para C
fk = fc + 273.00  # F para Kelvin
kf = t * 1.8 - 459.40  #  K para F
e = ['C', 'F', 'K']
if a == e[0] and t >= -273.00:
    print('{} F\n{} K'.format('%.1f' % cf, '%.1f' % ck))
elif a == e[1] and t >= -459.67:
    print('{} C\n{} K'.format('%.2f' % fc, '%.2f' % fk))
elif a == e[2] and t >= 0.0:
    print('{} C\n{} F'.format('%.1f' % kc, '%.1f' % kf))
elif a not in e:
    print('Escala invalida')
else:
    print('Valor de temperatura abaixo do minimo')
