a = int(input())
if a == 1:
    print('Nordeste')
elif a == 2:
    print('Norte')
elif a == 3 or a == 4:
    print('Centro-Oeste')
elif 5 <= a <= 9:
    print('Sul')
else:
    print('Sudeste')
