# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.human_vs_AI
import aiarena
from ..minimaxBrain import MinimaxBrain

brain1 = aiarena.ManualBrain()
human_time = 20 #the human will have 10 secs to play
brain2 = MinimaxBrain(aiarena.checkers)
brain2.depth = 7
ai_time = 1 #the AI will only have 1 sec to play
game = aiarena.Game(aiarena.checkers, brain1, human_time, brain2, ai_time)
game.displayLevel = 1   # this prints the board after each move
game.start()
print(game.pgn) #print the summary of the game. 

# Lancer une partie entre votre IA MinimaxBrain et un humain sur le puissance4 ou aux dames
