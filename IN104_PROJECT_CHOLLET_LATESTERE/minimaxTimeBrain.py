import aiarena
import time
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_time_alphabeta import minimax
from .evaluation_functions import connect4, checkers

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers.evaluate,
    aiarena.connect4: connect4.evaluate
}

def compute_research_time (GameState):
	init=time.time()
	GameState.findNextStates()
	return(time.time()-init)
	


class MinimaxBrain:

    def __init__(self, gameclass, gameclass_arguments={}):
        self.T_limit = 1 * 0.7
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]
        maxi=0
        for loop in range(50):
        	a=compute_research_time(gameclass.GameState())
        	if a>maxi:
        		maxi=a
        self.T_recherche= maxi
	
		

    def play(self, gameState, timeLimit):
    	tac = time.time()
    	states=gameState.findNextStates()
    	moves = gameState.findPossibleMoves()
    	nmb = len(states)
    	print(self.T_limit, self.T_recherche)
    	toc = time.time()
    	maxi=minimax(states[0], False, self.get_children, self.evaluate, (self.T_limit + toc - tac)/nmb,self.T_recherche)
    	nmaxi=0
    	n=0
    	for element in states[1:]:
    		minim =minimax(element, False, self.get_children, self.evaluate, (self.T_limit+ toc - tac)/nmb,self.T_recherche)
    		if minim>maxi:
    			maxi=minim
    			nmaxi=n
    		n=n+1
    	print(time.time() - tac)
    	return moves[nmaxi]
        
	
        
            

    def __str__(self):
        return "MiniMax_Player"


