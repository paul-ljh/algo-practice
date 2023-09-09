'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''

def kth_smallest(root, k):
  result, _ = kth_helper(root, k)
  return result

'''
The idea here is:
1. try to find it in your left child first
2. if not, check yourself then your right child.
3. if found, job is done. Otherwise, tell your parent how many more does it have to find.
'''
def kth_helper(node, target):
  l_result, l_further = (None, target) if node.left is None else kth_helper(node.left, target)
  if l_further is None:
    return (l_result, l_further)
  elif l_further == 1:
    return (node.val, None)
  else:
    return (None, l_further - 1) if node.right is None else kth_helper(node.right, l_further - 1)

def kth_smallest_iteration(node, k):
  s, return_s = [], []
  s.append(node)
  i = 0
  while len(s) > 0:
    n = s.pop()
    return_s.append(n)
    if n.left:
      s.append(n.left)
      continue

    while len(return_s) > 0:
      r = return_s.pop()
      i += 1
      if i == k:
        return r.data
      if r.right:
        s.append(r.right)
        break
