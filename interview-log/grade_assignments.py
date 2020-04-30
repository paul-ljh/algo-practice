'''
You need to grade student essays. You want to grade them in as few days as possible.

Rules:

* Each work day is exactly 8 hours long.
* Each essay takes between 1 and 7 hours to grade (inclusive.)
* Each essay must be marked to completion within a given day.

Write a function, AssignmentGrader, that returns the number of days it will take you to grade all the essays:

    int AssignmentGrader(int[] numOfEssays);
    
where numOfEssays is 7 elements long, numOfEssays[i] is the number of (i+1) hour essays.

Example: AssignmentGrader( [3, 1, 0, 3, 1, 0, 1] )

Correct, Optimal answer: 4

Day 1: 7, 1
Day 2: 5, 2, 1
Day 3: 4, 4
Day 4: 4, 1
'''

'''
1 7
2 6
3 5
4 4
'''

def grade_assignments(arr):
  result = 0
  for i in reversed(range(len(arr))):
    while arr[i] > 0:
      grade(arr, 8, i)
      result += 1
  return result

def grade(arr, leftover, i):
  if leftover == 0 or i == -1:
    return
  if arr[i] != 0:
    quotient = leftover // (i+1)
    leftover -= (min(quotient, arr[i]) * (i+1))
    arr[i] -= min(quotient, arr[i])
    i = leftover - 1
  else:
    i -= 1
  return grade(arr, leftover, i)

def test():
  arr = [4, 0, 0, 0]
  grade(arr, 4, 3)
  print('PASS' if arr == [0, 0, 0, 0] else 'FAIL')

  arr = [1, 1, 2, 0]
  grade(arr, 4, 3)
  print('PASS' if arr == [0, 1, 1, 0] else 'FAIL')

  arr = [0, 0, 0, 4]
  grade(arr, 8, 3)
  print('PASS' if arr == [0, 0, 0, 2] else 'FAIL')

  arr = [0] * 7
  print('PASS' if grade_assignments(arr) == 0 else 'FAIL')

  arr = [1] * 7
  print('PASS' if grade_assignments(arr) == 4 else 'FAIL')

  arr = [1, 1, 1, 2, 1, 1, 1]
  print('PASS' if grade_assignments(arr) == 4 else 'FAIL')

  arr = [3, 1, 0, 3, 1, 0, 1]
  print('PASS' if grade_assignments(arr) == 4 else 'FAIL')

  arr = [6, 5, 2, 3, 1, 1, 1]
  print('PASS' if grade_assignments(arr) == 7 else 'FAIL')


if __name__ == '__main__':
  test()
