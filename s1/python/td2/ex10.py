while(True):
    a = int(input("Entrez un nombre entier : "))
    if a > 0:
        break
x=0
for i in range(1,a+1):
    x=x+i
    print(x)
    x=x*10