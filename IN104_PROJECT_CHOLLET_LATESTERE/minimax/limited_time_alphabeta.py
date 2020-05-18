import time
import math as m
def minimax(node, maximize, get_children, evaluate,T_limit,T_recherche,alpha=-m.inf, beta=m.inf):
	tic=time.time()

	if (T_recherche > T_limit):
		return evaluate(node)
	noeudsEnfant = get_children(node)

	if len(noeudsEnfant) == 0 :
		return evaluate(node)

	minmaxEnfant = []
	nmbEnfants = len(noeudsEnfant)
	tac = time.time()
	T_limit_enfants = (T_limit + tic - tac)
	n = 0 
	for element in noeudsEnfant :
		toc = time.time()
		mimaElement = minimax(element, not maximize, get_children, evaluate,(T_limit_enfants/nmbEnfants),T_recherche,alpha,beta)

		if maximize and mimaElement >=beta:
			return mimaElement
		elif (not maximize) and mimaElement<=alpha:
			return mimaElement

		if (not maximize) and mimaElement <beta:
			beta =mimaElement
		elif maximize and mimaElement > alpha:
			alpha = mimaElement
		minmaxEnfant.append(mimaElement)
		n += 1
		tuc = time.time()
		if nmbEnfants-n != 0 :
			T_limit_enfants += ((T_limit_enfants)/(nmbEnfants) - (tuc - toc))*nmbEnfants/(nmbEnfants-n)

	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		


