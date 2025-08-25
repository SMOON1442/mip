while(True): 
    n = int(input("Entrez la taille : "))
    if n >= 2:
        break
s=0
a= int(input("Entrez votre nombre : "))
t = []
for i in range(0,n):
    t.append(int(input("Entrez une valeur : ")))
    if t[i] == a:
        s=s+1
print(f"Votre nombre occure {s} fois")