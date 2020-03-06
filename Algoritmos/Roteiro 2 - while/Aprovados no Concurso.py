cont = 0
nota_pt = int(input())
while nota_pt > 0:
    nota_math = int(input())
    nota_red = float(input())
    if (nota_pt >= (50 * 0.8)) and (nota_math >= (35 * 0.6)) and (nota_red >= 7):
        cont += 1
    nota_pt = int(input())
print(cont)
