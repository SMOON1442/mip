while(True):
    n=int(input("Entrez la taille du tableau : "))
    if n >= 2:
        break
t=[]
for i in range(0,n):
    t.append(int(input("Entrez une valeur : ")))
    print(t)
for i in range(0,n-1):
    imin=i
    for j in range(i+1,n):
        if(t[j]<t[imin]):
            imin=j
    if imin!=i:
        t[imin],t[i]=t[i],t[imin]
print(t) 