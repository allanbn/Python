a = 1
nome = input()
while a < len(nome):
    for i in range(1, len(nome) + 1):
        print(nome.upper()[0:a])
        a += 1
