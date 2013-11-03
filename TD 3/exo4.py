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

print("fonction inverse")
print(inverse([1,2,"trois",4,5,6]))


# une fonction qui dit si une liste est palindrome ou non
def palindrome(liste):
	if liste == inverse(liste):
		return True
	else: # on aurait meme pu se passer du else
		return False

print("fonction palindrome")

print(palindrome([1,2,3,2,1]))
print(palindrome([1,2,3,4,5]))


# meme chose, mais en ne parcourant qu une seule fois la liste
def palindrome_rapide(liste):
	palindrome = True
	length = len(liste)
	for i in range(length):
		if(liste[i] != liste[(length-1)-i]):
			palindrome = False
	return palindrome

print("fonction palindrome_rapide")

print(palindrome_rapide([1,2,3,2,1]))
print(palindrome_rapide([1,2,3,3,2,1]))
print(palindrome_rapide(["test"]))
print(palindrome_rapide(["pas","un","palindrome"]))
