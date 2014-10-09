#!/usr/bin/env python3
import sys, os
from random import randint
from adt import Node, Problem
from search import general_search
import copy

#[T]wo [T]housand [F]ourty [E]ight problem class
class TTFE(Problem):
  def __init__(self, m):
    operators = [
      self.operator_up,
      self.operator_down,
      self.operator_left,
      self.operator_right
    ]
    super().__init__(
      operators,
      GenGrid(),
      self.create_goal_test(m)
    )

  #returns a function that is the correct goal test according to the chosesn M
  def create_goal_test(self, m):
    def goal_test(grid):
      for row in grid:
        for cell in row:
          if cell == m: return True
      return False
    return goal_test

  # This method is used to check whether the grid is blocked and the game is over or not
  # retruns either true or false
  def checkBlocked(self, grid):
    grid1, _ = operator_up(self, grid)
    grid2, _ = operator_left(self, grid)
    grid3, _ = operator_right(self, grid)
    grid4, _ = operator_down(self, grid)
    if  grid1 == grid2 & grid2 == grid3 & grid3 == grid4:
      return True
    else:
      return False

  # This method is used to rotate the grid clockwise count times
  # so that we can use move left for move right/up/down just by rotating
  # first then applying move left then applying rotate again
  # returns the grid rotated count times antclock wise
  @staticmethod
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
  def displayGrid(self, grid):
    for row in grid:
      for cell in row:
        print(cell, end="\t")
      print()
    print()

  # This method is used to add a tile for the grid
  # returns new grid affter adding a tile
  def addTile(self, grid):
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
  @staticmethod
  def leftAlignNumbers(array): 
    temp = filter(lambda a: a != 0, array)
    while len(temp) != len(array):
      temp.append(0)
    return temp

  #doc lines are used to get a human readable description of the action
  #each operator returns a new state and a cost

  # This method is used to model move left in the game
  # returns grid after moving it left and score from the move
  # if the move doesn't change the state it return None and 0
  def operator_left(self, grid):
    """Move left"""
    originalGrid = grid
    grid = copy.deepcopy(grid)
    gridSize = len(grid)
    for i in range(ridSize):
      row = grid[i]
      row = leftAlignNumbers(row)
      grid[i] = row

    score = 0
    for i in range(ridSize):
      for j in range(ridSize-1):
        if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
          grid[i][j] *= 2
          score += grid[i][j]
          del(grid[i][j+1])
          grid[i].append(0)
    if grid == originalGrid:
      return None, 0
    else:
      return grid, score

  # This method is used to model move Up in the game
  # returns grid after moving it up and score from the move
  # if the move doesn't change the state it return None and 0
  def operator_up(self, grid):
    """Move up"""
    originalGrid = grid
    grid = rotateGrid(grid,1)
    grid, cost = moveLeft2048(grid)
    if grid == None:
      return None, 0
    grid = rotateGrid(grid,3)
    return grid, cost

  # This method is used to model move Down in the game
  # returns grid after moving it down and score from the move
  # if the move doesn't change the state it return None and 0
  def operator_down(self, grid):
    """Move down"""
    originalGrid = grid
    grid = rotateGrid(grid,3)
    grid, cost = moveLeft2048(grid)
    if grid == None:
      return None, 0
    grid = rotateGrid(grid,1)
    return grid, cost

  # This method is used to model move Right in the game
  # returns grid after moving it right and score from the move
  # if the move doesn't change the state it return None and 0
  def operator_right(self, grid):
    """Move right"""
    originalGrid = grid
    grid = rotateGrid(grid,2)
    grid, cost = moveLeft2048(grid)
    if grid == None:
      return None, 0
    grid = rotateGrid(grid,2)
    return grid, cost

#generates a grid and sets two random cells to 2
def GenGrid(rows=4, cols=4):
  grid = [[0]*cols for x in range(rows)]

  # checks that there are two '2's in the grid
  # protects against problem where the random values for row and col are the same
  while sum(map(sum, grid)) < 4:
    grid[randint(0, rows-1)][randint(0, cols-1)] = 2
  return grid

if __name__ == "__main__":
  p = TTFE(2048)
  pass
