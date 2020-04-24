def minimax(node, maximize, get_children, evaluate, max_depth):
	if (max_depth == 0):
		return evaluate(node)
	noeudsEnfant = get_children(node)
	if len(noeudsEnfant) == 0 :
		return evaluate(node)
	minmaxEnfant = []
	for element in noeudsEnfant :
		minmaxEnfant.append(minimax(element, not maximize, get_children, evaluate,max_depth-1))
	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		


