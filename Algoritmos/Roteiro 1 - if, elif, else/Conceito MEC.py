li = int(input())
a = int(input())
c = li / a
if c >= 0.125:
    print('A')
elif 0.083 <= c <= 0.12:
    print('B')
elif 0.055 <= c <= 0.078:
    print('C')
elif c < 0.55:
    print('D')
