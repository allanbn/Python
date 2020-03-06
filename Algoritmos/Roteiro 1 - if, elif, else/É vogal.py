z = input()
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if z in vogais:
    print('Eh vogal')
elif len(z) > 1:
    print('1 caractere, por favor!')
else:
    print('Nao eh vogal')
