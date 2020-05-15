def minimax(node, maximize, get_children, evaluate, max_depth,currentMinMax=(maximize==1)*):
	if (max_depth == 0):
		return evaluate(node)
	noeudsEnfant = get_children(node)
	if len(noeudsEnfant) == 0 :
		return evaluate(node)
	minmaxEnfant = []
	for element in noeudsEnfant :
		mimaElement = minimax(element, not maximize, get_children, evaluate,max_depth-1)
		if maximize and mimaElement >=currentMinMax:
			return mimaElement
		elif (not maximize) and mimaElement<=currentMinMax:
			return mimaElement
		minmaxEnfant.append(mimaElement)
	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		


