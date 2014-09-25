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

  def operator_up(self, grid):
    pass
  def operator_down(self, grid):
    pass
  def operator_left(self, grid):
    pass
  def operator_right(self, grid):
    pass

#generates a grid and sets two random cells to 2
def GenGrid(rows=4, cols=4):
  grid = [[0]*cols for x in range(rows)]
  grid[randint(0, rows-1)][randint(0, cols-1)] = 2;
  #FIXME may generate same row and col
  grid[randint(0, rows-1)][randint(0, cols-1)] = 2;
  return grid

if __name__ == "__main__":
  p = TTFE(2048)
  pass
