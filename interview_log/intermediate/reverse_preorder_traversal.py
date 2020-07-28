'''
Given an array that contains pre-order traversal result of a binary tree, construct the binary tree.

Note: NULL nodes are also included in the traversal result.

EX:
Tree                                  
      1                                                  
     / \                                                
    3   2                                       
   / \ / \                                 
  5  N N  N   
 / \
N   N

Pre-order
[1,3,5,None,None,2,None,None,None]
'''

import sys
sys.path.extend([
  "/Users/pauLi/Documents/Interviews/algo-practice/",
])

from bi_node import BiNode

def reverse_preorder_traversal(arr):
  if not arr:
    return None
  root = BiNode(data=arr[0])
  construct_tree(root, arr, 1)
  return root

def construct_tree(root, arr, index):
  if index == len(arr):
    return index
  if arr[index] is None:
    index += 1
  else:
    root.left_node = BiNode(data=arr[index])
    index = construct_tree(root.left_node, arr, index+1)
    
  if arr[index] is None:
    index += 1
  else:
    root.right_node = BiNode(data=arr[index])
    index = construct_tree(root.right_node, arr, index+1)
  return index

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
 
def test():
  arr = [1]
  print('PASS' if is_identical(reverse_preorder_traversal(arr), BiNode(data=1)) else 'FAIL')
  
  arr = [1,5,6,None,None,None,4,None,7,None,None]
  T = BiNode(
    data=1,
    left_node=BiNode(
      data=5,
      left_node=BiNode(data=6),
    ),
    right_node=BiNode(
      data=4,
      right_node=BiNode(data=7),
    )
  )
  print('PASS' if is_identical(reverse_preorder_traversal(arr), T) else 'FAIL')

if __name__ == '__main__':
  test()
