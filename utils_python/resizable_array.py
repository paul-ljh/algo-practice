class ResizableArray:
  INIT_SIZE = 1

  def __init__(self, arr = []):
    self.array = [None] * self.INIT_SIZE
    self.capacity = 0

    for item in arr: self.add(item)

  def add(self, item):
    if self.capacity == len(self.array):
      self.array.extend([None] * len(self.array))
    self.array[self.capacity] = item
    self.capacity += 1
    return

def test():
  a = ResizableArray()
  for i in range(5):
    a.add(i)
  print('PASS' if a.array == [*range(5), *([None] * 3)] else 'FAIL')

  a = ResizableArray(list(range(3)))
  print('PASS' if a.array == [*range(3), None] else 'FAIL')

if __name__ == '__main__':
  test()
