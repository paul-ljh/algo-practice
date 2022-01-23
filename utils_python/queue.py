class QueueNode:
  def __init__(self, data, next_node = None):
    self.data = data
    self.next_node = next_node

class Queue:
  def __init__(self):
    self.first = None
    self.last = None

  def is_empty(self):
    return self.first == None

  def peek(self):
    if self.first == None:
      raise IndexError
    return self.first.data

  def add(self, data):
    n = QueueNode(data, self.last)
    if self.first == None:
      self.first, self.last = n, n
    else:
      self.last.next_node = n
      self.last = n
    return True

  def remove(self):
    if self.first == None:
      raise IndexError
    data_to_return = self.first.data
    self.first = self.first.next_node
    if self.first == None:
      self.last = None
    return data_to_return

def test():
  q = Queue()
  try:
    q.remove()
  except IndexError:
    pass

  try:
    q.peek()
  except IndexError:
    pass

  q.add(1)
  print('PASS' if q.peek() == 1 else 'FAIL')
  q.add(2)
  print('PASS' if q.peek() == 1 else 'FAIL')
  print('PASS' if q.remove() == 1 else 'FAIL')
  print('PASS' if q.peek() == 2 else 'FAIL')
  print('PASS' if q.remove() == 2 else 'FAIL')

  try:
    q.remove()
  except IndexError:
    pass

  try:
    q.peek()
  except IndexError:
    pass

if __name__ == '__main__':
  test()
