'''
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.
'''
from sys import maxsize

def smallest_difference(l1, l2):
  if not l1 or not l2:
    return None
  
  l1.sort()
  l2.sort()
  difference = maxsize
  l1_index, l2_index = 0, 0
  while difference != 0 and l1_index < len(l1) and l2_index < len(l2):
    difference = min(difference, abs(l1[l1_index] - l2[l2_index]))
    if l2[l2_index] > l1[l1_index]:
      l1_index += 1
    else:
      l2_index += 1

  return difference

def test():
  l1 = []
  l2 = [1,2,3]
  answer = None
  print('PASS' if smallest_difference(l1, l2) == answer else 'FAIL')
  
  l1 = []
  l2 = []
  answer = None
  print('PASS' if smallest_difference(l1, l2) == answer else 'FAIL')
  
  l1 = [9]
  l2 = [23,127,235,10,8]
  answer = 1
  print('PASS' if smallest_difference(l1, l2) == answer else 'FAIL')
  
  l1 = [-12]
  l2 = [-10,127,235,10,8]
  answer = 2
  print('PASS' if smallest_difference(l1, l2) == answer else 'FAIL')
  
  l1 = [1,3,15,11,9]
  l2 = [23,127,235,10,8]
  answer = 1
  print('PASS' if smallest_difference(l1, l2) == answer else 'FAIL')
  
  l1 = [-11,1,3,235,11,-9]
  l2 = [-10,127,235,10,8]
  answer = 0
  print('PASS' if smallest_difference(l1, l2) == answer else 'FAIL')

if __name__ == "__main__":
  test()
  
  