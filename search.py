import queue, adt, ttfe, random
from decorators import queue_multi_insert
import grid_ops

def general_search(problem, queue):
  num_expanded = 0
  visited = set()
  queue.put(adt.Node(problem.initial_state, root=True))
  while not queue.empty():
    node = queue.get()
    if str(node.state) in visited:
      continue
    visited.add(str(node.state))
    num_expanded += 1
    node.expanded = num_expanded
    print(node, problem.heuristics[0](node.state))
    if problem.goal_test(node.state):
      return node, num_expanded
    queue.put_many(node.expand(problem.operators))
    pass
  return None, num_expanded

def dfs(problem):
  return general_search(problem, queue_multi_insert(queue.LifoQueue)())

def bfs(problem):
  return general_search(problem, queue_multi_insert(queue.Queue)())

def greedy(problem, heuristic_id):
  return general_search(problem, GreedyQueue(problem.heuristics[heuristic_id]))

def ids(problem):
  i = 0
  total_expanded = 0
  while True:
    q = LimitedDepthQueue(i)
    node, expanded = general_search(problem, q)
    total_expanded += expanded
    if node != None:
      return node, total_expanded
    if not q.hit_max:
      return None, total_expanded
    i += 1

def astar(problem, heuristic_id):
	return general_search(problem, AStarQueue(problem.heuristics[heuristic_id]))

@queue_multi_insert
class LimitedDepthQueue(queue.LifoQueue):
  def __init__(self, depth, *args, **kwargs):
    self.depth = depth
    self.hit_max = False
    super().__init__(*args, **kwargs)

  def put(self, node, *args, **kwargs):
    if node.depth > self.depth:
      self.hit_max = True
      return
    super().put(node, *args, **kwargs)

@queue_multi_insert
class GreedyQueue(queue.PriorityQueue):
  def __init__(self, heuristic, *args, **kwargs):
    self.heuristic = heuristic
    super().__init__(*args, **kwargs)

  def put(self, node, *args, **kwargs):
    super().put((self.heuristic(node.state), node), *args, **kwargs)

  def get(self, *args, **kwargs):
    h, node = super().get(*args, **kwargs)
    return node

@queue_multi_insert
class AStarQueue(queue.PriorityQueue):
	def __init__(self, heuristic, *args, **kwargs):
		self.heuristic = heuristic
		super().__init__(*args, **kwargs)

	def put(self, node, *args, **kwargs):
		super().put((self.heuristic(node.state) + node.path_cost, node),
        *args, **kwargs)

	def get(self, *args, **kwargs):
		f, node = super().get(*args, **kwargs)
		return node

def visualize_solution(node):
  solution = [node]
  while not node.root:
    solution.append(node.parent)
    node = node.parent
  solution.reverse()
  for node in solution:
    if not node.root:
      print(node.operator.__doc__, end="\n\n")
    print(node)

def Search(grid, M, strategy, visualize=False):
  problem = ttfe.TTFE(M, grid)
  if strategy == "BF":
    solution, expanded = bfs(problem)
  elif strategy == "DF":
    solution, expanded = dfs(problem)
  elif strategy == "ID":
    solution, expanded = ids(problem)
  elif strategy == "GR1":
    solution, expanded = greedy(problem, 0)
  elif strategy == "GR2":
    solution, expanded = greedy(problem, 1)
  elif strategy == "GR3":
    solution, expanded = greedy(problem, 2)
  elif strategy == "AS1":
    solution, expanded = astar(problem, 0)
  elif strategy == "AS2":
    solution, expanded = astar(problem, 1)
  elif strategy == "AS3":
    solution, expanded = astar(problem, 2)
  else:
    raise Exception("%s is not a valid strategy"%(strategy, ))
  if visualize:
    visualize_solution(solution)
  return solution, solution.path_cost, expanded

if __name__ == "__main__":
  import sys
  M = int(sys.argv[1])
  random.seed(M)
  solution, cost,  expanded = Search(grid_ops.GenGrid(), M, sys.argv[2], False)
  print("Path length=%i, cost=%i, number of expanded nodes=%i"%(solution.depth,
      cost, expanded))
