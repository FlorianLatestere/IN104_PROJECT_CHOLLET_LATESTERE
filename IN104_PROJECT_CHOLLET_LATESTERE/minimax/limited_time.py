import time

def minimax(node, maximize, get_children, evaluate, T_limit,T_recherche):
	tic=time.time()
	if (T_recherche>T_limit):
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
		minmaxEnfant.append(minimax(element, not maximize, get_children, evaluate,(T_limit_enfants/nmbEnfants),T_recherche))
		tuc = time.time()
		T_limit_enfants = ((T_limit_enfants)/(nmbEnfants) - (tuc - toc))*nmbEnfants/(nmbEnfants-n)
		n += 1
		
	if (maximize) :
		return max(minmaxEnfant)
	return min(minmaxEnfant)
		
