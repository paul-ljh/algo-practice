import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from bi_node import BiNode

def in_order_successor(n):
  if n is None:
    return None
  elif n.right_node is not None:
    return find_child_successor(n.right_node)
  else:
    return find_parent_successor(n)

def find_child_successor(n):
  while n.left_node is not None:
    n = n.left_node
  return n

def find_parent_successor(n):
  parent = n.parent
  while parent is not None and parent.data < n.data:
    n, parent = n.parent, parent.parent
  return parent

def test():
  t = None
  print('PASS' if in_order_successor(t) is None else 'FAIL')

  t = BiNode(data=6)
  print('PASS' if in_order_successor(t) is None else 'FAIL')

  result_node = BiNode(data=1)
  t = BiNode(
    data=6,
    right_node=BiNode(
      data=3,
      left_node=BiNode(
        data=2,
        left_node=result_node,
      ),
    )
  )
  print('PASS' if in_order_successor(t) is result_node else 'FAIL')

  grandparent = BiNode(data=5)
  parent = BiNode(data=2, parent=grandparent)
  son = BiNode(data=1, parent=parent)
  print('PASS' if in_order_successor(son) is parent else 'FAIL')
  
  grandparent = BiNode(data=2)
  parent = BiNode(data=5, parent=grandparent)
  son = BiNode(data=3, parent=parent)
  print('PASS' if in_order_successor(son) is parent else 'FAIL')

  result_node = BiNode(data=1)
  parent = BiNode(data=2, parent=result_node)
  son = BiNode(data=3, parent=parent)
  print('PASS' if in_order_successor(son) is None else 'FAIL')
  
  result_node = BiNode(data=5)
  parent = BiNode(data=2, parent=result_node)
  son = BiNode(data=3, parent=parent)
  print('PASS' if in_order_successor(son) is result_node else 'FAIL')

if __name__ == '__main__':
    test()

  