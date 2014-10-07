#!/usr/bin/python
import copy
# This method is used to check whether the grid is blocked and the game is over or not
# retruns either true or false
def checkBlocked(grid):
	grid1, _ = moveLeft2048(grid);
	grid2, _ = moveDown2048(grid);   
	if  grid1 == grid2: 
		return True;
	else:
		return False;

# This method is used to rotate the grid clockwise count times 
# so that we can use move left for move right/up/down just by rotating 
# first then applying move left then applying rotate again
# returns the grid rotated count times antclock wise
def rotateGrid(grid, count):
	temp = copy.deepcopy(grid);
	gridSize = len(grid);
	grid = [[0]*gridSize]*gridSize;
	for i in range(0, count):
		for j in range(0, gridSize):
			grid[gridSize - 1 - j]= [item[j] for item in temp];
		temp = copy.deepcopy(grid);
	return grid;

# This method is used to remove any zeros that lie between any 
# non zero numbers in all the rows of the grid 
# returns an array with zeros moved to the right of it
def leftAlignNumbers(array): 
	temp = filter(lambda a: a != 0, array);
	while len(temp) <> len(array):
		temp.append(0);
	return temp;

# This method is used to model move left in the game
# returns grid after moving it left and score from the move
def moveLeft2048(grid):
	originalGrid = grid;
	grid = copy.deepcopy(grid);
	gridSize = len(grid);
	for i in range(0,gridSize):
		row = grid[i];
		row = leftAlignNumbers(row)
		grid[i] = row;

	score = 0;
	for i in range(0,gridSize):
		for j in range(0,gridSize-1):
			if grid[i][j] == grid[i][j+1] and grid[i][j] <> 0:
				grid[i][j] *= 2;
				score += grid[i][j];
				del(grid[i][j+1]);
				grid[i].append(0);
	if grid == originalGrid:
		return None, 0;
	else:	
		return grid, score;			

# This method is used to model move Down in the game		
# returns grid after moving it down and score from the move
def moveDown2048(grid):
	originalGrid = grid;
	grid = rotateGrid(grid,3);
	grid, cost = moveLeft2048(grid);
	if grid == None:
		return None, 0;
	grid = rotateGrid(grid,1);
	return grid, cost;

# This method is used to model move Right in the game
# returns grid after moving it right and score from the move
def moveRight2048(grid):
	originalGrid = grid;
	grid = rotateGrid(grid,2);
	grid, cost = moveLeft2048(grid);
	if grid == None:
		return None, 0;
	grid = rotateGrid(grid,2);
	return grid, cost;

# This method is used to model move Up in the game
# returns grid after moving it up and score from the move
def moveUp2048(grid):
	originalGrid = grid;
	grid = rotateGrid(grid,1);
	grid, cost = moveLeft2048(grid);
	if grid == None:
		return None, 0;
	grid = rotateGrid(grid,3);
	return grid, cost;

# This method is used to display the grid in the console
def displayGrid(grid):
	for i in range(0, len(grid)):
		for j in range(0, len(grid)):
			print str(grid[i][j]) + " ",;
		print;
	print;

# This method is used to add a tile for the grid
# returns new grid affter adding a tile
def addTile(grid):
	grid = copy.deepcopy(grid);
	last = len(grid) -1;
	if grid[0][0] == 0:
		grid[0][0] = 2;
	elif grid[0][last] == 0:
		grid[0][last] = 2;
	elif grid[last][last] == 0:
		grid[last][last] = 2;
	elif grid[last][0] == 0:
		grid[last][0] = 2;
	return grid;
	

def tests():
	# grid = [[0,0,0,2],[0,0,0,0],[0,0,0,0],[2,0,0,2]];
	# grid = [[1,0,0,2],[0,1,2,0],[0,4,3,0],[4,0,0,3]];
	# grid = [[2,0,0,0],[1,1,1,1],[2,2,2,2],[0,3,3,0]];
	# grid = [[2,4,0,0],[4,4,8,8],[8,16,16,32],[64,128,64,128]]
	grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];
	print checkBlocked(grid);
	# displayGrid(grid);
	# board,cost = moveDown2048(grid);
	# displayGrid(grid);
	# displayGrid(board);
	
tests();