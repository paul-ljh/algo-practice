import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from bi_node import BiNode

def paths_with_sum(root, target):
  result = [0]
  compute_sum_map(root, target, result)
  return result[0]

def compute_sum_map(root, target, result):
  if root is None:
    return {}
  left = compute_sum_map(root.left_node, target, result) 
  right = compute_sum_map(root.right_node, target, result)
  current = combine_and_increment(left, right, root.data)
  result[0] += current.get(target, 0)
  return current

def combine_and_increment(left, right, additive):
  current = {}
  for key in left:
    current[key + additive] = left[key] + right.get(key, 0)
  
  for key in right:
    if key not in left:
      current[key + additive] = right[key]
  
  current[additive] = current.get(additive, 0) + 1
  return current

def test():
  root = None
  print('PASS' if paths_with_sum(root, 0) == 0 else 'FAIL')
  
  root = BiNode(
    data=10,
    left_node=BiNode(
      data=5,
      left_node=BiNode(
        data=0,
        left_node=BiNode(data=5),
        right_node=BiNode(data=5),
      ),
      right_node=BiNode(data=5),
    ),
    right_node=BiNode(
      data=-4,
      left_node=BiNode(
        data=20,
        left_node=BiNode(
          data=-6,
          right_node=BiNode(data=8),
        ),
        right_node=BiNode(data=10),
      ),
      right_node=BiNode(data=5),
    )
  )
  print('PASS' if paths_with_sum(root, 10) == 6 else 'FAIL')
  
  root = BiNode(
    data=5,
    left_node=BiNode(
      data=5,
      left_node=BiNode(
        data=0,
        left_node=BiNode(
          data=-1,
          left_node=BiNode(
            data=1,
            right_node=BiNode(data=3),
          ),
        ),
        right_node=BiNode(data=-5),
      ),
      right_node=BiNode(data=5),
    ),
    right_node=BiNode(
      data=10,
      left_node=BiNode(
        data=0,
        right_node=BiNode(data=2),
      ),
      right_node=BiNode(data=-5),
    )
  )
  print('PASS' if paths_with_sum(root, 10) == 7 else 'FAIL')

if __name__ == '__main__':
  test()
