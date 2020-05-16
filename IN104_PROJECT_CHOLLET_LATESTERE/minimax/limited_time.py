def minimax(node, maximize, get_children, evaluate, T_limit,T_recherche):

	if (T_recherche>T_limit):
		return evaluate(node)
	noeudsEnfant = get_children(node)

	if len(noeudsEnfant) == 0 :
		return evaluate(node)

	minmaxEnfant = []
	nmbEnfants = len(noeudsEnfant)
	for element in noeudsEnfant :
		minmaxEnfant.append(minimax(element, not maximize, get_children, evaluate,T_limit/nmbEnfant,T_recherche)

	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		
