n = int(input())
for i in range(n):
    fraseM = ''
    string = input()
    for i in range(len(string)):
        if i == 0:
            fraseM = string[i].upper()
            continue
        if string[i - 2] == '.' and string[i - 1] == ' ':
            fraseM += string[i].upper()
        else:
            fraseM += string[i]
    print(fraseM)
