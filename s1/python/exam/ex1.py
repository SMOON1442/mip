while(True):
    n=int(input("Entrez un nombre entier: "))
    if n > 0:
        break
s=0
t=[]
while(n>0):
    s+=1
    t.append(n%10)
    n=n//10
print(f"nombre est composé de {t}, le nombre des chiffres est : {s}")