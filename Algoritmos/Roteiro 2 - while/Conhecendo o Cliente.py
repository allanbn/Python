quantidade_vendas = 0
total_vendas_cartao = 0
total_vendas_vista = 0
mais_jovem = 0
maior_compra = 0
soma = 0
conti = 'S'
cont = 0
contv = 0
while conti == 'S':
    idade = int(input())
    valor = float(input())
    tipo = input()
    if cont == 0:
        mais_jovem = idade
        maior_compra = valor
    elif idade < mais_jovem:
        mais_jovem = idade
    if tipo == 'V':
        contv += 1
        total_vendas_vista += valor
    else:
        total_vendas_cartao += valor
    if valor > maior_compra:
        maior_compra = valor
    cont += 1
    quantidade_vendas += 1
    conti = input()
if contv == 0:
    print(quantidade_vendas)
    print(round(total_vendas_vista, 2))  # float
    print(round(total_vendas_cartao, 2))  # float
    print(mais_jovem)
    print(round(maior_compra, 2))  # float
    print(contv)
else:
    print(quantidade_vendas)
    print(round(total_vendas_vista, 2))  # float
    print(round(total_vendas_cartao, 2))  # float
    print(mais_jovem)
    print(round(maior_compra, 2))  # float
    print(round((total_vendas_vista / contv), 2))  # float
