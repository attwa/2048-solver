def general_search(problem, queue):
  queue.put(Node(problem.initial_state, root=True))
  while not queue.empty():
    node = queue.get()
    if problem.goal_test(node):
      return node
    queue.put_many(node.expand(problem.operators))
    pass
  return None
