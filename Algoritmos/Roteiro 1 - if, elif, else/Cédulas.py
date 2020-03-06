a = int(input())
z = a
cem = cinquenta = vinte = dez = cinco = dois = um = 0
if int(a/100) >= 1:
    cem = int(a/100)
    a -= cem*100
if int(a/50) >= 1:
    cinquenta = int(a/50)
    a -= cinquenta*50
if int(a/20) >= 1:
    vinte = int(a/20)
    a -= vinte*20
if int(a/10) >= 1:
    dez = int(a/10)
    a -= dez*10
if int(a/5) >= 1:
    cinco = int(a/5)
    a -= cinco*5
if int(a/2) >= 1:
    dois = int(a/2)
    a -= dois*2
if int(a/1) >= 1:
    um = int(a/1)
    a -= um*1
print("%d" % z)
print("%d nota(s) de R$ 100,00" % cem)
print("%d nota(s) de R$ 50,00" % cinquenta)
print("%d nota(s) de R$ 20,00" % vinte)
print("%d nota(s) de R$ 10,00" % dez)
print("%d nota(s) de R$ 5,00" % cinco)
print("%d nota(s) de R$ 2,00" % dois)
print("%d nota(s) de R$ 1,00" % um)
