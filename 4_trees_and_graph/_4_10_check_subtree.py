import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from bi_node import BiNode

def check_subtree(T1, T2):
  if T2 is None:
    return True
  return check(T1, T2)

def check(T1, T2):
  if T1 is None:
    return False
  if T1.data == T2.data and is_identical(T1, T2):
    return True
  return check(T1.left_node, T2) or check(T1.right_node, T2)

def is_identical(T1, T2):
  if T1 is None and T2 is None:
    return True
  if T1 is None or T2 is None or T1.data != T2.data:
    return False
  if not is_identical(T1.left_node, T2.left_node):
    return False
  if not is_identical(T1.right_node, T2.right_node):
    return False
  else:
    return True
  
def is_identical_test():
  T1 = BiNode(
    data=5,
    left_node=BiNode(data=9),
    right_node=BiNode(
      data=8,
      left_node=BiNode(data=7),
    )
  )
  print('PASS' if is_identical(T1, T1) else 'FAIL')
  
  T2 = BiNode(
    data=5,
    left_node=BiNode(data=9),
    right_node=BiNode(
      data=8,
      left_node=BiNode(data=10),
    )
  )
  print('PASS' if not is_identical(T1, T2) else 'FAIL')
  
  T2 = BiNode(
    data=5,
    left_node=BiNode(data=9),
    right_node=BiNode(
      data=8,
      right_node=BiNode(data=10),
    )
  )
  print('PASS' if not is_identical(T1, T2) else 'FAIL')
  
  T2 = BiNode(
    data=5,
    left_node=BiNode(data=9),
    right_node=BiNode(
      data=8,
      left_node=BiNode(
        data=7,
        left_node=BiNode(data=7),
      ),
    )
  )
  print('PASS' if not is_identical(T1, T2) else 'FAIL')

def test():
  T1 = BiNode(
    data=5,
    left_node=BiNode(
      data=9,
      left_node=BiNode(
        data=2,
        left_node=BiNode(data=1),
      ),
      right_node=BiNode(data=11),
    ),
    right_node=BiNode(
      data=8,
      left_node=BiNode(data=7),
      right_node=BiNode(
        data=10,
        right_node=BiNode(data=0),
      ),
    )
  )
  print('PASS' if check_subtree(T1, T1) else 'FAIL')
  
  T2 = BiNode(
    data=9,
    left_node=BiNode(
      data=2,
      left_node=BiNode(data=1),
    ),
    right_node=BiNode(data=11),
  )
  print('PASS' if check_subtree(T1, T2) else 'FAIL')
  
  T2 = BiNode(
    data=8,
    left_node=BiNode(data=7),
    right_node=BiNode(
      data=10,
      right_node=BiNode(data=11),
    ),
  )
  print('PASS' if not check_subtree(T1, T2) else 'FAIL')
  
  T2 = BiNode(
    data=8,
    left_node=BiNode(data=7),
    right_node=BiNode(data=10),
  )
  print('PASS' if not check_subtree(T1, T2) else 'FAIL')
  
  T2 = BiNode(data=0)
  print('PASS' if check_subtree(T1, T2) else 'FAIL')
  
  T2 = BiNode(data=10)
  print('PASS' if not check_subtree(T1, T2) else 'FAIL')

if __name__ == '__main__':
  is_identical_test()
  test()
