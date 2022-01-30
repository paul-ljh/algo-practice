import sys
sys.path.append('../../utils_python')

from binary_tree import BinaryTreeNode

def build_minimal_bst(arr):
  return build(arr, 0, len(arr) - 1)

def build(arr, start, end):
  if start > end:
    return None
  if start == end:
    return BinaryTreeNode(arr[start])

  mid_index = start + (end - start + 1) // 2
  left_subtree = build(arr, start, mid_index - 1)
  right_subtree = build(arr, mid_index + 1, end)
  return BinaryTreeNode(arr[mid_index], left_subtree, right_subtree)

def test():
  t = build_minimal_bst(list(range(7)))
  in_order_traveral(t)

def in_order_traveral(t):
  if t == None:
    return
  in_order_traveral(t.left_node)
  print(t.data)
  in_order_traveral(t.right_node)
  return

if __name__ == '__main__':
  test()
