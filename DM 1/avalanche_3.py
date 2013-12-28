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

	# si l'on est pas a l'une des deux etremites
	if rang not in [0, length-1] : 
		gauche = Montagne[rang-1]
		droite = Montagne[rang+1]
		# si il y a une denivelation + importante d'un coté comme de l'autre
		if gauche != droite :
			if gauche < droite :
				#Montagne[rang-1] += 2
				choix = rang-1
			else :
				#Montagne[rang+1] += 2
				choix = rang+1
		# ou si la dénivelation est la meme de chaque cote
		else :
			nbr = choice([-1,1])
			#Montagne[rang+nbr] += 2
			choix = rang+nbr
	# sinon
	else :
		# si on est au debut
		if rang == 0 :
			choix = rang+1
		# si on est a la fin, c'est des carres ejectes
		else :
			compteur += 2


	# dans tous les cas de figure, la colonne actuelle perds 2 unites
	Montagne[rang] -= 2

	# puis, si la colonne suivante n'est pas un "conteneur" a cubes
	if Montagne[choix] != '!' :
		montagne[choix] += 2
	# sinon, on les ejecte et on les comptabilisent
	else :
		compteur += 2




# boucle principale
# tant qu'il y a une colonne instable, on continue

while colonne_instable() :

	# 1/ chercher la premiere colonne instable de gauche a droite
	colonne = colonne_instable()

	# 2/ la faire s'effondrer
	effondrement(colonne)



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









