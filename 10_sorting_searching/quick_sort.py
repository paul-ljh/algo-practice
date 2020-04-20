from random import randint

def quick_sort(arr):
  if len(arr) > 1:
    sort_helper(arr, 0, len(arr)-1)
  return arr

def sort_helper(arr, begin, end):
  pivot = partition(arr, begin, end)
  if pivot > begin:
    sort_helper(arr, begin, pivot-1)
  if pivot < end:
    sort_helper(arr, pivot+1, end)

def partition(arr, begin, end):
  pivot_index = randint(begin, end)
  mid = None
  for i in range(begin, end+1):
    if arr[i] > arr[pivot_index] and mid is None:
      mid = i
    elif arr[i] < arr[pivot_index] and mid is not None:
      swap(arr, mid, i)
      mid += (2 if mid + 1 == pivot_index else 1)
  
  # pivot is the biggest element
  if mid is None:
    swap(arr, end, pivot_index)
    return end
  elif pivot_index >= mid: 
    swap(arr, mid, pivot_index)
    return mid
  else:
    swap(arr, mid-1, pivot_index)
    return mid-1
      
def swap(arr, pos1, pos2):
  tmp = arr[pos1]
  arr[pos1] = arr[pos2]
  arr[pos2] = tmp
  
def test():
  arr = []
  print('PASS' if quick_sort(arr) == sorted(arr) else 'FAIL')
  
  arr = [1]
  print('PASS' if quick_sort(arr) == sorted(arr) else 'FAIL')
  
  arr = [3,2,1]
  print('PASS' if quick_sort(arr) == sorted(arr) else 'FAIL')
 
  arr = [5,5,5,5,5,10,10,10,10,10]
  print('PASS' if quick_sort(arr) == sorted(arr) else 'FAIL')
  
  arr = [15,15,15,15,15,10,10,10,10,10]
  print('PASS' if quick_sort(arr) == sorted(arr) else 'FAIL')
  
  arr = [15,9,12,8,6,5,13,14,10,20]
  print('PASS' if quick_sort(arr) == sorted(arr) else 'FAIL') 


if __name__ == '__main__':
    test()
