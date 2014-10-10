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

def ids(problem):
	i = 0
	while True:
		node = general_search(problem, LimitedDepthQueue(i))
		if node != None:
			return node
		i += 1

@queue_multi_insert
class LimitedDepthQueue(queue.LifoQueue):
  def __init__(self, depth, *args, **kwargs):
    self.depth = depth
    super().__init__(*args, **kwargs)

  def put(self, node, *args, **kwargs):
    if node.depth > self.depth:
      return
    super().put(node, *args, **kwargs)

if __name__ == "__main__":
  import ttfe, sys
  p = ttfe.TTFE(int(sys.argv[1]))
  print(ids(p))
