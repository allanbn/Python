a = int(input())
b = int(input())
soma = 0
if a > b:
    fixo = a
    mutavel = a
    while mutavel > 0:
        mutavel -= 1
        soma = fixo + mutavel
        fixo = mutavel
        fixo = soma
    print(soma)
else:
    fixo = b
    mutavel = b
    while mutavel > 0:
        mutavel -= 1
        soma = fixo + mutavel
        fixo = mutavel
        fixo = soma
    print(soma)
