import grid_ops, random

#Abstract search tree class
class Node():
  # this is the constructor of the node class
  # it takes the state of the node(grid), the operator from the parent node,
  # the parent node it self, depth of the current node, path cost from root 
  # and whether it is root or not
  def __init__(self, state, operator=None, parent=None,
      depth=0, path_cost=0, root=False):
    self.root = root
    self.state = state
    self.parent = parent
    self.operator = operator
    self.depth = depth
    self.path_cost = path_cost

  # this is the function that is used to generate new nodes from a current node
  # it takes the list of valid operators as input
  def expand(self, operators):
    new_nodes = []
    for operator in operators:
      new_state, cost = operator(self.state)
      if new_state is not None:
        node = Node(new_state, operator, self, self.depth+1, self.path_cost+16-cost)
        new_nodes.append(node)
    return new_nodes

  def __lt__(self, node):
    return False

  # this is used to model the node as a string to be used for printing
  def __str__(self):
    s = ""
    s += grid_ops.displayGrid(self.state, ret=True)
    s += "depth={0} cost={1} expand_order={2}\n".format(self.depth,
        self.path_cost, self.expanded)
    return s

#Abstract problem class
class Problem():
  # this is the constructor for the problem class
  # it takes as input all the valid operators functions,
  # all heuristics functions, initial state and 
  # the goal test function
  def __init__(self, operators, heuristics, initial_state, goal_test):
    self.operators = operators
    self.heuristics = heuristics
    self.initial_state = initial_state
    self.goal_test = goal_test


from ttfe import TTFE
