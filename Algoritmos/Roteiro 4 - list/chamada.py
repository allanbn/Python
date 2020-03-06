L = []
a, b = input().split()
a = int(a)
b = int(b)
for i in range(a):
    L.append(input())
L.sort()
print(L[b - 1])
