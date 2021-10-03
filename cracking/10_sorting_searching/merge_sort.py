def merge_sort(arr):
  helper = [None] * len(arr)
  split_and_sort(helper, arr, 0, len(arr)-1)
  return arr

def split_and_sort(helper, arr, begin, end):
  if begin < end:
    middle = begin + (end-begin)//2
    split_and_sort(helper, arr, begin, middle)
    split_and_sort(helper, arr, middle+1, end)
    merge(helper, arr, begin, middle, middle+1, end)

def merge(helper, arr, l_begin, l_end, r_begin, r_end):
  for i in range(l_begin, r_end+1):
    helper[i] = arr[i]

  l, r = l_begin, r_begin
  current = l_begin
  while l <= l_end and r <= r_end:
    if helper[l] <= helper[r]:
      arr[current] = helper[l]
      l += 1
    else:
      arr[current] = helper[r]
      r += 1
    current += 1
      
  for j in range(l, l_end+1):
    arr[current] = helper[j]
    current += 1

def test():
  arr = []
  print('PASS' if merge_sort(arr) == sorted(arr) else 'FAIL')
  
  arr = [22]
  print('PASS' if merge_sort(arr) == sorted(arr) else 'FAIL')
  
  arr = [22,18,16,15,13,5]
  print('PASS' if merge_sort(arr) == sorted(arr) else 'FAIL')
  
  arr = [22,18,16,15,13,5,3]
  print('PASS' if merge_sort(arr) == sorted(arr) else 'FAIL')
  
  arr = [22,22,22,15,15,15,15]
  print('PASS' if merge_sort(arr) == sorted(arr) else 'FAIL')


if __name__ == '__main__':
    test()
