n = int(input())
a = 1
if 1 <= n <= 20:
    while a <= n:
        for i in range(1, n + 1):
            print(str(a)*a)
            a += 1
