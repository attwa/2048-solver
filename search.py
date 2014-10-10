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

if __name__ == "__main__":
  import ttfe, sys
  p = ttfe.TTFE(int(sys.argv[1]))
  print(dfs(p))
