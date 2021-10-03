def binary_search_recur(arr, begin, end, target):
  if end < begin:
    return -1
  mid = (end + begin) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] > target:
    return binary_search_recur(arr, begin, mid-1, target)
  else:
    return binary_search_recur(arr, mid+1, end, target)

def binary_search_iter(arr, target):
  if not arr:
    return -1
  begin, end = 0, len(arr)-1
  
  while end >= begin:
    mid = (begin + end) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      begin = mid+1
    else:
      end = mid-1
  return -1

def binary_search(arr, target):
  if not arr:
    return -1
  else:
    return binary_search_recur(arr, 0, len(arr)-1, target)
  
def test():
  arr = [1,4,5,6,7,8,9]
  print('PASS' if binary_search(arr, 1) == binary_search_iter(arr, 1) == 0 else 'FAIL')
  print('PASS' if binary_search(arr, 8) == binary_search_iter(arr, 8) == 5 else 'FAIL')
  print('PASS' if binary_search(arr, -1) == binary_search_iter(arr, -1) == -1 else 'FAIL')
  
  arr = [1,4,6,7]
  print('PASS' if binary_search(arr, 0) == binary_search_iter(arr, 0) == -1 else 'FAIL')
  print('PASS' if binary_search(arr, 5) == binary_search_iter(arr, 5) == -1 else 'FAIL')

if __name__ == '__main__':
    test()
