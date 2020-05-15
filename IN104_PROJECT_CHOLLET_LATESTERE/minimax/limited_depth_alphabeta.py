def minimax(node, maximize, get_children, evaluate, max_depth,alpha=-10**99, beta=10**99):
	if (max_depth == 0):
		return evaluate(node)
	noeudsEnfant = get_children(node)
	if len(noeudsEnfant) == 0 :
		return evaluate(node)
	alpha = minimax(noeudsEnfant[0], not maximize, get_children, evaluate,max_depth-1)
	beta = alpha
	minmaxEnfant = [alpha]
	for element in noeudsEnfant[1:] :
		mimaElement = minimax(element, not maximize, get_children, evaluate,max_depth-1,alpha,beta)
		if maximize and mimaElement >=beta:
			return mimaElement
		elif (not maximize) and mimaElement<=alpha:
			return mimaElement
		minmaxEnfant.append(mimaElement)
	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		


