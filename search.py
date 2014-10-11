import queue, adt
from decorators import queue_multi_insert

def general_search(problem, queue):
  queue.put(adt.Node(problem.initial_state, root=True))
  while not queue.empty():
    node = queue.get()
    if problem.goal_test(node.state):
      return node
    queue.put_many(node.expand(problem.operators))
    pass
  return None

def dfs(problem):
  return general_search(problem, queue_multi_insert(queue.LifoQueue)())

def bfs(problem):
  return general_search(problem, queue_multi_insert(queue.Queue)())

def greedy(problem, heuristic=lambda a: 0):
  return general_search(problem, GreedyQueue(heuristic))

def ids(problem):
  i = 0
  while True:
    q = LimitedDepthQueue(i)
    node = general_search(problem, q)
    if node != None:
      return node
    i += 1

search

@queue_multi_insert
class LimitedDepthQueue(queue.LifoQueue):
  def __init__(self, depth, *args, **kwargs):
    self.depth = depth
    super().__init__(*args, **kwargs)

  def put(self, node, *args, **kwargs):
    if node.depth > self.depth:
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
  print(greedy(p))
