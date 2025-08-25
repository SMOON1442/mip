while(True):
    n=int(input("Entrez un nombre entier : "))
    if n > 0:
        break
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(".", end="")
    for k in range(1, 2*(i)):
        print("*", end="")
    for j in range(1, n-i+1):
        print(".", end="")
    print()