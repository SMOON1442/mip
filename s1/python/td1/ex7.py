n=float(input("Entrez la note : "))
if n<0 or n>20:
    print("nombre invalide")
elif n>=16:
    print("Très bien")
elif n>=14:
    print("Bien")
elif n>=12:
    print("Assez bien")
elif n>=10:
    print("Passable")
else:
    print("Non admis")