while(True):
    n=int(input("Entrez la taille du tableau : "))
    if n>0:
        break
t=[]
a=0
x=int(input("Entrez la valeur que vous voulez : "))
for i in range(0,n):
    t.append(int(input("Entrez une valeur : ")))
    if t[i]==x:
        print(i)
        a=a+1
if a==0:
    print("-1")
