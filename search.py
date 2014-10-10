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
	
def dls(problem, queue, depth):
	queue.put(adt.Node(problem.initial_state, root=True))
	while not queue.empty():
	  node = queue.get()
	  if node.depth > depth:
	  	continue
	  if problem.goal_test(node.state):
	    return node
	  queue.put_many(node.expand(problem.operators))
	  pass
	return None	

def ids(problem):
	i = 0
	while True:
		node = dls(problem, queue_multi_insert(queue.LifoQueue)(), i)
		if node != None:
			return node
		i += 1

if __name__ == "__main__":
  import ttfe, sys
  p = ttfe.TTFE(int(sys.argv[1]))
  print(dfs(p))
