import aiarena
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_Time import minimax
from .evaluation_functions import connect4, checkers

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers.evaluate,
    aiarena.connect4: connect4.evaluate
}

class MinimaxTimeBrain:

    def __init__(self, gameclass, gameclass_arguments={}):
        self.T_limit = 4      # Set the exploration depth here
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]

    def play(self, gameState, timeLimit):
        states=gameState.findNextStates()
        moves = gameState.findPossibleMoves()
        maxi=minimax(states[0], True, self.get_children, self.evaluate, self.T_limit)
        nmaxi=0
        n=0
        for element in states:
            if minimax(element, True, self.get_children, self.evaluate, self.T_limit)>maxi:
                maxi=minimax(element, True, self.get_children, self.evaluate, self.T_limit)
                nmaxi=n
            n=n+1
        return moves[nmaxi]

	

    def __str__(self):
        return "MiniMax_Player"


