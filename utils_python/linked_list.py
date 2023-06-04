class Node:
  def __init__(self, data, next_node = None):
    self.data = data
    self.next_node = next_node

class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def append(self, data):
    n = Node(data)
    self.length += 1

    if self.head is None:
      self.head = n
      self.length += 1

    l = self.head
    while l.next_node is not None:
      l = l.next_node
    l.next_node = n
    return

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
    return True

  def remove(self, index):
    if index >= self.length:
      raise Exception('Invalid index')

    prev, curr = None, self.head
    i = 0
    while i < index:
      prev = curr
      curr = curr.next_node
      i += 1

    return_data = curr.data
    if index == 0:
      self.head = curr.next_node
    else:
      prev.next_node = curr.next_node

    self.length -= 1
    return return_data

  def print(self):
    tmp = self.head
    while tmp != None:
      print(tmp.data)
      tmp = tmp.next_node
    print('None')

def test():
  l = LinkedList()
  l.add(0,1)
  l.add(0,2)
  l.add(1,3)
  l.append(4)
  l.print()

  try:
    l.add(5,4)
  except Exception as e:
    print(e)

  l.remove(0)
  l.remove(1)

  try:
    l.remove(1)
  except Exception as e:
    print(e)

  l.remove(0)
  l.print()

if __name__ == '__main__':
  test()
