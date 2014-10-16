import copy, numpy
from random import randint

# This function is used to rotate the grid clockwise count times
# so that we can use move left for move right/up/down just by rotating
# first then applying move left then applying rotate again
# returns the grid rotated count times anticlock wise
def rotateGrid(grid, count):
  for i in range(count):
    grid = numpy.transpose(grid)
    _, cols = grid.shape
    for i in range(cols):
      grid[:,i] = grid[:,i][::-1]
  return grid.tolist()

# This function is used to display the grid in the console if ret is false
# or to return the grid as a string if ret is true
def displayGrid(grid, ret=False):
  s=""
  for row in grid:
    s += "\t".join(map(str, row)) + "\n"
  if ret: return s
  print(s)

# This function is used to add a tile for the grid
# returns new grid after adding a tile
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

# This function is used to remove any zeros that lie between any
# non zero numbers in all the rows of the grid
# returns an array with zeros moved to the right of it
def leftAlignNumbers(array):
  temp = [x for x in filter(lambda a: a != 0, array)]
  while len(temp) != len(array):
    temp.append(0)
  return temp

# This is the function that is used as a building block for all operators
# This function moves the board to the left
def moveLeft2048(grid):
  originalGrid = grid
  grid = copy.deepcopy(grid)
  gridSize = len(grid)
  for i in range(gridSize):
    row = grid[i]
    row = leftAlignNumbers(row)
    grid[i] = row

  score = 0
  for i in range(gridSize):
    for j in range(gridSize-1):
      if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
        grid[i][j] *= 2
        score += grid[i][j]
        del(grid[i][j+1])
        grid[i].append(0)
  if grid == originalGrid:
    return None, 0
  else:
    return grid, score

#generates a grid and sets two random cells to 2
def GenGrid(rows=4, cols=4):
  grid = [[0]*cols for x in range(rows)]

  # checks that there are two '2's in the grid otherwise adds another 2
  while sum(map(sum, grid)) < 4:
    grid[randint(0, rows-1)][randint(0, cols-1)] = 2
  return grid
