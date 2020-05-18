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
    					score=score+5+i
    					totBlanc=totBlanc+1
    				else:
    					score=score-5-8+i
    					totNoir=totNoir+1
                                        

    			if gameState.getCell(i,j).type == cell.KING:

    				if gameState.getCell(i,j).isWhite:
    					score=score+7+i
    					totBlanc=totBlanc+1
    				else:
    					score=score-7-8+i
    					totNoir=totNoir+1
                        		
    if totNoir==0:
        score=score+1000
    if totBlanc==0:
        score=score-1000
    return (score)

###
#def val_case(i,j):
#    val=[[0,100,0,100,0,100,0,80],[50,0,70,0,70,0,70,0],[0,25,0,25,0,25,0,40],[25,0,10,0,10,0,10,0],[0,10,0,10,0,10,0,25],[40,0,25,0,25,0,25,0],[0,70,0,70,0,70,0,50],[80,0,100,0,100,0,100,0]]
#    return (val[i][j])
###
