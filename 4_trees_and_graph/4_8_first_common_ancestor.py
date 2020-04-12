import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from bi_node import BiNode

def first_common_ancestor(root, node1, node2):
  if node2 is None:
    return node1
  if node1 is None:
    return node2
  result, is_ans = first_common_ancestor_helper(root, node1, node2)
  return result if is_ans else None

def first_common_ancestor_helper(root, node1, node2):
  if root is None:
    return (root, False)
  left, l_is_ans = first_common_ancestor_helper(root.left_node, node1, node2)
  if l_is_ans:
    return (left, True)

  right, r_is_ans = first_common_ancestor_helper(root.right_node, node1, node2)
  if r_is_ans:
    return (right, True)

  if left is not None and right is not None:
    return (root, True)
  elif root is node1 or root is node2:
    return (root, left is not None or right is not None)
  else:
    return (left if left is not None else right, False)
  
def test():
  node1, node2 = BiNode(data=4), BiNode(data=4)
  print('PASS' if first_common_ancestor(None, node1, node2) is None else 'FAIL')
  print('PASS' if first_common_ancestor(node1, None, None) is None else 'FAIL')
  print('PASS' if first_common_ancestor(node1, None, node2) is node2 else 'FAIL')
  print('PASS' if first_common_ancestor(node1, node1, None) is node1 else 'FAIL')
 
  result = BiNode(
    data=8,
    left_node=node1,
    right_node=node2,
  )
  root = BiNode(
    data=6,
    left_node=result,
    right_node=BiNode(
      data=10,
      left_node=BiNode(data=5),
      right_node=BiNode(data=5),
    )
  )
  print('PASS' if first_common_ancestor(root, node1, node2) is result else 'FAIL')
  
  root = BiNode(
    data=6,
    left_node=BiNode(
      data=11,
      left_node=node1,
      right_node=BiNode(data=10),
    ),
    right_node=BiNode(
      data=10,
      left_node=BiNode(data=5),
      right_node=node2,
    )
  )
  print('PASS' if first_common_ancestor(root, node1, node2) is root else 'FAIL')

  node1 = BiNode(data=4)
  node2 = BiNode(
    data=4,
    left_node=node1,
  )
  root = BiNode(
    data=6,
    left_node=node2,
    right_node=BiNode(
      data=10,
      left_node=BiNode(data=5),
      right_node=BiNode(data=5),
    )
  )
  print('PASS' if first_common_ancestor(root, node1, node2) is node2 else 'FAIL')
  print('PASS' if first_common_ancestor(root, node1, BiNode(data=8)) is None else 'FAIL')
  print('PASS' if first_common_ancestor(root, BiNode(data=2), BiNode(data=8)) is None else 'FAIL')

if __name__ == '__main__':
    test()
