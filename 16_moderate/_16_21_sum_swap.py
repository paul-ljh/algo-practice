def sum_swap(a1, a2):
  if not a1 or not a2:
    return None
  s1, s2 = sum(a1), sum(a2)
  diff = (s1-s2) / 2
  return find_swap_pair(a1,a2,diff)

def find_swap_pair(a1, a2, diff):
  set2 = set(a2)
  for elem in a1:
    if elem - diff in set2:
      return (elem, elem-diff)
  return None

def test():
  a1 = []
  a2 = []
  print('PASS' if sum_swap(a1, a2) == None else 'FAIL')
  print('PASS' if sum_swap(a2, a1) == None else 'FAIL')
  
  a1 = [4,1,2,1,1,2]
  a2 = [3,6,3,3]
  print('PASS' if sum_swap(a1, a2) == (4,6) else 'FAIL')
  print('PASS' if sum_swap(a2, a1) == (3,1) else 'FAIL')
  
  a1 = [4,6,8,5]
  a2 = [7,6,9,6]
  print('PASS' if sum_swap(a1, a2) == None else 'FAIL')
  print('PASS' if sum_swap(a2, a1) == None else 'FAIL')
  
  a1 = [1,1,3,2]
  a2 = [-1,8,0]
  print('PASS' if sum_swap(a1, a2) == None else 'FAIL')
  print('PASS' if sum_swap(a2, a1) == None else 'FAIL')

  a1 = [1,1,1]
  a2 = [2,1]
  print('PASS' if sum_swap(a1, a2) == (1,1) else 'FAIL')
  print('PASS' if sum_swap(a2, a1) == (1,1) else 'FAIL')

if __name__ == '__main__':
    test()
