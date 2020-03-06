m = int(input())
n = int(input())
z = 1
d = 1
if m < n:
    while d <= n:
        d = m * z
        z += 1
    if d > n:
        print(d-m)
    elif d == n:
        print(d)
else:
    print('sem multiplos menores que {}'.format(n))
