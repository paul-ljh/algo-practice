from math import log, floor
from queue import SimpleQueue

class MinHeap:
  class Node:
    def __init__(self, data=None, left=None, right=None):
      self.data = data
      self.left = left
      self.right = right

  def __init__(self):
    self.root = None
    self.size = 0

  def peek(self):
    return self.root.data

  def insert(self, data):
    node = self.Node(data)
    if self.root is None:
      self.root = node
      self.size += 1
      return

    q = SimpleQueue()
    parent = self.find_rightmost_node_parent(self.root, self.size, q)
    if parent.left is None:
      parent.left = node
    else:
      parent.right = node
    self.size += 1

    self.sort_heap(self.root, q)
    return

  def find_rightmost_node_parent(self, root, size, direction_queue):
    if root.left is None or root.right is None:
      direction_queue.put(0 if root.left is None else 1)
      return root

    # 0 based
    num_level = floor(log(size, 2))
    num_nodes_above = pow(2, num_level) - 1
    num_nodes_last_level = pow(2, num_level)
    target_index = size - num_nodes_above

    '''
    The idea here is to determine whether to go left or right based on the number of nodes in the heap.
    Caculate:
    - the number of nodes on the last level of the heap
    - the index of the to-be-inserted node relative to the last level of the heap
    If index is in the left half, go left; if the index is in the right half, go right; if the index is equal to the node count, meaning the to-be-inserted node will go onto a new level, go left.

    Direction queue holds the instructions on how to traver from the root to the target node, 0 - left, 1 - right
    '''
    if target_index < num_nodes_last_level // 2:
      direction_queue.put(0)
      return self.find_rightmost_node_parent(root.left, (num_nodes_above - 1) // 2 + target_index, direction_queue)
    elif target_index == num_nodes_last_level:
      direction_queue.put(0)
      return self.find_rightmost_node_parent(root.left, (num_nodes_above - 1) // 2 + num_nodes_last_level // 2, direction_queue)
    else:
      direction_queue.put(1)
      return self.find_rightmost_node_parent(root.right, (num_nodes_above - 1) // 2 + target_index - num_nodes_last_level // 2, direction_queue)

  def sort_heap(self, root, queue):
    child = root.left if queue.get() == 0 else root.right
    if queue.empty():
      if child.data < root.data:
        temp = child.data
        child.data = root.data
        root.data = temp
        return True
      return False
    else:
      result = self.sort_heap(child, queue)
      if not result or root.data < child.data:
        return result
      else:
        temp = child.data
        child.data = root.data
        root.data = temp
        return True

def test():
  mh = MinHeap()

  for i in reversed(range(10)):
    mh.insert(i)
    print('PASS' if mh.peek() == i else 'FAIL')

if __name__ == '__main__':
  test()
