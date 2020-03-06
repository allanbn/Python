cont = 0
conthomi = 0
contmule = 0
maior_salario = 0
maior_salario_sexo = ''
salariohomi = 0
salariototal = 0
while True:
    if cont == 10:
        break
    salario = int(input())
    sexo = input()
    if cont == 0:
        maior_salario = salario
        maior_salario_sexo = sexo
    if sexo == 'm':
        conthomi += 1
        salariototal += salario
        salariohomi += salario
    else:
        contmule += 1
        salariototal += salario
    if salario > maior_salario:
        maior_salario = salario
        maior_salario_sexo = sexo
    cont += 1
print(conthomi)
print(contmule)
print(round(salariototal / 10, 2))
print(maior_salario_sexo)
print(round(salariohomi / conthomi, 2))
