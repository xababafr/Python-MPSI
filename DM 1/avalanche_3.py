from math import *
from random import *
import time

Montagne = [ 8 , 5 , 4 , 3 , 2 , 1 , '!' ]
#Montagne = ['!', 2, 8, 2, '!']
#Montagne = [ 4 , 5 , '!' ]
#Montagne = ['!', 8, '!']
#Montagne = ['!', 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, '!']

# une seule obligation a ce format : un '!' a la fin
# cependant, l'avantage est de pouvoir en mettre ailleurs
# on suppose aussi que la montagne fait au moins une colonne d'epaiseur

# compteur principal de carres ejectes

compteur = 0

def colonne_instable(montagne):

	""" retourne le numero de la premiere colonne de rochers
		instables reperee, en partant de la gauche.
		S'il n'y a pas de colonnes instables, renvoi False. """

	length = len(montagne)

	# si la difference de hauteur est de deux, la colonne est instable
	for i in range(1,length):

		precedente = Montagne[i-1]
		actuelle = Montagne[i]

		if precedente == -1:
			precedente = 0
		if actuelle == -1:
			actuelle = 0

		# 1er cas : si la colonne actuelle est plus grande
		# (de 2 carres ou + ) que la precedente
		if actuelle-precedente > 2 :
			#print("cas 1",actuelle-precedente)
			return i # dans ce cas elle est instable
		# 2eme cas : si la colonne actuelle est plus petite
		# (de 2 carres ou + ) que la precedente
		elif actuelle-precedente < -2 : 
			#print("cas 2")
			return i-1  # dans ce cas celle d'avant est instable

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
		# si a gauche et ou a droite il y a un contener '!', cela veut dire
		# qu'il y a 0 cubes
		# a reecrire plus tard, c'est degueu
		# pour le moment l'important c'est que sa marche
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

def effondrement(montagne,rang):

	""" effectue l'effondrement de la colonne dont le numero
		est specifie en parametre. Si le cube atteint un '!',
		il est ejecte et comptabilise tel quel. """

	global compteur

def affichage(montagne):

	""" fonction qui retourne l'aspect visuel de la montagne
		passee en parametre. """

	affichage =  '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
	affichage += '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
	#affichage += '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

	# 1) on remplace les '!' par des -1
	for i in range(len(montagne)):
		if montagne[i] == '!':
			montagne[i] = -1

	# maintenant la liste n'a que des nombres/chiffres

	# 2) puis on parcours du plus grand element au plus petit
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


##### BOUCLE PRINCIPALE #####

print(affichage(Montagne))

# tant que la structure globale est instable
while colonne_instable(Montagne) is not False :

	time.sleep(1)

	colonne = colonne_instable(Montagne)
	rang = choix(Montagne,colonne)

	Montagne[colonne] -= 2
	if Montagne[rang] == -1:
		compteur += 2
	else :
		Montagne[rang] += 2

	print(affichage(Montagne))

print("compteur",compteur)
