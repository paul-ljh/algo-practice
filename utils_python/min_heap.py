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
    return self.root.data

  def insert(self, data):
    node = self.Node(data)
    if self.root is None:
      self.root = node
      self.size += 1
      return

    q = SimpleQueue()
    parent = self.find_leftmost_node_parent(self.root, self.size, q)
    if parent.left is None:
      parent.left = node
    else:
      parent.right = node
    self.size += 1

    self.sort_heap(self.root, q)
    return

  '''
  This function locates the parent node of the node of index "size" in a tree rooted at "root",
  returns a direction queue holds the instructions on how to traver from the root to the target node, 0 - left, 1 - right
  '''
  def find_leftmost_node_parent(self, root, size, direction_queue):
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
    '''
    if target_index < num_nodes_last_level // 2:
      direction_queue.put(0)
      return self.find_leftmost_node_parent(root.left, (num_nodes_above - 1) // 2 + target_index, direction_queue)
    elif target_index == num_nodes_last_level:
      direction_queue.put(0)
      return self.find_leftmost_node_parent(root.left, (num_nodes_above - 1) // 2 + num_nodes_last_level // 2, direction_queue)
    else:
      direction_queue.put(1)
      return self.find_leftmost_node_parent(root.right, (num_nodes_above - 1) // 2 + target_index - num_nodes_last_level // 2, direction_queue)

  def find_node_parent_by_index(self, node, index, direction_queue):
    num_level = floor(log(index, 2))
    num_nodes_above = pow(2, num_level) - 1
    num_nodes_last_level = pow(2, num_level)
    target_index = index - num_nodes_above

    if target_index < num_nodes_last_level // 2:
      new_node, new_index, direction = node.left, (num_nodes_above - 1) // 2 + target_index, 0
    elif target_index == num_nodes_last_level:
      new_node, new_index, direction = node.left, (num_nodes_above - 1) // 2 + num_nodes_last_level // 2, 0
    else:
      new_node, new_index, direction = node.right, (num_nodes_above - 1) // 2 + target_index - num_nodes_last_level // 2, 1

    if new_index == 0:
      return node
    else:
      direction_queue.put(direction)
      return self.find_node_parent_by_index(new_node, new_index, direction_queue)

  '''
  The idea here is to follow the direction queue items to locate the element that was previous inserted.
  As recusion calls pop off the stack, we swap parent and child if applicable.
  '''
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
    # self.sort_from_root_node(self.root)
    return data_to_return

  def sort_from_root_node(self, node):
    if node is None or node.is_leaf():
      return

    should_swap = node.data > node.left.data or (node.right and node.data > node.right.data)
    if not should_swap: return

    node_to_swap = node.left if node.is_single_parent() or node.left.data < node.right.data else node.right
    temp = node.data
    node.data = node_to_swap.data
    node_to_swap.data = temp
    return self.sort_from_root_node(node_to_swap)

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

def test():
  get_direction_to_node_at_index_test()

if __name__ == '__main__':
  test()
