class StackNode:
  def __init__(self, data, next_node = None):
    self.data = data
    self.next_node = next_node

class Stack:
  def __init__(self):
    self.top = None

  def push(self, data):
    sn = StackNode(data, self.top)
    self.top = sn
    return True

  def pop(self):
    if self.top == None:
      raise IndexError

    value_to_return = self.top.data
    self.top = self.top.next_node
    return value_to_return

  def peek(self):
    if self.top == None:
      raise IndexError

    return self.top.data

  def is_empty(self):
    return self.top == None

def test():
  s = Stack()

  print('PASS' if s.is_empty() else 'FAIL')
  try:
    s.pop()
  except IndexError:
    pass

  try:
    s.peek()
  except IndexError:
    pass

  s.push(2)
  print('PASS' if s.peek() == 2 else 'FAIL')
  s.push(3)
  print('PASS' if s.peek() == 3 else 'FAIL')
  print('PASS' if s.pop() == 3 else 'FAIL')
  print('PASS' if s.pop() == 2 else 'FAIL')

  print('PASS' if s.is_empty() else 'FAIL')
  try:
    s.pop()
  except IndexError:
    pass

  try:
    s.peek()
  except IndexError:
    pass

if __name__ == '__main__':
  test()
