from aiarena.checkers import cell

def evaluate(gameState):
    score=0
    totBlanc=0
    totNoir=0
    for i in range (8):
    	for j in range (8):
    		if (j%2 == 1 and i%2 == 0) or (j%2 == 0 and i%2 == 1):  
    			if gameState.getCell(i,j).type == cell.MAN:
    				if gameState.getCell(i,j).isWhite:
    					score=score+15-i
    					totBlanc=totBlanc+1
    				else:
    					score=score-15+7-i
    					totNoir=totNoir+1
                                        

    			if gameState.getCell(i,j).type == cell.KING:

    				if gameState.getCell(i,j).isWhite:
    					score=score+30
    					totBlanc=totBlanc+1
    				else:
    					score=score-30
    					totNoir=totNoir+1
                        		
    if totNoir==0:
        score=score+1000
    if totBlanc==0:
        score=score-1000
    return (score)


