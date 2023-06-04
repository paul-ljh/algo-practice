class Node:
  def __init__(self, data, next_node = None):
    self.data = data
    self.next_node = next_node

class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0

  def __len__(self):
    return self.length

  def __contains__(self, data):
    l = self.head
    while l is not None:
      if l.data == data:
        return True
      l = l.next_node
    return False

  def __iter__(self):
    self.iter = self.head
    return self

  def __next__(self):
    if self.iter is not None:
      result = self.iter.data
      self.iter = self.iter.next_node
      return result
    raise StopIteration

  def to_array(self):
    result = []
    l = self.head
    while l is not None:
      result.append(l.data)
      l = l.next_node
    return result

  def append(self, data):
    n = Node(data)
    self.length += 1

    if self.head is None:
      self.head = n
      return

    l = self.head
    while l.next_node is not None:
      l = l.next_node
    l.next_node = n
    return

  def delete(self, data):
    l = self.head
    prev = None
    while l is not None:
      if l.data != data:
        prev = l
        l = l.next_node
        continue
      if prev is None:
        self.head = self.head.next_node
      else:
        prev.next_node = l.next_node
      self.length -= 1
      return
    raise IndexError('Not found')

  def add(self, index, data):
    if index > self.length:
      raise IndexError('Invalid index')

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
      raise IndexError('Invalid index')

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
  print('PASS' if 5 not in l else 'FAIL')

  l.append(4)
  print('PASS' if len(l) == 1 else 'FAIL')
  l.add(0,1)
  print('PASS' if len(l) == 2 else 'FAIL')
  l.add(0,2)
  print('PASS' if len(l) == 3 else 'FAIL')
  l.add(1,3)
  l.append(4)
  print('PASS' if l.to_array() == [2,3,1,4,4] else 'FAIL')

  result = [2,3,1,4,4]
  for i, data in enumerate(l):
    print('PASS' if data == result[i] else 'FAIL')

  print('PASS' if 2 in l else 'FAIL')
  print('PASS' if 5 not in l else 'FAIL')

  l.delete(4)
  print('PASS' if l.to_array() == [2,3,1,4] else 'FAIL')
  print('PASS' if len(l) == 4 else 'FAIL')
  l.delete(3)
  print('PASS' if l.to_array() == [2,1,4] else 'FAIL')
  print('PASS' if len(l) == 3 else 'FAIL')

  for i in [2,1,4]: l.delete(i)
  print('PASS' if l.to_array() == [] else 'FAIL')
  print('PASS' if len(l) == 0 else 'FAIL')

  try:
    l.delete(1)
  except IndexError as e:
    print('PASS' if str(e) == 'Not found' else 'FAIL')

  try:
    l.add(5,4)
  except IndexError as e:
    print('PASS' if str(e) == 'Invalid index' else 'FAIL')

  l.append(4)
  try:
    l.remove(1)
  except IndexError as e:
    print('PASS' if str(e) == 'Invalid index' else 'FAIL')

  l.remove(0)
  print('PASS' if l.to_array() == [] else 'FAIL')
  print('PASS' if len(l) == 0 else 'FAIL')

if __name__ == '__main__':
  test()
