for p in range(1,1000):
    s=0
    for n in range(1,p):
        if p%n==0:
            s=s+n
    if s==p:
        print(p, "est un nombre parfait")