from aiarena.connect4 import cell
import math as m

def evaluate(gs):
	score = 0
	for j in range(7) :
		for i in range(6):
			if (gs.getCell(i,j).color != cell.NONE) :
				score += checkHoriz(gs,i,j)
				score += checkVert(gs,i,j)
				score += checkD1(gs,i,j)
				score += checkD2(gs,i,j)
	return score





def checkHoriz(gs,i,j):
	a, b = i, j
	score = 0
	compteur = 1
	mult = 2* (gs.getCell(i,j).color == cell.WHITE) -1	
	while b>0 and gs.getCell(a,b-1).color == gs.getCell(i,j).color:
		b -=1
		compteur +=1
	b = j
	while b<6 and gs.getCell(a,b+1).color == gs.getCell(i,j).color:
		b+=1
		compteur +=1
	if compteur >= 4:
		return mult*m.inf
	if b<6 and gs.getCell(a,b+1).color == cell.NONE:
		score +=100 * (compteur**4)*mult
	if b>compteur-1 and gs.getCell(a,b-compteur).color == cell.NONE:
		score +=100*(compteur**4)*mult 	
	return score

def checkVert(gs,i,j):
	a, b = i, j
	score = 0
	compteur = 1
	mult = 2* (gs.getCell(i,j).color == cell.WHITE) -1	
	while a>0 and gs.getCell(a-1,b).color == gs.getCell(i,j).color:
		a -=1
		compteur +=1
	a = i
	while a<5 and gs.getCell(a+1,b).color == gs.getCell(i,j).color:
		a+=1
		compteur +=1
	if compteur >= 4:
		return mult*m.inf
	if a<5 and gs.getCell(a+1,b).color == cell.NONE:
		score +=100 * (compteur**4)*mult
	if a>compteur-1 and gs.getCell(a-compteur,b).color == cell.NONE:
		score +=100*(compteur**4)*mult 	
	return score

def checkD1(gs,i,j):
	a, b = i, j
	score = 0
	compteur = 1
	mult = 2* (gs.getCell(i,j).color == cell.WHITE) -1	
	while a>0 and b>0 and gs.getCell(a-1,b-1).color == gs.getCell(i,j).color:
		a -=1
		b -=1
		compteur +=1
	a,b = i,j
	while a<5 and b<6 and gs.getCell(a+1,b+1).color == gs.getCell(i,j).color:
		a+=1
		b+=1
		compteur +=1
	if compteur >= 4:
		return mult*m.inf
	if a<5 and b<6 and gs.getCell(a+1,b+1).color == cell.NONE:
		score +=100 * (compteur**4)*mult
	if a>compteur-1 and b>compteur-1 and gs.getCell(a-compteur,b-compteur).color == cell.NONE:
		score +=100*(compteur**4)*mult 	
	return score


def checkD2(gs,i,j):
	a, b = i, j
	score = 0
	compteur = 1
	mult = 2* (gs.getCell(i,j).color == cell.WHITE) -1	
	while a<5 and b>0 and gs.getCell(a+1,b-1).color == gs.getCell(i,j).color:
		a +=1
		b -=1
		compteur +=1
	a,b = i,j
	while a>0 and b<6 and gs.getCell(a-1,b+1).color == gs.getCell(i,j).color:
		a-=1
		b+=1
		compteur +=1
	if compteur >= 4:
		return mult*m.inf
	if a+compteur<6 and b>compteur-1 and gs.getCell(a+1,b-compteur).color == cell.NONE:
		score +=100 * (compteur**4)*mult
	if a>0 and b<6 and gs.getCell(a-1,b+1).color == cell.NONE:
		score +=100*(compteur**4)*mult 	
	return score















