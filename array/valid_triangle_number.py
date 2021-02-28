'''
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3

Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].

https://leetcode.com/problems/valid-triangle-number/
'''

def valid_triangle_number(arr):
  arr.sort()
  result = 0
  for i in reversed(range(2, len(arr))):
    search_index = 0
    for j in reversed(range(1, i)):
      threshold = arr[i] - arr[j]
      while arr[search_index] <= threshold and search_index < j:
        search_index += 1
      if search_index == j:
        break
      else:
        result += (j - search_index)
  return result

def test():
  inputs = [
    [],
    [1],
    [1,2],
    [1,2,3],
    [2,2,3,4],
    [3,4,4,6,7],
  ]

  answers = [0,0,0,0,3,8]

  for i in range(len(answers)):
    print('PASS' if valid_triangle_number(inputs[i]) == answers[i] else 'FAIL')

if __name__ == "__main__":
  test()
