def rotated_search(arr, target):
  return search(arr, target, 0, len(arr)-1)

def search(arr, target, left, right):
  if right < left:
    return -1
  mid = (left+right) // 2
  
  if arr[mid] == target:
    return mid
  elif arr[mid] < arr[left]:
    if arr[mid] < target <= arr[right]:
      r = search(arr, target, mid+1, right)
      if r != -1:
        return r
    else:
      return search(arr, target, left, mid-1)
  elif arr[mid] > arr[left]:
    if arr[left] <= target <= arr[mid]:
      l = search(arr, target, left, mid-1)
      if l != -1:
        return l
    else:
      return search(arr, target, mid+1, right)
  else:
    if arr[right] != arr[mid]:
      return search(arr, target, mid+1, right)
    else:
      l = search(arr, target, left, mid-1)
      if l != -1:
        return l
      else:
        return search(arr, target, mid+1, right)

def test():
  arr = []
  print('PASS' if rotated_search(arr, 9) == -1 else 'FAIL')
  
  arr = [4]
  print('PASS' if rotated_search(arr, 9) == -1 else 'FAIL')
  print('PASS' if rotated_search(arr, 2) == -1 else 'FAIL')
  print('PASS' if rotated_search(arr, 4) == 0 else 'FAIL')
  
  arr = [9,15,2,3,6,7,8]
  print('PASS' if rotated_search(arr, 7) == 5 else 'FAIL')
  print('PASS' if rotated_search(arr, 6) == 4 else 'FAIL')
  print('PASS' if rotated_search(arr, 8) == 6 else 'FAIL')
  
  print('PASS' if rotated_search(arr, 1) == -1 else 'FAIL')
  print('PASS' if rotated_search(arr, 16) == -1 else 'FAIL')
  print('PASS' if rotated_search(arr, 9) == 0 else 'FAIL')
  print('PASS' if rotated_search(arr, 2) == 2 else 'FAIL')
  
  arr = [2,5,8,2,2,2,2]
  print('PASS' if rotated_search(arr, 2) == 3 else 'FAIL')
  print('PASS' if rotated_search(arr, 1) == -1 else 'FAIL')
  print('PASS' if rotated_search(arr, 3) == -1 else 'FAIL')

  arr = [2,2,2,3,9,1]
  print('PASS' if rotated_search(arr, 2) == 2 else 'FAIL')
  print('PASS' if rotated_search(arr, 1) == 5 else 'FAIL')
  print('PASS' if rotated_search(arr, 3) == 3 else 'FAIL')
  print('PASS' if rotated_search(arr, 0) == -1 else 'FAIL')
  print('PASS' if rotated_search(arr, 10) == -1 else 'FAIL')
  
if __name__ == '__main__':
    test()
