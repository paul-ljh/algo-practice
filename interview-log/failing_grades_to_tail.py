'''
Given an array of integer grades, move all the failing grades to the end of the array while maintaining the original order of the passing grades. The final order of failing grades does not matter.
'''

def failing_grade_to_tail(arr):
  if arr is None:
    return arr
  failing_index = None
  for index in range(0, len(arr)):
    if arr[index] < 50 and failing_index is None:
      failing_index = index
    elif arr[index] >= 50 and failing_index is not None:
      tmp = arr[index]
      arr[index] = arr[failing_index]
      arr[failing_index] = tmp
      failing_index += 1
  return arr

def test():
  print('PASS' if failing_grade_to_tail([]) == [] else 'FAIL')
  print('PASS' if failing_grade_to_tail([10,10,10,10]) == [10,10,10,10] else 'FAIL')
  print('PASS' if failing_grade_to_tail([80,80,80,80,80]) == [80,80,80,80,80] else 'FAIL')
  print('PASS' if failing_grade_to_tail([20,80,20,80,20,80,20]) == [80,80,80,20,20,20,20] else 'FAIL')

if __name__ == '__main__':
  test()
