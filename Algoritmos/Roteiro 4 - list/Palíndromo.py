n = int(input())
for a in range(1, n + 1):
    b = input()
    b = b.replace(' ', '')
    if b.lower()[:] == b.lower()[::-1]:
        print('SIM')
    else:
        print('NAO')
