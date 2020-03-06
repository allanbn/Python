while True:
    z = 1
    total = 1
    n = int(input())
    if n < 0:
        break
    while z <= n:
        total *= z
        z += 1
    print(total)
