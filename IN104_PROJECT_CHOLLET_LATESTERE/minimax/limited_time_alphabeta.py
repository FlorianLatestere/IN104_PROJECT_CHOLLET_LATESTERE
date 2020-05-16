import time
def minimax(node, maximize, get_children, evaluate,T_limit,T_recherche,alpha=-10**99, beta=10**99):
	tic=time.time()

	if (T_recherche > T_limit):
		return evaluate(node)
	noeudsEnfant = get_children(node)

	if len(noeudsEnfant) == 0 :
		return evaluate(node)

	minmaxEnfant = []
	nmbEnfants = len(noeudsEnfant)
	tac = time.time()
	for element in noeudsEnfant :
		mimaElement = minimax(element, not maximize, get_children, evaluate,((T_limit+tic-tac)/nmbEnfants),T_recherche,alpha,beta)

		if maximize and mimaElement >=beta:
			return mimaElement
		elif (not maximize) and mimaElement<=alpha:
			return mimaElement

		if (not maximize) and mimaElement <beta:
			beta =mimaElement
		elif maximize and mimaElement > alpha:
			alpha = mimaElement
		minmaxEnfant.append(mimaElement)

	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		


