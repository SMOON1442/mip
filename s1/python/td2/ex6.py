b=5 #un nombre quelconque de votre choix
while(True):
    a=int(input("Entrez un nombre entre 1 et 20: "))
    if a<=1 and a>=20:
        continue
    while(a!=b):
        if a>b:
            print("nombre deviné est trop grand")
        elif a<b:
            print("nombre deviné est trop petit")
        else:
            break
        a=int(input("Entrez un nombre entre 1 et 20 : "))
    break
print("Vous avez trouvez le nombre!")