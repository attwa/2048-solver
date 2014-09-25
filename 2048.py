#!/usr/bin/env python3
class Node():
  def __init__(self, state):
    self.root = True
    self.state = state
    self.parent = state
    self.depth = 0
    self.path_cost = 0

  def __init__(self, state, parent, operator, depth, path_cost):
    self.root = True
    self.state = state
    self.parent = parent
    self.operator = operator
    self.depth = depth
    self.path_cost = path_cost

class Problem():
  def __init__(self, operators, init, state_space, goal_test, path_cost):
    self.operators = operators
    self.initial_state = initial_state
    self.state_space = state_space
    self.goal_test = goal_test
    self.path_cost = path_cost

def general_search(problem, queue):
  queue.put(Node(problem.initial_state))
  while not queue.empty():
    node = queue.get()
    if problem.goal_test(node):
      return node
    queue.put_many(Node.create_many(problem.apply_operators(node.state), node))
    pass
  return None
