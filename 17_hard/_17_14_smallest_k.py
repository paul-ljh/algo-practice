from random import randint

def smallest_k(arr, k):
  if k > len(arr):
    return False
  if k == 0:
    return []
  select(arr, k, 0, len(arr)-1)
  return arr[:k]
  
def select(arr, k, begin, end):
  pivot = partition(arr, begin, end)
  if pivot == k:
    return
  elif pivot < k:
    return select(arr, k-pivot, pivot, end)
  else:
    return select(arr, k, begin, begin+pivot-2)

def partition(arr, begin, end):
  pivot = randint(begin, end)
  pivot_value = arr[pivot]
  swap(arr, pivot, end)

  right = begin
  for i in range(begin, end):
    if arr[i] <= pivot_value and i >= right:
      swap(arr, right, i)
      right += 1
  swap(arr, end, right)
  return right-begin+1


def better_smallest_k(arr, k):
  if k > len(arr):
    return False
  if k == 0:
    return []
  better_select(arr, k, 0, len(arr)-1)
  return arr[:k]
  
def better_select(arr, k, begin, end):
  sm, pivot = better_partition(arr, begin, end)
  if sm <= k <= sm+pivot:
    return
  elif pivot+sm < k:
    return select(arr, k-pivot-sm, begin+pivot+sm, end)
  else:
    return select(arr, k, begin, begin+sm-1)

def better_partition(arr, begin, end):
  pivot = randint(begin, end)
  pivot_value = arr[pivot]
  swap(arr, pivot, begin)
  
  left, right, mid = begin, end, begin+1
  while mid <= right:
    if arr[mid] == pivot_value:
      mid += 1
    elif arr[mid] < pivot_value:
      swap(arr, mid, left)
      mid += 1
      left += 1
    else:
      swap(arr, right, mid)
      right -= 1
  return (left-begin, mid-left)

def swap(arr, pos1, pos2):
  tmp = arr[pos1]
  arr[pos1], arr[pos2] = arr[pos2], tmp
  
def test():
  k = 0
  print('PASS' if sorted(smallest_k([4,3,7,2,9,9,2,2], k)) == sorted(better_smallest_k([4,3,7,2,9,9,2,2], k)) == [] else 'FAIL')
  
  k = 8
  print('PASS' if sorted(smallest_k([4,3,7,2,9,9,2,2], k)) == sorted(better_smallest_k([4,3,7,2,9,9,2,2], k)) == [2,2,2,3,4,7,9,9] else 'FAIL')
  
  k = 1
  print('PASS' if sorted(smallest_k([4,3,7,2,9,9,2,2], k)) == sorted(better_smallest_k([4,3,7,2,9,9,2,2], k)) == [2] else 'FAIL')
  
  k = 3
  print('PASS' if sorted(smallest_k([4,3,7,2,9,9,2,2], k)) == sorted(better_smallest_k([4,3,7,2,9,9,2,2], k)) == [2,2,2] else 'FAIL')
  
  k = 5
  print('PASS' if sorted(smallest_k([4,3,7,2,9,9,2,2], k)) == sorted(better_smallest_k([4,3,7,2,9,9,2,2], k)) == [2,2,2,3,4] else 'FAIL')
  
  k = 7
  print('PASS' if sorted(smallest_k([4,3,7,2,9,9,2,2], k)) == sorted(better_smallest_k([4,3,7,2,9,9,2,2], k)) == [2,2,2,3,4,7,9] else 'FAIL')
  

if __name__ == '__main__':
  test()
