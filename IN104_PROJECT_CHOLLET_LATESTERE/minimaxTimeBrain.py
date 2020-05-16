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
        tot=0
        for loop in range(10):
        	tot=tot+compute_research_time(gameclass.GameState())
        self.T_recherche=tot/10
	
		

    def play(self, gameState, timeLimit):
        states=gameState.findNextStates()
        moves = gameState.findPossibleMoves()
        maxi=minimax(states[0], True, self.get_children, self.evaluate, self.T_limit,self.T_recherche)
        nmaxi=0
        n=0
        for element in states:
            if minimax(element, True, self.get_children, self.evaluate, self.T_limit,self.T_recherche)>maxi:
                maxi=minimax(element, True, self.get_children, self.evaluate, self.T_limit,self.T_recherche)
                nmaxi=n
            n=n+1
        return moves[nmaxi]

	

    def __str__(self):
        return "MiniMax_Player"


