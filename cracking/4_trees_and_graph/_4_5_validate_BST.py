import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from bi_node import BiNode

def validate_BST(root):
  if root is None:
    return True
  else:
    result = validate_BST_helper(root)
    return result[0] != False

def validate_BST_helper(root):
  if root.left_node is None and root.right_node is None:
    return (root.data, root.data)

  if root.left_node is None:
    l_s, l_b = (root.data, root.data)
  else:
    l_s, l_b = validate_BST_helper(root.left_node)
    if l_s is False: return (False, False)

  if root.right_node is None:
    r_s, r_b = (root.data, root.data)
  else:
    r_s, r_b = validate_BST_helper(root.right_node)
    if r_s is False: return (False, False)

  if l_b <= root.data <= r_s:
    return (l_s, r_b)
  else:
    return (False, False)


def validate_BST_alternative(root):
  return validate_BST_alternative_helper(root, None, None)
  
def validate_BST_alternative_helper(root, min, max):
  if root is None:
    return True
  if (min is not None and root.data < min) or (max is not None and root.data > max):
    return False
  elif (not validate_BST_alternative_helper(root.left_node, min, root.data)) or (not validate_BST_alternative_helper(root.right_node, root.data, max)):
    return False
  else:
    return True


def test():
  t = None
  print('PASS' if validate_BST(t) else 'FAIL')
  print('PASS' if validate_BST_alternative(t) else 'FAIL')

  t = BiNode(data=6)
  print('PASS' if validate_BST(t) else 'FAIL')
  print('PASS' if validate_BST_alternative(t) else 'FAIL')

  t = BiNode(
    data=6,
    left_node=BiNode(data=7),
    right_node=BiNode(
      data=8,
      right_node=BiNode(data=7)
    )
  )
  print('PASS' if not validate_BST(t) else 'FAIL')
  print('PASS' if not validate_BST_alternative(t) else 'FAIL')

  t = BiNode(
    data=6,
    left_node=BiNode(data=7),
    right_node=BiNode(
      data=9,
      left_node=BiNode(
        data=5,
        right_node=BiNode(data=10)
      ),
      right_node=BiNode(data=12)
    )
  )
  print('PASS' if not validate_BST(t) else 'FAIL')
  print('PASS' if not validate_BST_alternative(t) else 'FAIL')

  t = BiNode(
    data=10,
    left_node=BiNode(data=2),
    right_node=BiNode(
      data=15,
      left_node=BiNode(data=13),
      right_node=BiNode(
        data=17,
        left_node=BiNode(data=16)
      )
    )
  )
  print('PASS' if validate_BST(t) else 'FAIL')
  print('PASS' if validate_BST_alternative(t) else 'FAIL')

if __name__ == '__main__':
    test()
