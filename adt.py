import pdb

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

  def expand(self, operators, update_state):
    new_nodes = []
    for operator in operators:
      new_state, cost = operator(self.state)
      if new_state is not None:
        for update in update_state:
          grid = update(new_state);
          node = Node(update(new_state), operator, self, self.depth+1, self.path_cost+cost)
          new_nodes.append(node)
    return new_nodes

#Abstract problem class
class Problem():
  def __init__(self, operators, initial_state, goal_test, update_state):
    self.operators = operators
    self.initial_state = initial_state
    self.goal_test = goal_test
    self.update_state = update_state
