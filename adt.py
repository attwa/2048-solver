#Abstract search tree class
class Node():
  def __init__(self, state, operator=None, parent=None,
      depth=0, path_cost=0, root=False):
    self.root = root
    self.state = state
    self.parent = parent
    self.operator = operator
    self.depth = depth
    self.path_cost = path_cost

#Abstract problem class
class Problem():
  def __init__(self, operators, initial_state, goal_test):
    self.operators = operators
    self.initial_state = initial_state
    self.goal_test = goal_test
