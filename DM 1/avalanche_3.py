from math import *
from random import *
import time

# que je suis bete ! cette structure correspondrait 
#bien mieux ! il faut tout reprendre...

Montagne = [ 8 , 5 , 4 , 3 , 2 , 1 , '!' ]

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

	# 1) on remplace les '!' par des 0
	for i in range(length):
		if montagne[i] == '!':
			montagne[i] = 0

	precedente = montagne[0]

	# si la difference de hauteur est de deux, la colonne est instable
	for i in range(1,length):
		# 1er cas : si la colonne actuelle est plus grande
		# (de 2 carres ou + ) que la precedente
		if montagne[i]-precedente > 2 :
			return i # dans ce cas elle est instable
		# 2eme cas : si la colonne actuelle est plus petite
		# (de 2 carres ou + ) que la precedente
		elif montagne[i]-precedente < -2 : 
			return i-1  # dans ce cas celle d'avant est instable
		else:
			precedente = montagne[i]
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
				#Montagne[rang-1] += 2
				choix = rang-1
			else :
				#Montagne[rang+1] += 2
				choix = rang+1
		# ou si la denivelation est la meme de chaque cote
		else :
			nbr = choice([-1,1])
			#Montagne[rang+nbr] += 2
			choix = rang+nbr
	# sinon, c'est forcement a droite que l'on procede a l'effondrement
	else :
		#print("mur")
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
	#affichage += '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
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

i = 0

print(affichage(Montagne))

print(Montagne)

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

	i += 1

	print(affichage(Montagne))

print("compteur",compteur)


#### TEST DE COLONNE_INSTABLE() ####
#print([ 8 , 5 , 4 , 3 , 2 , 1 , '!' ])
#print(colonne_instable([ 8 , 5 , 4 , 3 , 2 , 1 , '!' ]))
#print([ 6 , 7 , 4 , 3 , 2 , 1 , '!' ])
#print(colonne_instable([ 6 , 7 , 4 , 3 , 2 , 1 , '!' ]))
#print(['!', 2, 8, 2, '!'])
#print(colonne_instable(['!', 2, 8, 2, '!']))
#print([ 4 , 5 , '!' ])
#print(colonne_instable([ 4 , 5 , '!' ]))
#print([ '!', 2, 8, 2, '!'])
#print(colonne_instable([ '!', 2, 8, 2, '!']))

#### TEST DE AFFICHAGE() ####

#print(affichage([ 8 , 5 , 4 , 3 , 2 , 1 , '!' ]))
#print(affichage([5,2,'!']))
#print(affichage(['!', 2, 8, 2, '!']))

#for i in reversed(range(8)):
	#print(i)


#### TEST DE CHOIX() ####

# Montagne = [5,2,'!']
# print(Montagne)
# print(choix(0,Montagne))

# Montagne = [3,4,'!']
# print(Montagne)
# print(choix(1,Montagne))

# Montagne = [2, 8, 3, '!']
# print(Montagne)
# print(choix(1,Montagne))

# Montagne = ['!', 2, 8, 2, '!']
# print(Montagne)
# print(choix(2,Montagne))

# Montagne = ['!', 8, '!']
# print(Montagne)
# print(choix(1,Montagne))

#print("colonne instable (1) : ",colonne_instable())
# effondrement(0)
# print(Montagne)
# effondrement(1)
# print(Montagne)
# effondrement(2)
# print(Montagne)
# effondrement(3)
# print(Montagne)
# effondrement(4)
# print(Montagne)
# effondrement(5)
# print(Montagne)
# print(compteur)

#dada = 0
#def Test():
#	global dada
#	dada += 1

#Test()

#print(dada)

#print("colonne instable (2) : ",colonne_instable())


# boucle principale
# tant qu'il y a une colonne instable, on continue

#while colonne_instable() != False :

	#prnt("test")

	# 1/ chercher la premiere colonne instable de gauche a droite
	#colonne = colonne_instable()

	# 2/ la faire s'effondrer
	#effondrement(colonne)

#print("compteur : ",compteur)



# pour le moment, je ne sais pas trop quelle condition mettre,
# alors on va partir sur une centaine d'iterations pour avoir
# un systeme stable, ce qui sera largement suffisant

#for i in range(100):

	# je pense qu'il faut proceder comme ceci : 
	# 2/ la faire s'effondrer
	# 3/ puis recommencer
	# 4/ avec a chaque effondrement une verification que le carre n'est
	#    pas ejecte et donc comptabilise comme ejecte

	# donc visiblement il me faudrait une fonction qui cherche la premiere
	# colonne instable en partant de gauche

	# puis une fonction pour l'effondrement, qui utilisera la fonction
	# modifier element

	# et une fonction de verification pour les carres ejectes

	# enfin, il faut un compteur global pour les carres comptes
	# je le met a l'exterieur de la boucle, juste apres la matrice,
	# pour que chaque fonction y ait acces









