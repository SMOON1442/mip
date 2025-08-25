a=int(input("Entrez le nombre de photocopie(s) demandé : "))
if a>=1 and a<10:
    prix=a*0.5
elif a<20:
    prix=a*0.4
else:
    prix=a*0.3
print("Le prix à payer est : ",prix)