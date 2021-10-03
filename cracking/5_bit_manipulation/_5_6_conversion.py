'''
Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
'''

def conversion_best(a, b):
  d = a ^ b
  count = 0
  while d != 0:
    d &= (d-1)
    count += 1
  return count

def conversion(a, b):
  d = a ^ b
  count = 0
  i = 0

  while d != 0:
    mask = 1 << i
    if d & mask != 0:
      count += 1
      d ^= mask
    i += 1
  return count

def test():
  a, b = 0b0, 0b0
  answer = 0
  print('PASS' if conversion(a,b) == conversion_best(a,b) == answer else 'FAIL')
  
  a, b = 0b1, 0b1
  answer = 0
  print('PASS' if conversion(a,b) == conversion_best(a,b) == answer else 'FAIL')
  
  a, b = 0b1, 0b0
  answer = 1
  print('PASS' if conversion(a,b) == conversion_best(a,b) == answer else 'FAIL')
  
  a, b = 0b11001, 0b1101010
  answer = 5
  print('PASS' if conversion(a,b) == conversion_best(a,b) == answer else 'FAIL')
  
if __name__ == "__main__":
  test()

  