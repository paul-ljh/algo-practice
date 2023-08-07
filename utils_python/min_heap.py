from math import log, floor

class MinHeap:
  class Node:
    def __init__(self, data=None, left=None, right=None):
      self.data = data
      self.left = left
      self.right = right

  def __init__(self):
    self.root = None
    self.size = 0

  def insert(self, data):
    node = self.Node(data)
    if self.root is not None:
      self.root = node
      self.size += 1
      return

    parent = self.find_rightmost_node_parent(self.root, self.size)
    if parent.left is None:
      parent.left = node
    else:
      parent.right = node
    self.size += 1
    return

  def find_rightmost_node_parent(self, root, size):
    if root.left is None or root.right is None:
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
      return self.find_rightmost_node_parent(root.left, (num_nodes_above - 1) // 2 + target_index)
    elif target_index == num_nodes_last_level:
      return self.find_rightmost_node_parent(root.left, (num_nodes_above - 1) // 2 + num_nodes_last_level // 2)
    else:
      return self.find_rightmost_node_parent(root.left, (num_nodes_above - 1) // 2 + target_index - num_nodes_last_level // 2)
