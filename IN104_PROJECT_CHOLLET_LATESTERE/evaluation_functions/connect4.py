from aiarena.connect4 import cell
import math as m

def evaluate(gs):
	PiontsAlignes = [0,0,0,0]
	nmbPionts = 0
	for j in range(7) :
		for i in range(6):
			if (gs.getCell(i,j).color != cell.NONE) :
				mult = 2* (gs.getCell(i,j).color == cell.WHITE) -1
				nmbPionts += 1
				Val = checkHoriz(gs,i,j)
				PiontsAlignes[Val-1] += mult
				Val = checkVert(gs,i,j)
				PiontsAlignes[Val-1] += mult
				Val = checkD1(gs,i,j)
				PiontsAlignes[Val-1] += mult
				Val = checkD2(gs,i,j)
				PiontsAlignes[Val-1] += mult
	if PiontsAlignes[3] != 0:
		#print(PiontsAlignes[3]/abs(PiontsAlignes[3]) * 10000000 / (nmbPionts**2))
		return PiontsAlignes[3]/abs(PiontsAlignes[3]) * 10000000 / (nmbPionts**2)
	else :
		return PiontsAlignes[0] * 1 + PiontsAlignes[1] * 5 + PiontsAlignes[2] * 10





def checkHoriz(gs,i,j):
	a, b = i, j
	compteur = 1
	while b>0 and gs.getCell(a,b-1).color == gs.getCell(i,j).color:
		b -=1
		compteur +=1
	b = j
	while b<6 and gs.getCell(a,b+1).color == gs.getCell(i,j).color:
		b+=1
		compteur +=1
	if compteur >= 4:
		return 4	
	return compteur

def checkVert(gs,i,j):
	a, b = i, j
	compteur = 1
	while a>0 and gs.getCell(a-1,b).color == gs.getCell(i,j).color:
		a -=1
		compteur +=1
	a = i
	while a<5 and gs.getCell(a+1,b).color == gs.getCell(i,j).color:
		a+=1
		compteur +=1
	if compteur >= 4:
		return 4
	return compteur

def checkD1(gs,i,j):
	a, b = i, j
	compteur = 1	
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
		return 4	
	return compteur


def checkD2(gs,i,j):
	a, b = i, j
	compteur = 1
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
		return 4
	return compteur














