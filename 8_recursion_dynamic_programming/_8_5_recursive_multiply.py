import math

def recursive_multiply(n1, n2):
  bigger, smaller = (n1, n2) if n1 > n2 else (n2, n1)
  if smaller == 0:
    return 0
  elif smaller == 1:
    return bigger
  else:
    return binary_shift_add(smaller, bigger)
  
def binary_shift_add(smaller, bigger):
  result = 0
  l = math.floor(math.log(smaller, 2) + 1)
  for i in range(l):
    mask = 1 << i
    if mask & smaller != 0:
      result += (bigger << i)
  return result

def test():
  print('PASS' if recursive_multiply(0,8) == 0 else 'FAIL')
  print('PASS' if recursive_multiply(1,3) == 3 else 'FAIL')
  print('PASS' if recursive_multiply(8,5) == 40 else 'FAIL')

if __name__ == '__main__':
  test()
