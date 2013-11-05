# 1)

def DecToBin(nombre):
    if nombre == 0:
        return [0]
    else:
        retour = []
        while nombre > 0:
            quotient = nombre//2
            reste = nombre%2
            retour.append(reste)
            nombre = quotient
        return retour[::-1]
        
print(DecToBin(42))

# 3)

def BinToDec(liste):
    retour = 0
    liste = liste[::-1]
    for i in range(len(liste)):
        if liste[i] == 1:
            retour += 2**i
    return retour
    
print(BinToDec([1, 0, 1, 0, 1, 0]))