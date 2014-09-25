# class decorator for queue.Queue derived classes to add method to queue
# multiple items at the same time
def queue_multi_insert(cls):
  class MultiQueue(cls):
    def put_many(self, items, *args, **kwargs):
      for item in items:
        self.put(item, *args, **kwargs)
  return MultiQueue
