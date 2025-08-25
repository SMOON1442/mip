a=float(input("Entrez le premier nombre : "))
b=float(input("Entrez le deuxieme nombre : "))
if a==0 or b==0:
    print("Le produit est nul")
elif (a>0 and b>0) or (a<0 and b<0):
    print("Le produit est positif")
else:
    print("Le produit est negatif")