class Listy:
  def __init__(self, arr=[]):
    self.arr = arr
    
  def element_at(self, i):
    if i in range(len(self.arr)):
      return self.arr[i]
    else:
      return -1
    
def no_size_sorted_search(listy, target):
  if listy.element_at(0) == -1 or target < 0:
    return -1
  index = 1
  while listy.element_at(index) != -1 and listy.element_at(index) <= target:
    index *= 2
  return binary_search_recur(listy, target, index // 2, index)

def binary_search_recur(listy, target, begin, end):
  if end < begin or listy.element_at(begin) == listy.element_at(end) == -1:
    return -1
  mid = (end + begin) // 2
  elem = listy.element_at(mid)
  if elem == target:
    return mid
  elif elem == -1 or elem > target:
    return binary_search_recur(listy, target, begin, mid-1)
  else:
    return binary_search_recur(listy, target, mid+1, end)

def test():
  arr = [4,8,9,12,15,19,20,22]
  l = Listy(arr)
  for i in range(len(arr)):
    print('PASS' if no_size_sorted_search(l, arr[i]) == i else 'FAIL')
    
  print('PASS' if no_size_sorted_search(l, 3) == -1 else 'FAIL')
  print('PASS' if no_size_sorted_search(l, 25) == -1 else 'FAIL')
  print('PASS' if no_size_sorted_search(l, 13) == -1 else 'FAIL')
  print('PASS' if no_size_sorted_search(l, 18) == -1 else 'FAIL')

if __name__ == '__main__':
    test()
