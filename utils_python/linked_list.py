class Node:
  def __init__(self, data, next_node):
    self.data = data
    self.next_node = next_node

class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def add(self, index, data):
    if index > self.length:
      raise Exception('Invalid index')

    prev, curr = None, self.head
    i = 0
    while i < index:
      prev = curr
      curr = curr.next_node
      i += 1

    n = Node(data, curr)
    if index == 0:
      self.head = n
    else:
      prev.next_node = n

    self.length += 1

  def print(self):
    tmp = self.head
    while tmp != None:
      print(tmp.data)
      tmp = tmp.next_node

def test():
  l = LinkedList()
  l.add(0,1)
  l.add(0,2)
  l.add(1,3)
  l.print()

  try:
    l.add(4,4)
  except Exception as e:
    print(e)

if __name__ == '__main__':
  test()
