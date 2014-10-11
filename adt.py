import boardOperations

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

  def expand(self, operators):
    new_nodes = []
    for operator in operators:
      new_state, cost = operator(self.state)
      if new_state is not None:
        node = Node(new_state, operator, self, self.depth+1, self.path_cost+cost)
        new_nodes.append(node)
    return new_nodes

  def __lt__(self, node):
    return self.depth > node.depth

  def __str__(self):
    s = ""
    s += "depth={0} cost={1} expand_order={2}\n".format(self.depth,
        self.path_cost, self.expanded)
    s += boardOperations.displayGrid(self.state, ret=True)
    return s

#Abstract problem class
class Problem():
  def __init__(self, operators, initial_state, goal_test):
    self.operators = operators
    self.initial_state = initial_state
    self.goal_test = goal_test
