class StackNode:
  def __init__(self, data, next_node = None):
    self.data = data
    self.next_node = next_node

class Stack:
  def __init__(self):
    self.top = top

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
