a = int(input())
b = int(input())
c = int(input())
if a != b and b == c:
    print('A\n')
elif b != c and c == a:
    print('B\n')
elif c != a and a == b:
    print('C\n')
else:
    print('*\n')
