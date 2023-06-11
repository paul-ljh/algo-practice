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

  def compare_to_array(self, target):
    if len(target) == 0 and self.head is None: return True

    l = self.head
    for i in range(len(target)):
      if target[i] != l.data: return False
      if i < len(target) - 1: l = l.next
    if l.next is not None:
      return False

    for i in reversed(range(len(target))):
      if target[i] != l.data: return False
      l = l.prev

    if l is not None:
      return False
    else:
      return True

  def __iter__(self):
    self.iter = self.head
    return self

  def __next__(self):
    if self.iter is None:
      raise StopIteration
    result = self.iter
    self.iter = self.iter.next
    return result

def test():
  l = DoublyLinkedList(list(range(4)))
  print('PASS' if l.compare_to_array(list(range(4))) else 'FAIL')

  try:
    l.remove(5)
  except KeyError as e:
    print('PASS')

  for index, node in enumerate(l):
    if index > 0: print('PASS' if node.prev.data == index - 1 else 'FAIL')
    print('PASS' if node.data == index else 'FAIL')
    if index < 3: print('PASS' if node.next.data == index + 1 else 'FAIL')

  print('PASS' if l.remove(0) == 0 else 'FAIL')
  print('PASS' if l.compare_to_array(list(range(1,4))) else 'FAIL')
  print('PASS' if l.remove(3) == 3 else 'FAIL')
  print('PASS' if l.compare_to_array(list(range(1,3))) else 'FAIL')
  print('PASS' if l.remove(2) == 2 else 'FAIL')
  print('PASS' if l.compare_to_array(list(range(1,2))) else 'FAIL')
  print('PASS' if l.remove(1) == 1 else 'FAIL')
  print('PASS' if l.compare_to_array(list(range(0))) else 'FAIL')

  try:
    l.remove(5)
  except KeyError as e:
    print('PASS')

if __name__ == '__main__':
  test()
