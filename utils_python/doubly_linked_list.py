class Node:
  def __init__(self, data, prev = None, next = None):
    self.data = data
    self.prev = prev
    self.next = next

class DoublyLinkedList:
  def __init__(self, arr = []):
    self.head = None
    self.length = 0

    for i in arr: self.append(i)

  def __len__(self):
    return self.length

  def append(self, e):
    self.length += 1
    n = Node(e)
    if self.head is None:
      self.head = n
      return

    l = self.head
    while l.next is not None:
      l = l.next
    n.prev = l
    l.next = n
    return

  def remove(self, e):
    l = self.head
    while l is not None:
      if l.data != e:
        l = l.next
        continue

      if l.prev is None:
        self.head = l.next
        if l.next is not None: l.next.prev = None
      else:
        l.prev.next = l.next
        if l.next is not None: l.next.prev = l.prev
      self.length -= 1
      return e
    raise KeyError(e)

def test():
  l = DoublyLinkedList(list(range(4)))

  try:
    l.remove(5)
  except KeyError as e:
    print('PASS')

  print('PASS' if l.remove(0) == 0 else 'FAIL')
  print('PASS' if l.remove(3) == 3 else 'FAIL')
  print('PASS' if l.remove(2) == 2 else 'FAIL')
  print('PASS' if l.remove(1) == 1 else 'FAIL')

  try:
    l.remove(5)
  except KeyError as e:
    print('PASS')

if __name__ == '__main__':
  test()
