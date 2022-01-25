class MinStackNode:
  def __init__(self, data, minimum, next_node = None):
    self.data = data
    self.minimum = minimum
    self.next_node = next_node

class MinStack:
  def __init__(self):
    self.top = None

  def push(self, data):
    new_min = min(data, self.top.minimum) if self.top else data
    sn = MinStackNode(data, new_min, self.top)
    self.top = sn
    return True

  def pop(self):
    if self.top == None:
      raise IndexError

    value_to_return = self.top.data
    self.top = self.top.next_node
    return value_to_return

  def minimum(self):
    if self.top == None:
      raise IndexError
    return self.top.minimum

  def peek(self):
    if self.top == None:
      raise IndexError

    return self.top.data

  def is_empty(self):
    return self.top == None

def test():
  s = MinStack()

  print('PASS' if s.is_empty() else 'FAIL')
  try:
    s.pop()
  except IndexError:
    pass

  try:
    s.peek()
  except IndexError:
    pass

  s.push(1)
  s.push(2)
  print('PASS' if s.minimum() == 1 else 'FAIL')
  s.push(-1)
  print('PASS' if s.minimum() == -1 else 'FAIL')
  s.push(-1)
  print('PASS' if s.minimum() == -1 else 'FAIL')
  print('PASS' if s.pop() == -1 else 'FAIL')
  print('PASS' if s.minimum() == -1 else 'FAIL')
  print('PASS' if s.pop() == -1 else 'FAIL')
  print('PASS' if s.minimum() == 1 else 'FAIL')


if __name__ == '__main__':
  test()
