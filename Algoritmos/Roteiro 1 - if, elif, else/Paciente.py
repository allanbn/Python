t = float(input())
stdc = str(input())
e = ['S', 'N']
if t >= 37.00 and stdc == e[0]:
    print('Exames Especiais')
elif t >= 37.00 and stdc == e[1]:
    print('Liberado')
elif t < 37.00 and stdc == e[1]:
    print('Liberado')
elif t < 37.00 and stdc == e[0]:
    print('Exames Basicos')
elif stdc != e:
    print('Erro')
else:
    print('Exames Basicos')
