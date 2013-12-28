from math import *
from random import *

# que je suis bete ! cette structure correspondrait 
#bien mieux ! il faut tout reprendre...

Montagne = [ 8 , 5 , 4 , 3 , 2 , 1 , '!' ]

# une seule obligation a ce format : un '!' a la fin
# cependant, l'avantage est de pouvoir en mettre ailleurs
# on suppose aussi que la montagne fait au moins une colonne d'epaiseur

# compteur principal de carres ejectes

compteur = 0
length = len(Montagne)


def colonne_instable():

	""" retourne le numero de la premiere colonne de rochers
		instables reperee, en partant de la gauche.
		S'il n'y a pas de colonnes instables, renvoi False. """

	precedente = Montagne[0]

	# si la difference de hauteur est de deux, la colonne est instable
	for i in range(1,length-1):
		# 1er cas : si la colonne actuelle est plus grande
		# (de 2 carres ou + ) que la precedente
		if Montagne[i]-precedente > 2 :
			return i # dans ce cas elle est instable
		# 2eme cas : si la colonne actuelle est plus petite
		# (de 2 carres ou + ) que la precedente
		elif Montagne[i]-precedente < -2 : 
			return i-1 # dans ce cas celle d'avant est instable
	return False # sinon on retourne False

def effondrement(rang):

	""" effectue l'effondrement de la colonne dont le numero
		est specifie en parametre. Si le cube atteint un '!',
		il est ejecte et comptabilise tel quel. """

	# je pense que tout ne marche pas comme il faut quand on est à coté d'un "!"

	print("effondrement")

	global compteur

	# si l'on est pas a l'une des deux etremites
	if rang not in [0, length-2] : 
		gauche = Montagne[rang-1]
		droite = Montagne[rang+1]
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
	# sinon
	else :
		print("extremite")
		choix = rang+1
		# si on est a la fin, c'est des carres ejectes
		#if rang != 0 :
			#compteur += 2


	# dans tous les cas de figure, la colonne actuelle perds 2 unites
	# n'importe quoi, pas forcement vrai
	#Montagne[rang] -= 2

	# puis, si la colonne suivante n'est pas un "conteneur" a cubes
	if Montagne[choix] != '!' :
		Montagne[choix] += 2
	# sinon, on les ejecte et on les comptabilisent
	####
	####
	#### ICI ! Il faudrait sans doute rajouter que si la colonne a gauche
	# du "!" a moins de 3 carres, sa ne s'effondre pas?
	####
	####
	# par contre s'il y a un contener a cubes
	else :
		compteur += 2


##########
##########
# TESTS  #
##########

#print("colonne instable (1) : ",colonne_instable())
effondrement(0)
print(Montagne)
effondrement(1)
print(Montagne)
effondrement(2)
print(Montagne)
effondrement(3)
print(Montagne)
effondrement(4)
print(Montagne)
effondrement(5)
print(Montagne)
print(compteur)

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









