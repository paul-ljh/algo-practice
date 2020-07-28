'''
You are given an array with all the numbers from 1 to N appearing exactly once, except for two numbers that are missing. How can you find the missing numbers in O(N) runtime and O(1) space?
'''

from math import sqrt, prod

def missing_two_bit_manipulation(arr):
  attendance = 0
  for elem in arr:
    mask = 1 << (elem - 1)
    attendance |= mask
  
  result = []
  for i in range(len(arr) + 2):
    mask = 1 << i
    if attendance | mask != attendance:
      result.append(i+1)
  return set(result)

def missing_two_algebra(arr):
  n = len(arr) + 2
  prod_diff = prod(range(1,n+1)) / prod(arr)
  sum_diff = sum(range(1,n+1)) - sum(arr)
  discriminant = sqrt(sum_diff ** 2 - 4 * prod_diff)
  return set([(sum_diff + discriminant) / 2, (sum_diff - discriminant) / 2])

def test():
  arr = [2,3,1,4,7,6]
  answer = set([5,8])
  print('PASS' if missing_two_algebra(arr) == missing_two_bit_manipulation(arr) == answer else 'FAIL')

  arr = [2,3,5,4,7,6,8]
  answer = set([1,9])
  print('PASS' if missing_two_algebra(arr) == missing_two_bit_manipulation(arr) == answer else 'FAIL')
  
  arr = []
  answer = set([1,2])
  print('PASS' if missing_two_algebra(arr) == missing_two_bit_manipulation(arr) == answer else 'FAIL')

if __name__ == "__main__":
  test()
  
