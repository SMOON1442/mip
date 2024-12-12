while(True):
    n=int(input("Entrez la taille du tableau : "))
    if n>0:
        break
t=[]
for i in range(0,n):
    t.append(int(input("Entrez une valeur : ")))
    print(t)
for i in range(0, n//2):
    t[i],t[n-i-1]=t[n-i-1],t[i]
print(t)