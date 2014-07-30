import itertools as it

def getGrid(x):
	f = open("96.txt")
	lines = f.readlines()
	grid = [[int(char) for char in lines[k][0:-1]] for k in range(x*10+1,x*10+10)]
	f.close()
	return grid

def getLine(line):
	s = [x for x in range(1,10)];
	for n in line:
		if n != 0:
			s.remove(n)
	return ''.join([str(x) for x in s])

def insertPerm(perm, grid, line, gridmap):
	perm = [c for c in perm]
	for c in range(9):
		if gridmap[line][c] == 0:
			grid[line][c] = int(perm.pop())
	return grid

def getSquareV(x,y,grid):
	if x<3 and y<3:
		return [grid[a][b] for a in [0,1,2] for b in [0,1,2]]
	if x<3 and y<6:
		return [grid[a][b] for a in [0,1,2] for b in [3,4,5]]
	if x<3 and y<9:
		return [grid[a][b] for a in [3,4,5] for b in [6,7,8]]
	if x<6 and y<3:
		return [grid[a][b] for a in [3,4,5] for b in [0,1,2]]
	if x<6 and y<6:
		return [grid[a][b] for a in [3,4,5] for b in [3,4,5]]
	if x<6 and y<9:
		return [grid[a][b] for a in [3,4,5] for b in [6,7,8]]
	if x<9 and y<3:
		return [grid[a][b] for a in [6,7,8] for b in [0,1,2]]
	if x<9 and y<6:
		return [grid[a][b] for a in [6,7,8] for b in [3,4,5]]
	if x<9 and y<9:
		return [grid[a][b] for a in [6,7,8] for b in [6,7,8]]

def check(elt):
	elt = filter(lambda a: a != 0, elt)
	values = []
	for v in elt:
		if v in values:
			return False
		else:
			values.append(v)
	return True

def checkGrid(grid):
	for a in range(9):
		if not check([grid[x][a] for x in range(9)]):
			print 'column failed',a
			return False
	for a in range(3):
		for b in range(3):
			if not check(getSquareV(a*3,b*3,grid)):
				print 'square',a,b
				return False
	return True

def prt(grid):
	for k in range(9):
		print ''.join([str(x) for x in grid[k]])
	print

grid = getGrid(0)
gridmap = getGrid(0)
for p1 in it.permutations(getLine(gridmap[0])):
	grid = insertPerm(p1, grid, 0, gridmap)
	for p2 in it.permutations(getLine(gridmap[1])):
		grid = insertPerm(p2, grid, 1, gridmap)
		if not checkGrid(grid):
			prt(grid)
		#	for p3 in it.permutations(getLine(gridmap[2])):
		#		grid = insertPerm(p3, grid, 2, gridmap)
	
		

