'''
https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/
'''
from sys import maxsize

class Solution:
  class TreeNode:
    def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

  def __init__(self, root):
    self.max_so_far = 0
    self.root = root
    self.tree = self.build_tree(0)
    self.find_max_sum(self.tree)

  def build_tree(self, index):
    if self.root[index] is None:
      return None
    l_index, r_index = index * 2 + 1, (index + 1) * 2
    left_node = self.build_tree(l_index) if l_index < len(self.root) else None
    right_node = self.build_tree(r_index) if r_index < len(self.root) else None
    return self.TreeNode(self.root[index], left_node, right_node)

  def find_max_sum(self, tree):
    if tree is None:
      # min, max, sum
      return maxsize, -maxsize, 0

    left = self.find_max_sum(tree.left)
    right = self.find_max_sum(tree.right)

    if left is None or right is None or tree.val < left[1] or tree.val > right[0]:
      return None

    self_sum = sum([left[-1], right[-1], tree.val])
    self.max_so_far = max(self.max_so_far, self_sum)
    self_min = min(tree.val, left[0])
    self_max = max(tree.val, right[1])
    return self_min, self_max, self_sum

  def max_sum(self):
    return self.max_so_far
