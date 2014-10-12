import copy
from random import randint

# This method is used to rotate the grid clockwise count times
# so that we can use move left for move right/up/down just by rotating
# first then applying move left then applying rotate again
# returns the grid rotated count times antclock wise
def rotateGrid(grid, count):
  temp = copy.deepcopy(grid)
  gridSize = len(grid)
  grid = [[0]*gridSize]*gridSize
  for i in range(count):
    for j in range(gridSize):
      grid[gridSize - 1 - j]= [item[j] for item in temp]
    temp = copy.deepcopy(grid)
  return grid

# This method is used to display the grid in the console
def displayGrid(grid, ret=False):
  s=""
  for row in grid:
    s += "\t".join(map(str, row)) + "\n"
  if ret: return s
  print(s)

# This method is used to add a tile for the grid
# returns new grid affter adding a tile
def addTile(grid):
  grid = copy.deepcopy(grid)
  if grid[0][0] == 0:
    grid[0][0] = 2
  elif grid[0][-1] == 0:
    grid[0][-1] = 2
  elif grid[-1][-1] == 0:
    grid[-1][-1] = 2
  elif grid[-1][0] == 0:
    grid[-1][0] = 2
  return grid

# This method is used to remove any zeros that lie between any
# non zero numbers in all the rows of the grid
# returns an array with zeros moved to the right of it
def leftAlignNumbers(array):
  temp = [x for x in filter(lambda a: a != 0, array)]
  while len(temp) != len(array):
    temp.append(0)
  return temp

#generates a grid and sets two random cells to 2
def GenGrid(rows=4, cols=4):
  grid = [[0]*cols for x in range(rows)]

  # checks that there are two '2's in the grid and then add another 2
  # protects against problem where the random values for row and col are the same
  while sum(map(sum, grid)) < 4:
    grid[randint(0, rows-1)][randint(0, cols-1)] = 2
  return grid
