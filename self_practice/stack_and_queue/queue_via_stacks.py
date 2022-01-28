class QueueViaStacks:
  def __init__(self):
    self.original = []
    self.tmp = []

  def is_empty(self):
    return len(self.original) == len(self.tmp) == 0

  def push(self, data):
    if len(self.tmp) > 0:
      self.reverse_items()

    self.original.append(data)
    return True

  def pop(self):
    if self.is_empty():
      raise IndexError

    if len(self.original) > 0:
      self.reverse_items()
    return self.tmp.pop()

  def peek(self):
    if self.is_empty():
      raise IndexError

    if len(self.original) > 0:
      self.reverse_items()
    return self.tmp[-1]

  def reverse_items(self):
    if self.is_empty():
      return

    if len(self.original) == 0:
      dst, src = self.original, self.tmp
    else:
      dst, src = self.tmp, self.original

    while len(src) > 0:
      dst.append(src.pop())
    return


def test():
  q = QueueViaStacks()
  q.push(1)
  print('PASS' if q.peek() == 1 else 'FAIL')

  q.push(2)
  print('PASS' if q.pop() == 1 else 'FAIL')
  print('PASS' if q.peek() == 2 else 'FAIL')

  q.push(3)
  print('PASS' if q.peek() == 2 else 'FAIL')
  print('PASS' if q.pop() == 2 else 'FAIL')
  print('PASS' if q.pop() == 3 else 'FAIL')

  try:
    q.peek()
  except IndexError:
    print('PASS')

if __name__ == '__main__':
  test()
