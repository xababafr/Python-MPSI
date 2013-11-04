# les fonctions dont on a besoin : 

# une fonction qui inverse une liste sans utiliser reverse()
def inverse(liste):
	length = len(liste)
	R = []
	for j in range(length):
		R.append('')
	# on parcours la liste en sens normal
	for i in range(length):
		# on rempli la liste a retourner d elements vides
		R[(length-1)-i] = liste[i]
	return R

# une fonction qui dit si une liste est palindrome ou non
def palindrome(liste):
	#if liste == inverse(liste):
	if liste == liste[::-1]:
		return True
	else: # on aurait meme pu se passer du else
		return False

# conversion nombre / liste
def numberToList(nombre):
	liste = [int(i) for i in str(nombre)]
	#on aurait pu faire : return [int(i) for i in str(nombre)]
	return liste

# conversion liste / nombre
def listToNumber(liste):
	nombre = 0
	length = len(liste)
	for i in range(length):
		nombre += liste[length-1-i] * 10**i
	return nombre


# les nombre de lychrel
reponse = []

# boucle principale : de 0 a 200
for i in range(200):

	# booleen continuer
	continuer = True

	additionD = -1

	# boucle secondaire : 50 tests de palindromes
	for j in range(50):

		# !!!! il faut repartir sur l'addition et pas sur les memes nombres
		# a chaque fois !!!!!!

		if additionD < 0:
			nombre = i
		else:
			nombre = additionD

		# si il faut s arreter, on s arrete
		if continuer == False :
			break

		# le nombre et son inverse sous forme de liste
		nombre = numberToList(nombre)
		inverse = nombre[::-1]

		# le nombre et son inverse sous forme d'entiers
		nombreD = i
		inverseD = listToNumber(inverse)

		#print(nombre)
		#print(inverse)

		# addition puis palindrome?
		len = len(nombre)
		# addition
		additionD = nombreD + inverseD
		addition = numberToList(additionD)

		#palindrome?
		condition = palindrome(addition)
		if condition == True :
			continuer = False

	# le booleen est-il encore vrai?
	if continuer == True : 
		reponse.append(i)


	