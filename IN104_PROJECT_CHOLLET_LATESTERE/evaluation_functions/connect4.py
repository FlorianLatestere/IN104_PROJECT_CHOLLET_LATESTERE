from aiarena.connect4 import cell
import math as m

def evaluate(gs):
	score = 0
	for i in range(7) :
		for j in range(6):
			score += checkHoriz(gs,i,j)
			score += checkVert(gs,i,j)
			score += checkD1(gs,i,j)
			score += checkD2(gs,i,j)
	return score





def checkHoriz(gs,i,j):
	a, b = i, j
	score = 0
	compteur = 1
	mult = 2* gs.getCell(i,j).isWhite -1	
	while b>0 and gs.getCell(a,b-1).type == gs.getCell(i,j).type:
		b -=1
		compteur +=1
	b = j
	while b<6 and gs.getCell(a,b+1).type == gs.getCell(i,j).type:
		b+=1
		compteur +=1
	if compteur >= 4:
		return mult*m.inf
	if b<6 and gs.getCell(a,b+1) == cell.NONE:
		score +=100 * compteur*mult
	if b>compteur-1 and gs.getCell(a,b-compteur) == cell.NONE:
		score +=100*compteur*mult 	
	return score

def checkVert(gs,i,j):
	a, b = i, j
	score = 0
	compteur = 1
	mult = 2* gs.getCell(i,j).isWhite -1	
	while a>0 and gs.getCell(a-1,b).type == gs.getCell(i,j).type:
		a -=1
		compteur +=1
	a = i
	while a<5 and gs.getCell(a,b+1).type == gs.getCell(i,j).type:
		a+=1
		compteur +=1
	if compteur >= 4:
		return mult*m.inf
	if a<5 and gs.getCell(a+1,b) == cell.NONE:
		score +=100 * compteur*mult
	if a>compteur-1 and gs.getCell(a-compteur,b) == cell.NONE:
		score +=100*compteur*mult 	
	return score

def checkD1(gs,i,j):
	a, b = i, j
	score = 0
	compteur = 1
	mult = 2* gs.getCell(i,j).isWhite -1	
	while a>0 and b>0 and gs.getCell(a-1,b-1).type == gs.getCell(i,j).type:
		a -=1
		b -=1
		compteur +=1
	a,b = i,j
	while a<5 and b<6 and gs.getCell(a+1,b+1).type == gs.getCell(i,j).type:
		a+=1
		b+=1
		compteur +=1
	if compteur >= 4:
		return mult*m.inf
	if a<5 and b<6 and gs.getCell(a+1,b+1) == cell.NONE:
		score +=100 * compteur*mult
	if a>compteur-1 and b>compteur-1 and gs.getCell(a-compteur,b-compteur) == cell.NONE:
		score +=100*compteur*mult 	
	return score


def checkD1(gs,i,j):
	a, b = i, j
	score = 0
	compteur = 1
	mult = 2* gs.getCell(i,j).isWhite -1	
	while a<5 and b>0 and gs.getCell(a+1,b-1).type == gs.getCell(i,j).type:
		a +=1
		b -=1
		compteur +=1
	a,b = i,j
	while a>0 and b<6 and gs.getCell(a-1,b+1).type == gs.getCell(i,j).type:
		a-=1
		b+=1
		compteur +=1
	if compteur >= 4:
		return mult*m.inf
	if a+compteur<6 and b>compteur-1 and gs.getCell(a+1,b-compteur) == cell.NONE:
		score +=100 * compteur*mult
	if a>0 and b<6 and gs.getCell(a-1,b+1) == cell.NONE:
		score +=100*compteur*mult 	
	return score















