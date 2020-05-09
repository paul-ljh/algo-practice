def sparse_search(arr, target):
  return binary_search(arr, target, 0, len(arr)-1)

def binary_search(arr, target, left, right):
  if left > right:
    return -1
  mid = (left+right) // 2
  if target == arr[mid]:
    return mid
  elif arr[mid] == '':
    l = binary_search(arr, target, left, mid-1)
    if l != -1:
      return l
    return binary_search(arr, target, mid+1, right)
  elif target < arr[mid]:
    return binary_search(arr, target, left, mid-1)
  else:
    return binary_search(arr, target, mid+1, right)

def test():
  arr = []
  target = ''
  print('PASS' if sparse_search(arr, target) == -1 else 'FAIL')
  
  arr = ['a','b','','d','e','','','','','','']
  target = 'd'
  print('PASS' if sparse_search(arr, target) == 3 else 'FAIL')
  
  arr = ['','','','','','','','','','','','','d']
  target = 'd'
  print('PASS' if sparse_search(arr, target) == 12 else 'FAIL')

if __name__ == '__main__':
  test()
