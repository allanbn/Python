a, b = input().split(' ')
a = int(a)
b = int(b)
if a == b:
    if a % 4 % 100 % 400 == 0:
        print('{}\n'.format(a))
    else:
        print('-1\n')
elif a + 2 >= b:
    print('-1\n')
elif a < b:
    c = a
    if c <= b:
        while c <= b:
            if a % 4 % 100 % 400 == 0:
                c = a
            if c > b:
                break
            print('{}\n'.format(c))
            a += 4
            if a % 4 % 100 % 400 != 0:
                a += 3
                c = a
                print('{}\n'.format(c))
                a += 4
                if c > b:
                    print('\n')
                    break
else:
    print('-1\n')
