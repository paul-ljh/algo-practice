def pairs_with_sum_dict(arr, target):
  occur = {}
  result = []
  for elem in arr:
    complement = target - elem
    if occur.get(complement, 0) > 0:
      occur[complement] -= 1
      result.append((elem, complement))
    else:
      occur[elem] = occur.get(elem, 0) + 1
  return result

def pairs_with_sum_iter(arr, target):
  arr.sort()
  start, end = 0, len(arr)-1
  result = []
  while start != end:
    complement = target - arr[start]
    if complement == arr[end]:
      result.append((arr[start], complement))
      start += 1
      end -= 1
    elif complement > arr[end]:
      start += 1
    else:
      end -= 1
  return result

def test():
  arr = [1,3,1,1,3,5,6,4,4]
  target = 4
  print('PASS' if pairs_with_sum_dict(arr, target) == [(3,1), (3,1)] else 'FAIL')
  print('PASS' if pairs_with_sum_iter(arr, target) == [(1,3), (1,3)] else 'FAIL')

  arr = [1,3,1,1,3,5,6,4,4]
  target = 2
  print('PASS' if pairs_with_sum_dict(arr, target) == [(1,1)] else 'FAIL')
  print('PASS' if pairs_with_sum_iter(arr, target) == [(1,1)] else 'FAIL')

  arr = [1,2,3,3,3,4,5,7]
  target = 6
  print('PASS' if pairs_with_sum_dict(arr, target) == [(3,3), (4,2), (5,1)] else 'FAIL')
  print('PASS' if pairs_with_sum_iter(arr, target) == [(1,5), (2,4), (3,3)] else 'FAIL')
  
if __name__ == '__main__':
  test()
      
