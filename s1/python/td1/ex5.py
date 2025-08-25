T=int(input("Entrez le nombre en seconde : "))
H=T//3600
M=(T%3600)//60
S=T%60
print(f"C'est equivalent à {H} heures, {M} minutes et {S} secondes")