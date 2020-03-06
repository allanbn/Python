nome = input()
print(nome[-1].upper() + nome[1:len(nome) - 1].lower()[::-1] + nome.upper()[0])
