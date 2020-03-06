n = int(input())
m = int(input())
if n % 2 == 1:
    while m >= n:
        print(n)
        n = n + 2
elif n % 2 == 0:
    n += 1
    while m >= n:
        print(n)
        n = n + 2
else:
    print('SEM RESPOSTA')