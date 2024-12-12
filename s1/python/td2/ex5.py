while(True):
    a=int(input("Entrez le premier nombre : "))
    b=int(input("Entrez le deuxieme nombre : "))
    if a > 0 and b >= 0:
        break
for i in range(1, a + b):
    if a % i == 0 and b % i == 0:
        pgcd = i        
print(f"PGCD({a},{b})={pgcd}")
