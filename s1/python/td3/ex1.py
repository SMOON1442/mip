while(True): 
    n = int(input("Entrez la taille : "))
    if n > 0:
        break
t = []
t.append(float(input("Entrez la premiere valeur du tableau : ")))
min = max = t[0]
for i in range(0,n):
    j = float(input("Entrez une valeur : "))
    t.append(j)
    if j > max:
        max = 0
        max += j
    if j < min:
        min = 0
        min += j
print(f"min est {min} et max est {max}")