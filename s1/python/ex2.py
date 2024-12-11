while(True): 
    n = int(input("Entrez la taille : "))
    if n >= 2:
        break
s=0
t = []
for i in range(0,n):
    t.append(int(input("Entrez une valeur : ")))
    if t[i]%2 == 1:
        s=s+1
print("Le nombre des élements impaires est : ", s)