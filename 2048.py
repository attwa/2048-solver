#!/usr/bin/env python3
import sys, os
from random import randint
from adt import Node, Problem
from search import general_search

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

#doc lines are used to get a human readable description of the action
#each operator returns a new state and a cost

  def operator_up(self, grid):
    """Move up"""
    pass
  def operator_down(self, grid):
    """Move down"""
    pass
  def operator_left(self, grid):
    """Move left"""
    pass
  def operator_right(self, grid):
    """Move right"""
    pass

#generates a grid and sets two random cells to 2
def GenGrid(rows=4, cols=4):
  grid = [[0]*cols for x in range(rows)]

  # checks that there are two '2's in the grid
  # protects against problem where the random values for row and col are the same
  while len(str(grid).split("2")) < 3:
    grid[randint(0, rows-1)][randint(0, cols-1)] = 2;
    grid[randint(0, rows-1)][randint(0, cols-1)] = 2;
  return grid

if __name__ == "__main__":
  p = TTFE(2048)
  pass
