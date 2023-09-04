from math import log, floor
from queue import SimpleQueue

class MinHeap:
  class Node:
    def __init__(self, data=None, left=None, right=None):
      self.data = data
      self.left = left
      self.right = right

    def is_leaf(self):
      return self.left is None and self.right is None

    def is_single_parent(self):
      return not self.is_leaf() and (self.left is None or self.right is None)

  def __init__(self):
    self.root = None
    self.size = 0

  def peek(self):
    if self.root is None: raise IndexError
    return self.root.data

  def insert(self, data):
    node = self.Node(data)
    if self.root is None:
      self.root = node
      self.size += 1
      return

    direction_q = MinHeap.get_direction_to_node_at_index(self.size)
    another_direction_q = SimpleQueue()
    parent = self.root

    # Stop at the parent of the position you are trying to insert
    while direction_q.qsize() > 1:
      d = direction_q.get_nowait()
      another_direction_q.put_nowait(d)
      parent = parent.left if d == 0 else parent.right
    else:
      d = direction_q.get_nowait()
      another_direction_q.put_nowait(d)

    if d == 0:
      parent.left = node
    else:
      parent.right = node
    self.size += 1

    MinHeap.sort_heap(self.root, another_direction_q)
    return

  '''
  The idea here is to follow the direction queue items to locate the element that was previous inserted.
  As recusion calls pop off the stack, we swap parent and child if applicable.
  '''
  @staticmethod
  def sort_heap(root, queue):
    child = root.left if queue.get_nowait() == 0 else root.right
    if queue.empty():
      if child.data < root.data:
        temp = child.data
        child.data = root.data
        root.data = temp
        return True
      return False
    else:
      result = MinHeap.sort_heap(child, queue)
      '''
      If your child did not swap, then there is the min heap property is preserved automatically.
      If your child did swap, then you wanna check whether your child is smaller than you.
      '''
      if not result or root.data <= child.data:
        return result
      else:
        temp = child.data
        child.data = root.data
        root.data = temp
        return True

  def remove_min(self):
    if self.root is None:
      raise IndexError

    data_to_return = self.root.data
    if self.size == 1:
      self.root = None
      self.size -= 1
      return data_to_return

    parent = self.root
    directions = self.get_direction_to_node_at_index(self.size - 1)
    while directions.qsize() > 1:
      d = directions.get()
      parent = parent.left if d == 0 else parent.right

    d = directions.get()
    if d == 1:
      data_to_swap = parent.right.data
      parent.right = None
    else:
      data_to_swap = parent.left.data
      parent.left = None

    self.size -= 1
    self.root.data = data_to_swap
    MinHeap.sort_from_root_node(self.root)
    return data_to_return

  @staticmethod
  def sort_from_root_node(node):
    if node is None or node.is_leaf():
      return

    should_swap = node.data > node.left.data or (node.right and node.data > node.right.data)
    if not should_swap: return

    node_to_swap = node.left if node.is_single_parent() or node.left.data < node.right.data else node.right
    temp = node.data
    node.data = node_to_swap.data
    node_to_swap.data = temp
    return MinHeap.sort_from_root_node(node_to_swap)

  '''
  Returns a queue holds the instructions on how to travel from the root to the target node, 0 - left, 1 - right
  This function is based off the principle that:
  - left child index == parent index * 2 + 1
  - right child index == parent index * 2 + 2
  '''
  @staticmethod
  def get_direction_to_node_at_index(index):
    if index == 0:
      return SimpleQueue()
    direction = int(index % 2 == 0)
    parent_index = (index - (2 if direction else 1)) // 2
    queue = MinHeap.get_direction_to_node_at_index(parent_index)
    queue.put(direction)
    return queue

def queue_to_array(queue):
  result = []
  while not queue.empty(): result.append(queue.get_nowait())
  return result

def get_direction_to_node_at_index_test():
  test_data = {
    1: [0],
    2: [1],
    4: [0,1],
    5: [1,0],
    7: [0,0,0],
  }

  for k, v in test_data.items():
    print('PASS' if queue_to_array(MinHeap.get_direction_to_node_at_index(k)) == v else 'FAIL')

def insert_test():
  mh = MinHeap()
  for i in reversed(range(7)):
    mh.insert(i)
    print('PASS' if mh.peek() == i else 'FAIL')

def remove_min_test():
  mh = MinHeap()
  for i in range(7):
    mh.insert(i)

  for i in range(7):
    print('PASS' if mh.remove_min() == i else 'FAIL')

def test():
  get_direction_to_node_at_index_test()
  insert_test()
  remove_min_test()

if __name__ == '__main__':
  test()
