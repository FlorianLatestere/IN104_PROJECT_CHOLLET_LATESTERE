def minimax(node, maximize, get_children, evaluate, max_depth,dico):

	if (max_depth == 0):
		strnode=toString(node)
		if dico.has_key[strnode]:
			return dico[strnode]
		else:
			dico[strnode]=evaluate(node)
			return dico.get[strnode]

	noeudsEnfant = get_children(node)
	if len(noeudsEnfant) == 0 :
		return evaluate(node)
	minmaxEnfant = []
	for element in noeudsEnfant :
		minmaxEnfant.append(minimax(element, not maximize, get_children, evaluate,max_depth-1,dico))

	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		


