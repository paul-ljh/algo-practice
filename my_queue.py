from uni_node import UniNode

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def push(self, data):
    new_last = UniNode(data)
    if self.last is not None:
      self.last.next_node = new_last
    self.last = new_last

    if self.first is None:
      self.first = new_last
    self.length += 1

  def pop(self):
    if self.is_empty(): raise IndexError("EMPTY QUEUE")
    data_to_pop = self.first.data
    self.first = self.first.next_node
    if self.first is None: self.last = None
    self.length -= 1
    return data_to_pop

  def is_empty(self):
    return self.first is None

  def peek(self):
    if self.is_empty(): raise IndexError("EMPTY QUEUE")
    return self.first.data

def test():
  q = Queue()
  q.push(5)
  print('PASS' if q.peek() == 5 else 'FAIL')
  print('PASS' if q.is_empty() == False else 'FAIL')
  print('PASS' if q.length == 1 else 'FAIL')

  q.push(4)
  print('PASS' if q.peek() == 5 else 'FAIL')
  print('PASS' if q.is_empty() == False else 'FAIL')
  print('PASS' if q.length == 2 else 'FAIL')

  print('PASS' if q.pop() == 5 else 'FAIL')
  print('PASS' if q.is_empty() == False else 'FAIL')
  print('PASS' if q.length == 1 else 'FAIL')

  print('PASS' if q.pop() == 4 else 'FAIL')
  print('PASS' if q.is_empty() else 'FAIL')
  print('PASS' if q.length == 0 else 'FAIL')


if __name__ == '__main__':
  test()
