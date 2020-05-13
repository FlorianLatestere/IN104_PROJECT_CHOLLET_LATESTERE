import aiarena
# changer l'import ci-dessous pour changer la version de minimax utilisée
from .minimax.limited_depth import minimax
from .evaluation_functions import connect4, checkers

# definition d'un dictionaire qui associe à chaque jeu une fonction d'évaluation
evaluations_functions = {
    aiarena.checkers: checkers.evaluate,
    aiarena.connect4: connect4.evaluate
}

class MinimaxBrain:

    def __init__(self, gameclass, gameclass_arguments={}):
        self.depth = 5      # Set the exploration depth here
        self.get_children = gameclass.GameState.findNextStates
        self.evaluate = evaluations_functions[gameclass]

    def play(self, gameState, timeLimit):
        moves=gameState.findPossibleMoves()
        maxi=minimax(moves [0])
        nmaxi=0
        n=0
        for element in moves:
            if minimax(element)>maxi:
                maxi=minimax(element)
                nmaxi=n
            n=n+1
        return moves[nmaxi]

	

    def __str__(self):
        return "MiniMax_Player"
