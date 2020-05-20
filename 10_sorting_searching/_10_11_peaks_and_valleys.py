'''
In an array of integers, a peak is an element which is greater than or equal to its two adjacent integers, a valley is an element which is smaller than or equal to its two adjacent integers.

EX: [5,8,6,2,3,4]
Peaks: 8,4
Valleys: 5,2

Given an array of integers, sort it into an alternating sequence of peaks and valleys.
'''

def peaks_and_valleys(arr):
  prev = None #  unknown: None, peak: 1, valley: 0
  for i in range(1, len(arr)):
    if prev == 0:
      if arr[i] < arr[i-1]:
        swap(arr, i, i-1)
      prev = 1
    elif prev == 1:
      if arr[i] > arr[i-1]:
        swap(arr, i, i-1)
      prev = 0
    else:
      if arr[i] > arr[i-1]:
        prev = 1
      elif arr[i] < arr[i-1]:
        prev = 0
  return arr
  
def swap(arr, i, j):
  tmp = arr[i]
  arr[i] = arr[j]
  arr[j] = tmp
  
def test():
  arr = []
  print('PASS' if peaks_and_valleys(arr) == [] else 'FAIL')
  
  arr = [0]
  print('PASS' if peaks_and_valleys(arr) == [0] else 'FAIL')
  
  arr = [0,1]
  print('PASS' if peaks_and_valleys(arr) == [0,1] else 'FAIL')
  
  arr = [1,1,1,5,6,4,3,7]
  print('PASS' if peaks_and_valleys(arr) == [1,1,1,6,4,5,3,7] else 'FAIL')
  
  arr = [4,4,4,2,1,4,7,2]
  print('PASS' if peaks_and_valleys(arr) == [4,4,4,1,4,2,7,2] else 'FAIL')
  
  arr = [2,2,2,4,5,3,6,4,8]
  print('PASS' if peaks_and_valleys(arr) == [2,2,2,5,3,6,4,8,4] else 'FAIL')

if __name__ == '__main__':
  test()
