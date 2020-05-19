def magic_index(arr):
  return magic_index_distinct(arr, 0, len(arr)-1)

def magic_index_distinct(arr, begin, end):
  if end < begin:
    return None
  mid = (end+begin) // 2
  if arr[mid] == mid:
    return mid
  elif arr[mid] > mid:
    return magic_index_distinct(arr, begin, mid-1)
  else:
    return magic_index_distinct(arr, mid+1, end)
  
def magic_fast(arr):
  return magic_index_duplicate(arr, 0, len(arr)-1)
  
def magic_index_duplicate(arr, begin, end):
  if end < begin:
    return None
  
  mid = (end+begin) // 2
  if arr[mid] == mid:
    return mid
  
  r = magic_index_duplicate(arr, max(arr[mid], mid+1), end)
  if r:
    return r

  return magic_index_duplicate(arr, begin, min(arr[mid], mid-1))
  
def test():
  arr = []
  print('PASS' if magic_index(arr) == None else 'FAIL')
  print('PASS' if magic_fast(arr) == None else 'FAIL')
  
  arr = [0]
  print('PASS' if magic_index(arr) == 0 else 'FAIL')
  print('PASS' if magic_fast(arr) == 0 else 'FAIL')
  
  arr = [1]
  print('PASS' if magic_index(arr) == None else 'FAIL')
  print('PASS' if magic_fast(arr) == None else 'FAIL')
  
  arr = [-1,0,2,4,5,6,7]
  print('PASS' if magic_index(arr) == 2 else 'FAIL')
  
  arr = [-1,0,1,2,5,6,7]
  print('PASS' if magic_index(arr) == None else 'FAIL')
  
  arr = [-1,0,4,4,6,6,9,10]
  print('PASS' if magic_fast(arr) == None else 'FAIL')
  
  arr = [0,2,2,2,4,5,6]
  print('PASS' if magic_fast(arr) == 5 else 'FAIL')

if __name__ == '__main__':
  test()
