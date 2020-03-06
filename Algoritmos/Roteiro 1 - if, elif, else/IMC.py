m = float(input())
a = float(input())
v = m / a ** 2
if 0.00 <= m <= 500.00 and 0.00 <= a <= 2.8:
    print(round(v, 2))
