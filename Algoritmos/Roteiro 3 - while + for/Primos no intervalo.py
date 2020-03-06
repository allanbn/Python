cont = 0
a = int(input())
b = int(input())
if a > b:
    z = a
    while z >= b:
        for i in range(a, b - 1, -1):
            primo = z % i
            if primo == 0:
                cont += 1
            if z % 2 == 0 and z != 2:
                z -= 1
            if z % 3 == 0 and z != 3:
                z -= 1
            if z % 5 == 0 and z != 5:
                z -= 1
            if z % 7 == 0 and z != 7:
                z -= 1
            if z == 1:
                z -= 1
                break
            if cont == 2:
                print(z)
                z -= 1
                cont = 0
else:
    z = b
    while z >= a:
        for i in range(b, a - 1, -1):
            primo = z % i
            if primo == 0:
                cont += 1
            if z % 2 == 0 and z != 2:
                z -= 1
            if z % 3 == 0 and z != 3:
                z -= 1
            if z % 5 == 0 and z != 5:
                z -= 1
            if z % 7 == 0 and z != 7:
                z -= 1
            if z == 1:
                z -= 1
                break
            if cont == 2:
                print(z)
                z -= 1
                cont = 0
