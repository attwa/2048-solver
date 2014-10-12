import queue, adt, ttfe
from decorators import queue_multi_insert
import grid_ops

def general_search(problem, queue):
  num_expanded = 0
  queue.put(adt.Node(problem.initial_state, root=True))
  while not queue.empty():
    node = queue.get()
    num_expanded += 1
    node.expanded = num_expanded
    #print(node, problem.heuristics[0](node.state))
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
  def __init__(self, heuristic=lambda a: 0, *args, **kwargs):
    self.heuristic = heuristic
    super().__init__(*args, **kwargs)

  def put(self, node, *args, **kwargs):
    super().put((self.heuristic(node.state), node), *args, **kwargs)

  def get(self, *args, **kwargs):
    h, node = super().get(*args, **kwargs)
    return node

if __name__ == "__main__":
  import ttfe, sys
  p = ttfe.TTFE(int(sys.argv[1]))
  solution, expanded = greedy(p, 0)
  print(solution)
