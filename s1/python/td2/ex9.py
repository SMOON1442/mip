while(True):
    a=int(input("Entrez le premier nombre : "))
    b=int(input("Entrez le deuxieme nombre : "))
    if a>0 and b>0:
        break
if a>b:
    a,b=b,a
for n in range(a,b):
    x=n
    s=0
    while(n>0):
        s=s+((n%10)**3)
        n=n//10
    if s==x:
        print(x, "est cubique")