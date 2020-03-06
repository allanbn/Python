a = int(input())
b = int(input())
c = int(input())
if a <= b <= c:
    print('{}\n{}\n{}\n'.format(a, b, c))
elif a <= c <= b:
    print('{}\n{}\n{}\n'.format(a, c, b))
elif c <= a <= b:
    print('{}\n{}\n{}\n'.format(c, a, b))
elif c <= b <= a:
    print('{}\n{}\n{}'.format(c, b, a))
elif b <= c <= a:
    print('{}\n{}\n{}'.format(b, c, a))
else:
    print('{}\n{}\n{}'.format(b, a, c))
