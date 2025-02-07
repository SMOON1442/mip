#this may not be the exact same exercice but the concept is the same
while(True):
    n=int(input("Entrez un nombre entier : "))
    if n>0:
        break
if n < 1000:
    print(f"le montant à payer est {n*0.1} DHs")
elif n < 5000:
    print(f"le montant à payer est {n*0.2} DHs")
elif n < 10000:
    print(f"le montant à payer est {n*0.3} DHs")
else:
    print(f"le montant à payer est {n*0.5} DHs")