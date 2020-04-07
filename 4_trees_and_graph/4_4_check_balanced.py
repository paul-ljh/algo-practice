import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from bi_node import BiNode

def check_balanced(root):
  if root is None:
    return True
  else:
    return check_by_height(root) != -1

def check_by_height(root):
  if root.left_node is None and root.right_node is None:
    return 1
  left = 0 if root.left_node is None else check_by_height(root.left_node)
  right = 0 if root.right_node is None else check_by_height(root.right_node)
  if left == -1 or right == -1 or abs(left-right) > 1:
    return -1 
  else:
    return max(left, right) + 1

def test():
  t = None
  print('PASS' if check_balanced(t) else 'FAIL')

  t = BiNode(data=6)
  print('PASS' if check_balanced(t) else 'FAIL')

  t = BiNode(
    data=6,
    left_node=BiNode(data=7),
    right_node=BiNode(
      data=8,
      right_node=BiNode(data=9)
    )
  )
  print('PASS' if check_balanced(t) else 'FAIL')

  t = BiNode(
    data=6,
    left_node=BiNode(data=7),
    right_node=BiNode(
      data=9,
      left_node=BiNode(
        data=10,
        right_node=BiNode(data=11)
      ),
      right_node=BiNode(data=12)
    )
  )
  print('PASS' if not check_balanced(t) else 'FAIL')

  t = BiNode(
    data=6,
    left_node=BiNode(data=7),
    right_node=BiNode(
      data=9,
      left_node=BiNode(data=10),
      right_node=BiNode(
        data=12,
        left_node=BiNode(
          data=15,
          left_node=BiNode(data=11)
        )
      )
    )
  )
  print('PASS' if not check_balanced(t) else 'FAIL')

if __name__ == '__main__':
    test()
