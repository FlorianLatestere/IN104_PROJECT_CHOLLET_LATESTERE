# executez ce script dans un terminal (depuis n'importe quel repertoire)
# avec la commande python -m IN104_PROJECT_NOM1_NOM2.scripts.random_vs_random
import aiarena
import randomBrain
from ..randomBrain import RandomBrain

# TODO: Instantier ICI des IA de type RandomBrain

brain1 = randomBrain.RandomBrain()
brain2 = randomBrain.RandomBrain()
timeLimit = 1 #The AI gave 1 second to play

for module in [aiarena.abalone, aiarena.chess, aiarena.checkers, aiarena.connect4]:
    # TODO: ajouter le code pour lancer une partie et afficher son déroulement
    game = aiarena.Game(module, brain1, timeLimit, brain2, timeLimit)
    # afficher le PGN en fin de partie
    print(game.pgn) #print the summary of the game.
    input('press enter to continue')

