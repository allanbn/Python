n = int(input())
z = 1
if 1 <= n <= 1000:
    while z <= n:
        b = z ** 2
        c = z ** 3
        print(z, b, c)
        z += 1
