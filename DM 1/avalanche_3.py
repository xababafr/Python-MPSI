Montagne =[ " |...... ",
			" |*..... ",
			" |*..... ",
			" |*..... ",
			" |**.... ",
			" |***... ",
			" |****.. ",
			" |*****. ",
			" |****** " ]

# la matrice de la Montagne
# les | representent le mur
# les * representent les roches
# les . representent du vide

# compteur principal de carres ejectes

compteur = 0

def element(ligne,colonne):

	""" la fonction qui renvoi le contenu de la matrice à
	    la ligne et la colonne souhaitee. On suppose que
	    le mur est la colonne numero 1 et que la premiere
	    ligne de la matrice est la premiere ligne egalement.
	    La fonction renvoi 0 si c'est un mur, 1 si c'est un
	    rocher, 2 si c'est un vide, et enfin 3 si ce n'est
	    aucun des elements precedents (dans ce cas, cela
	   	veut dire que l'on est dans la derniere colonne,
	   	celle ou seront comptabilises les carres ejectes."""

		# de par la structure choisie precedemment, selectionner
		# un element precis est tres simple

		element = Montagne[ligne-1,colonne]

		# on retourne en fonction du contenu

		if element == "|" :
			return 0
		elif element == "*" :
			return 1
		elif element == "." :
			return 2
		elif element == " " :
			return 3
		else # erreur
			return False

def modifier_element(ligne,colonne,contenu):

	""" remplace l'element de la matrice specifie par la
		nouvelle valeur passee en argument. """

	if len(contenu) == 1:
		Montagne[ligne-1,colonne] = "contenu" 
	else
		return False

# boucle principale

# pour le moment, je ne sais pas trop quelle condition mettre,
# alors on va partir sur une centaine d'iterations pour avoir
# un systeme stable, ce qui sera largement suffisant

for i in range(100):

	# je pense qu'il faut proceder comme ceci : 
	# 1/ chercher la premiere colonne instable de gauche a droite
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
	# pour que chaque fonction y ait accès












