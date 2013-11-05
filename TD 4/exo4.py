# exercice 4)

def DecToBin(n):
    retour = [0,0,0,0,0,0,0,0]
    if(n == 0):
        retour.append(0)
    
    j = 0
    while n > 0:
    
        i = 0

        print(j+1)
    
        # on cherche la puissance de 2 < ou = a n
        while 2**i <= n:
            i += 1
    
        # on soustrait la puissance de 2 obtenue
        n -= 2**(i-1)
        retour[i] = 1
        
        print(n)
        print("----")
    
        # puis on continue tant que n est > 0
        
        j += 1
    
    return retour

print(DecToBin(42))
    