def general_search(problem, queue):
  queue.put(Node(problem.initial_state, root=True))
  while not queue.empty():
    node = queue.get()
    if problem.goal_test(node):
      return node
    queue.put_many(Node.create_many(problem.apply_operators(node.state), node))
    pass
  return None
