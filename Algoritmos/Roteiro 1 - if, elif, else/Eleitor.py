a = int(input())
if a <= 15:
    print('nao eleitor')
elif 18 <= a <= 65:
    print('eleitor obrigatorio')
else:
    print('eleitor facultativo')
