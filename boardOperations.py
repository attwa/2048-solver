#!/usr/bin/python

# This method is used to check whether the board is blocked and the game is over or not
def checkBlocked(board):
	if moveLeft2048(board) == board and moveDown2048(board) == board:
		return True;
	else:
		return False;

# This method is used to rotate the board clockwise count times 
# so that we can use move left for move right/up/down just by rotating 
# first then applying move left then applying rotate again
def rotateBoard(board, count):
	temp = [x[:] for x in board];
	boardSize = len(board);
	# board = [[0 for x in xrange(boardSize)] for x in xrange(boardSize)];
	for i in range(0, count):
		for j in range(0, boardSize):
			board[boardSize - 1 - j]= [item[j] for item in temp];
		temp = [x[:] for x in board]

# This method is used to remove any zeros that lie between any 
# non zero numbers in all the rows of the board 
def leftAlignNumbers(array): 
	temp = filter(lambda a: a != 0, array);
	while len(temp) <> len(array):
		temp.append(0);
	return temp;

# This method is used to model move left in the game
def moveLeft2048(board):
	boardSize = len(board);
	for i in range(0,boardSize):
		row = board[i];
		row = leftAlignNumbers(row)
		board[i] = row;

	score = 0;
	for i in range(0,boardSize):
		for j in range(0,boardSize-1):
			if board[i][j] == board[i][j+1] and board[i][j] <> 0:
				board[i][j] *= 2;
				score += board[i][j];
				del(board[i][j+1]);
				board[i].append(0);	
	return score;			

# This method is used to model move Down in the game		
def moveDown2048(board):
	rotateBoard(board,3);
	cost = moveLeft2048(board);
	rotateBoard(board,1);
	return cost;

# This method is used to model move Right in the game
def moveRight2048(board):
	rotateBoard(board,2);
	cost = moveLeft2048(board);
	rotateBoard(board,2);
	return cost;

# This method is used to model move Up in the game
def moveUp2048(board):
	rotateBoard(board,1);
	cost = moveLeft2048(board);
	rotateBoard(board,3);
	return cost;

# This method is used to display the board in the console
def displayBoard(board):
	for i in range(0, len(board)):
		for j in range(0, len(board)):
			print str(board[i][j]) + " ",;
		print;
	print;


def tests():
	# board = [[1,0,0,2],[0,1,2,0],[0,4,3,0],[4,0,0,3]];
	# board = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]];
	board = [[2,4,0,0],[4,4,8,8],[8,16,16,32],[64,128,64,128]]
	displayBoard(board);
	moveUp2048(board);
	displayBoard(board);

tests();