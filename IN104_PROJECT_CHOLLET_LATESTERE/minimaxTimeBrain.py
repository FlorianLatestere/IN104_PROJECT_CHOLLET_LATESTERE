import aiarena
import time
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_time import minimax
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
        self.T_limit = 2
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]
        maxi=0
        for loop in range(50):
        	a=compute_research_time(gameclass.GameState())
        	if a>maxi:
        		maxi=a
        self.T_recherche= maxi
	
		

    def play(self, gameState, timeLimit):
        states=gameState.findNextStates()
        moves = gameState.findPossibleMoves()
        nmb = len(states)
        maxi=minimax(states[0], True, self.get_children, self.evaluate, self.T_limit/nmb,self.T_recherche)
        nmaxi=0
        n=0
        for element in states[1:]:
        	minim =minimax(element, True, self.get_children, self.evaluate, self.T_limit/nmb,self.T_recherche)
        	if minim>maxi:
        		maxi=minim
        		nmaxi=n
        	n=n+1
        return moves[nmaxi]
            
                
                
            
        

	

    def __str__(self):
        return "MiniMax_Player"


