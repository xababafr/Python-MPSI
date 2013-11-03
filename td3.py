from math import *

# les deux listes a additionner
# on les suppose de meme taille
L = [0, 0, 1, 0, 1, 1, 0, 1]
M = [0, 1, 0, 1, 1, 1, 0, 1]

# la liste reponse
R = [0, 0, 0, 0, 0, 0, 0, 0]

retenue = 0

# on parcours la premiere liste dans le sens inverse
for i in reversed(range(len(L))):
    # somme des deux cases + l eventuelle retenue
    valeur = L[i] + M[i] + retenue

    # on peut remettre la retenue a 0
    retenue = 0

    # si la valeur vaut 2 ou 3, on met une retenue
    # sinon on met juste la valeur de la somme
    if valeur < 2:
        R[i] = valeur
    else:
        R[i] = valeur%2
        retenue = 1

print L,"+",M,"=",R