while(True):
    n=int(input("Entrez la taille du tableau : "))
    if n >= 2:
        break
t=[]
m=n
d=True
for i in range(0,n):
    t.append(int(input("Entrez une valeur : ")))
    print(t)
while(d==True):
    d=False
    for i in range(0,m-1):
        if t[i]>t[i+1]:
            t[i],t[i+1]=t[i+1],t[i]
            d=True 
    m=m-1
print(t)