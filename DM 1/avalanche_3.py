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

def get_element(ligne,colonne):
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
		content = Montagne[ligne-1,colonne]
		if content == "|" :
			return 0
		elif content == "*":
			return 1
		elif content == ".":
			return 2
		else # ( si content == " " )
			return 3


