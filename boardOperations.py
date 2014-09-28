#!/usr/bin/python

def leftAlignNumbers(array): 
	temp = filter(lambda a: a != 0, array);
	while len(temp) <> len(array):
		temp.append(0);
	return temp;

def moveLeft2048(board):
	for i in range(0,4):
		row = board[i];
		row = leftAlignNumbers(row)
		board[i] = row;

	for i in range(0,4):
		for j in range(0,3):
			if board[i][j] == board[i][j+1] and board[i][j] <> 0:
				board[i][j] *= 2;
				del(board[i][j+1]);
				board[i].append(0);				


def remove_values_from_list(the_list, val):
  return [value for value in the_list if value != val]
		
def displayBoard(board):
	for i in range(0,4):
		for j in range(0,4):
			print str(board[i][j]) + " ",;
		print;

# This method is used to check whether the board is blocked and the game is over or not
def checkBlocked(board):
	if moveLeft2048(board) == board and moveDown2048(board) == board:
		return True;
	else:
		return False;



	


# board = [[0 for x in xrange(4)] for x in xrange(4)] ;
# displayBoard(board);
# print;
# board[0][0] = 2;
# board[1][1] = 2;
# board[2][2] = 2;
# board[3][3] = 2;
# displayBoard(board);
# print;
# moveLeft2048(board);
# displayBoard(board);

x = [1,2,3,2,2,2,3,4]
board = [[0 for x in xrange(4)] for x in xrange(4)]
board[0][1] = 2;
board[1][1] = 4;
board[2][1] = 4;
board[3][1] = 4;

board[0][2] = 2;
board[1][2] = 4;
board[2][2] = 2;
board[3][2] = 8;

board[0][3] = 2;
board[1][3] = 4;
board[2][3] = 2;
board[3][3] = 2;

displayBoard(board);
moveLeft2048(board);
print;
displayBoard(board);