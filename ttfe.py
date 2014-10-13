#!/usr/bin/env python3
import sys, os
from random import randint
from adt import Node, Problem
from search import general_search, dfs, bfs, ids
import copy
import numpy
import grid_ops

#[T]wo [T]housand [F]ourty [E]ight problem class
class TTFE(Problem):
  # this is the constructor for the 2048 problem class and it takes as input the required
  # m and the initial grid 
  def __init__(self, m, grid=None):
    operators = [
      self.operator_up,
      self.operator_down,
      self.operator_left,
      self.operator_right
    ]
    heuristics = [self.heuristic1, self.heuristic2, self.heuristic3]
    self.goal = m
    if grid is None:
      grid = grid_ops.GenGrid()
    super().__init__(
      operators,
      heuristics,
      grid,
      self.goal_test,
    )

  # this is the function that checks the goal test according to the chosen M
  def goal_test(self, grid):
    for row in grid:
      for cell in row:
        if cell == self.goal: return True
    return False

  # This function is used to check whether the grid is blocked and the game is over or not
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

  #doc lines are used to get a human readable description of the action
  #each operator returns a new state and a cost

  # This function is used to model move left in the game
  # returns grid after moving it left and score from the move
  # if the move doesn't change the state it returns None and 0
  def operator_left(self, grid):
    """Move left"""
    originalGrid = grid
    grid, cost = grid_ops.moveLeft2048(grid)
    if grid == None:
      return None, 0
    grid = grid_ops.addTile(grid)
    return grid, cost

  # this function returns the value of applying the first heuristic on the grid
  def heuristic1(self, grid):
    max_value = max(map(max, grid))
    cost = 0
    while max_value < self.goal:
      max_value *= 2
      cost += max_value
    return cost

  # this function returns the value of applying the second heuristic on the grid
  def heuristic2(self, grid):
    summation = sum(map(sum, grid))
    return max(self.goal-summation, 0)

  # this is the function that given a grid returns the max of both heuristics applied on it
  def heuristic3(self, grid):
    return max(self.heuristic1(grid), self.heuristic1(grid))

  # This function is used to model move Up in the game
  # returns grid after moving it up and score from the move
  # the move is done by rotating the grid to the left 1 times 
  # then applying move left and the rotating it back 3 times
  def operator_up(self, grid):
    """Move up"""
    originalGrid = grid
    grid = grid_ops.rotateGrid(grid,1)
    grid, cost = grid_ops.moveLeft2048(grid)
    if grid == None:
      return None, 0
    grid = grid_ops.rotateGrid(grid,3)
    grid = grid_ops.addTile(grid)
    return grid, cost

  # This function is used to model move Down in the game
  # returns grid after moving it down and score from the move
  # if the move doesn't change the state it returns None and 0
  # the move is done by rotating the grid to the left 3 times 
  # then applying move left and the rotating it back 1 times
  def operator_down(self, grid):
    """Move down"""
    originalGrid = grid
    grid = grid_ops.rotateGrid(grid,3)
    grid, cost = grid_ops.moveLeft2048(grid)
    if grid == None:
      return None, 0
    grid = grid_ops.rotateGrid(grid,1)
    grid = grid_ops.addTile(grid)
    return grid, cost

  # This function is used to model move Right in the game
  # returns grid after moving it right and score from the move
  # if the move doesn't change the state it returns None and 0
  # the move is done by rotating the grid to the left 2 times 
  # then applying move left and the rotating it back 2 times
  def operator_right(self, grid):
    """Move right"""
    originalGrid = grid
    grid = grid_ops.rotateGrid(grid,2)
    grid, cost = grid_ops.moveLeft2048(grid)
    if grid == None:
      return None, 0
    grid = grid_ops.rotateGrid(grid,2)
    grid = grid_ops.addTile(grid)
    return grid, cost

# if __name__ == "__main__":
#   p = TTFE(64)
#   # p.operator_left([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
#   # p.operator_left([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])
#   pass
