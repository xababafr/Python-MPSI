from math import *
from random import *
import time

""" 
La montagne est representee par une liste.
 Chaque element de la liste represente une colonne
 de carres. Le chiffre corresponds donc a la hauteur
 de chaque colonne.
 Le '!' represente la surface sur laquelle 
 s'empilent les carres ejectes. La montagne 
 peut d'ailleurs en comporter plusieurs.
La montagne initiale est supposee stable, puis
l'utilisateur doit rentrer a l'execution du programme
une liste (de la taille de la montagne), chaque valeur
correspondant au nombre de cube a ajouter pour la colonne
concernee.
Donc, [1,1,1,1] rajoutera un cube de hauteur a une montagne
de 4 colonnes de longueur.
Puis, le programme procede a l'avalanche, si les chutes de neige
ont rendu la montagne instable. 
"""

Montagne = [ 6 , 5 , 4 , 3 , 2 , 1 , '!' ]

# compteur principal de carres ejectes
compteur = 0


#### FONCTIONS AUXILLIAIRES ####

def chute(montagne,chutes):

	""" retourne la Montagne, apres avoir effectue a l'enneigement
		correspondant aux valeurs de la liste chutes. """

	# on ne procede que si c'est evidemment possible
	if len(chutes) != len(montagne)-1:
		return False
	else:
		# on rajoute les elements de la liste chutes a la montagne
		for i in range(len(montagne)-1):
			montagne[i] += chutes[i]
		return montagne


def colonne_instable(montagne):

	""" retourne le numero de la premiere colonne de rochers
		instables reperee, en partant de la gauche.
		S'il n'y a pas de colonnes instables, renvoi False. """

	length = len(montagne)

	# si la difference de hauteur est de deux, la colonne est instable
	for i in range(1,length):

		precedente = Montagne[i-1]
		actuelle = Montagne[i]

		# on considere les '!' comme des colonnes de hauteur nulle
		if precedente == -1:
			precedente = 0
		if actuelle == -1:
			actuelle = 0

		# 1er cas : si la colonne actuelle est plus grande
		# (de 2 carres ou + ) que la precedente
		if actuelle-precedente > 2 :
			return i
		# 2eme cas : si la colonne actuelle est plus petite
		# (de 2 carres ou + ) que la precedente
		elif actuelle-precedente < -2 : 
			return i-1

	return False # sinon on retourne False


def choix(montagne,rang):

	""" fonction qui a une colonne instables donnee, retourne l'indice
		de la colonne qui doit gagner deux unites (celle de gauche ou
		celle de droite). """

	length = len(montagne)

	# si on n'est pas tout a gauche, on fait un choix normal
	if rang != 0 : 
		gauche = montagne[rang-1]
		droite = montagne[rang+1]

		# une fois encore, on considere les '!' comme des 0
		if gauche == '!':
			gauche = 0
		if droite == '!':
			droite = 0

		# si il y a une denivelation + importante d'un cote comme de l'autre
		if gauche != droite :
			if gauche < droite :
				choix = rang-1
			else :
				choix = rang+1
		# ou si la denivelation est la meme de chaque cote
		else :
			nbr = choice([-1,1])
			choix = rang+nbr
	# sinon, c'est forcement a droite que l'on procede a l'effondrement
	else :
		choix = rang+1

	# on retourne le rang de la colonne qui doit recevoir les 2 unites
	return choix


def affichage(montagne):

	""" fonction qui retourne l'aspect visuel (en texte) 
		de la montagne passee en parametre.  """

	affichage = ''

	# 1) on remplace les '!' par des -1
	for i in range(len(montagne)):
		if montagne[i] == '!':
			montagne[i] = -1

	# maintenant la liste n'a que des nombres/chiffres

	# 2) puis on parcours du plus grand element au plus petit
	#    en affichant lr bloc correspondant
	maxi = max(montagne)
	for i in reversed(range(maxi+1)):
		for j in montagne :
			if j > i :
				affichage += ' *'
			else :
				affichage += '  '
		affichage += '\n'
	for k in montagne:
		if k == -1:
			affichage += ' _'
		else :
			affichage += '  '

	return affichage


def visuel_neige(chutes,marge):

	""" fonction qui retourne l'aspect visuel de la chute de neige """

	affichage = ''
	maxi = max(chutes)+marge-1
	for i in range(maxi+1):
		for j in chutes:
			if j > i:
				affichage += ' *'
			else:
				affichage += '  '
		affichage += '\n'

	return affichage


print(affichage(Montagne))

# un gros saut de lignes pour donner l'illusion du mouvement
lignes = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
lignes += '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
lignes += '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

chutes = input("rentrez l'importance de la chute de neige [] : ")

# on affiche la neige au dessu de la montagne
# mais avec une marge de + en + faible
# ( la neige tombe donc se rapproche )
for i in reversed(range(4)):
	neige = visuel_neige(chutes,i)
	print(lignes+neige+affichage(Montagne))
	time.sleep(1)

# puis on prends la valeur de la montagne apres la chute
Montagne = chute(Montagne, chutes)
print(lignes+affichage(Montagne))

# et on entre dans la : 

##### BOUCLE PRINCIPALE (avalanche) #####

# tant que la structure globale est instable
while colonne_instable(Montagne) is not False :

	# on pause le programme pour une seconde
	time.sleep(1)

	colonne = colonne_instable(Montagne)
	rang = choix(Montagne,colonne)

	# on procede a l'effondrement
	Montagne[colonne] -= 2
	if Montagne[rang] == -1:
		compteur += 2
	else :
		Montagne[rang] += 2

	# enfin, on affiche la structure de la montagne
	print(lignes+affichage(Montagne))

# et pour conclure, on affiche le nombre de carres ejectes
print("nombre de carres ejectes : ",compteur)
