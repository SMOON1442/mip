while(True):
    n=int(input("Entrez la taille du tableau : "))
    if n > 0:
        break
t=[]
for i in range(0, n):
    t.append(int(input("Entrez une valeur : ")))
    temp = i
    for j in range(i+1, n):
        if temp > t[j]:
            temp=j
    
    
        
