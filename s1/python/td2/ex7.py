while(True):
    p=int(input("Entrez un nombre: "))
    if p>=2:
        break
premier=True
for i in range(2,p):
    if p%i==0:
        premier=False
        break
if premier==True:
    print(p, "est un nombre premier")
else:
    print(p, "n'est pas un nombre premier")