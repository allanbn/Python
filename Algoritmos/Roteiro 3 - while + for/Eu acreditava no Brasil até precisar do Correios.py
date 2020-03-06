cont = 0
total = 0
for i in range(1, 8):
    n = int(input())
    total += n
    if n >= 100:
        cont += 1
print('{}\n{}'.format(cont, total // 7))
