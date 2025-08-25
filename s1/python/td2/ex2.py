a=int(input("Entrez le premier nombre : "))
b=int(input("Entrez le deuxieme nombre : "))
if a>b:
    a,b=b,a
for i in range(a,b):
    if i%2==0:
        print(i)
