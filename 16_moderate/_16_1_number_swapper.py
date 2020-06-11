def number_swapper(a,b):
  a ^= b
  b ^= a
  a ^= b
  return (a,b)

def test():
  print('PASS' if number_swapper(1,2) == (2,1) else 'FAIL')
  
  print('PASS' if number_swapper(2,1) == (1,2) else 'FAIL')
  
  print('PASS' if number_swapper(1,1) == (1,1) else 'FAIL')
  
if __name__ == "__main__":
  test()
