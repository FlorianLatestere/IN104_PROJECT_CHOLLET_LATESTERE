def minimax(node, maximize, get_children, evaluate, max_depth,alpha=-10**99, beta=10**99):

	if (max_depth == 0):
		return evaluate(node)
	noeudsEnfant = get_children(node)

	if len(noeudsEnfant) == 0 :
		return evaluate(node)

	minmaxEnfant = []

	for element in noeudsEnfant :
		mimaElement = minimax(element, not maximize, get_children, evaluate,max_depth-1,alpha,beta)
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
		


