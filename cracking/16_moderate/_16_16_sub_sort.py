def sub_sort(arr):
  if not arr:
    return (0,0)

  m, n = find_borders(arr)
  if n == 0:
    return (0,0)
  
  seg_min, seg_max = m, m
  for i in range(m,n+1):
    if arr[i] > arr[seg_max]: seg_max = i
    if arr[i] < arr[seg_min]: seg_min = i

  return expand_borders(arr, m, n, seg_min, seg_max)

def find_borders(arr):
  m, n = 0, len(arr)-1
  while m < len(arr)-1:
    m += 1
    if arr[m] < arr[m-1]:
      break
  
  while n > 0:
    n -= 1
    if arr[n] > arr[n+1]:
      break
  return (m, n)

def expand_borders(arr, m, n, seg_min, seg_max):
  while m > 0 and arr[m-1] > arr[seg_min]:
    if arr[m-1] > arr[seg_max]:
      seg_max = m-1
    m -= 1
    
  while n < len(arr)-1 and arr[n+1] < arr[seg_max]:
    if arr[n+1] < arr[seg_min]:
      seg_min = n+1
    n += 1
  return (m,n)
    

def test():
  arr = []
  print('PASS' if sub_sort(arr) == (0,0) else 'FAIL')
  
  arr = [1,4,5,7,7,9]
  print('PASS' if sub_sort(arr) == (0,0) else 'FAIL')
  
  arr = [5,5,4,4,3,2,1,1]
  print('PASS' if sub_sort(arr) == (0,7) else 'FAIL')
  
  arr = [1,13,15,16,2,3,20,25,18,19]
  print('PASS' if sub_sort(arr) == (1,9) else 'FAIL')
  
  arr = [1,13,15,16,14,20,25,18,19,26,27]
  print('PASS' if sub_sort(arr) == (2,8) else 'FAIL')

if __name__ == '__main__':
    test()
