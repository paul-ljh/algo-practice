import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from bi_node import BiNode

def BST_sequences_helper(root):
  if root is None:
    return []
  left = BST_sequences_helper(root.left_node)
  right = BST_sequences_helper(root.right_node)
  if not left and not right:
    return [[root.data]]
  elif not left or not right:
    return list(map(lambda affix: [root.data] + affix, left if left else right))
  else:
    weaved = weave_all(left, right)
    return list(map(lambda affix: [root.data] + affix, weaved))

def weave_all(left, right):
  result = []
  for order_l in left:
    for order_r in right:
      weave(result, [], order_l, 0, order_r, 0)
  return result

def weave(result, prefix, arr1, index1, arr2, index2):
  if index1 == len(arr1):
    result.append(prefix + arr2[index2:])
    return
  if index2 == len(arr2):
    result.append(prefix + arr1[index1:])
    return
  one_arr = prefix + arr1[index1:index1+1]
  two_arr = prefix + arr2[index2:index2+1]
  weave(result, one_arr, arr1, index1+1, arr2, index2)
  weave(result, two_arr, arr1, index1, arr2, index2+1)
  return

def test():
  result = []
  weave(result, [], [1,2], 0, [3,4,5], 0)
  print('PASS' if result == [
    [1,2,3,4,5],
    [1,3,2,4,5],
    [1,3,4,2,5],
    [1,3,4,5,2],
    [3,1,2,4,5],
    [3,1,4,2,5],
    [3,1,4,5,2],
    [3,4,1,2,5],
    [3,4,1,5,2],
    [3,4,5,1,2],
  ] else 'FAIL')

  root = BiNode(
    data=8,
    left_node=BiNode(data=2),
    right_node=BiNode(data=10),
  )
  print('PASS' if BST_sequences_helper(root) == [[8,2,10], [8,10,2]] else 'FAIL')
  
  root = BiNode(
    data=8,
    left_node=BiNode(data=6),
    right_node=BiNode(
      data=12,
      left_node=BiNode(data=10),
      right_node=BiNode(
        data=14,
        right_node=BiNode(data=16),
      ),
    ),
  )
  print('PASS' if BST_sequences_helper(root) == [
    [8,6,12,10,14,16],
    [8,12,6,10,14,16],
    [8,12,10,6,14,16],
    [8,12,10,14,6,16],
    [8,12,10,14,16,6],
    [8,6,12,14,10,16],
    [8,12,6,14,10,16],
    [8,12,14,6,10,16],
    [8,12,14,10,6,16],
    [8,12,14,10,16,6],
    [8,6,12,14,16,10],
    [8,12,6,14,16,10],
    [8,12,14,6,16,10],
    [8,12,14,16,6,10],
    [8,12,14,16,10,6],
  ] else 'FAIL')


if __name__ == '__main__':
    test()
