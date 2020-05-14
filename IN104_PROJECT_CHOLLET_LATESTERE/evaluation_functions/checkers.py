from aiarena.checkers import cell

def evaluate(gameState):
    score=0
    for i in range (8):
    	for j in range (8):
    		if (j%2 == 1 and i%2 == 0) or (j%2 == 0 and i%2 == 1):  
    			if gameState.getCell(i,j).type == cell.MAN:
    				if gameState.getCell(i,j).isWhite:
    					score=score+1
    				else:
    					score=score-1
    			if gameState.getCell(i,j).type == cell.KING:
    				if gameState.getCell(i,j).isWhite:
    					score=score+3
    				else:
    					score=score-3
    return (score)


