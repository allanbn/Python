def _pow(x, n):
    p = 1
    if n == 0:
        return 1
    if x == 2:
        p = p << n
        return p
    else:
        y = _pow(x, n//2)
        if n%2 == 1:
            return x * y * y
        else:
            return y * y


def main():
    x = int(input())
    n = int(input())

    print(_pow(x, n))

if __name__ == "__main__":
    main();