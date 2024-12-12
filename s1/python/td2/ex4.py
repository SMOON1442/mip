while(True):
    a=int(input("Entrez 1, 2 ou 3 : "))
    n=int(input("Entrez un entier positif : "))
    if (a>0 and a<=3) and n>0:
        break
if a==1:
    s=0
    for i in range(1,n+1):
        s=s+i
    print(f"La somme de 1 jusqu'à {n} est {s}")
elif a==2:
    s=1
    for i in range(2,n+1):
        s=s*i
    print(f"Le factoriel de {n} est {s}")
else:
    s=0
    for i in range(1,n+1):
        s=s+(1/i)
    print(f"La somme harmonique de {n} est {s}")
