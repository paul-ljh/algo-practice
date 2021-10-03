def multiply(a,b):
  sm, bg = abs(min(a,b)), abs(max(a,b))
  product = 0
  for i in range(sm):
    product += bg
  
  if (a <= 0 and b < 0) or (a >= 0 and b > 0):
    return product
  else:
    return negate(product)

def subtract(a,b):
  return a + negate(b)

def divide(num, denom):
  if denom == 0:
    raise ZeroDivisionError('division by zero')
  product, quo = 0, 0
  abs_num, abs_denom = abs(num), abs(denom)
  while product + abs_denom <= abs_num:
    product += abs_denom
    quo += 1
  
  if (num <= 0 and denom < 0) or (num >= 0 and denom > 0):
    return quo
  else:
    return negate(quo)
  
def negate(a):
  return ~a+1

def test():
  # multiply
  a, b, answer = 0, 0, 0
  print('PASS' if multiply(a,b) == answer else 'FAIL')
  
  a, b, answer = 2, 3, 6
  print('PASS' if multiply(a,b) == answer else 'FAIL')
  
  a, b, answer = -2, -4, 8
  print('PASS' if multiply(a,b) == answer else 'FAIL')
  
  a, b, answer = -2, 1, -2
  print('PASS' if multiply(a,b) == answer else 'FAIL')
  
  # subtract
  a, b, answer = 0, 0, 0
  print('PASS' if subtract(a,b) == answer else 'FAIL')
  
  a, b, answer = 2, 3, -1
  print('PASS' if subtract(a,b) == answer else 'FAIL')
  
  a, b, answer = -2, 3, -5
  print('PASS' if subtract(a,b) == answer else 'FAIL')
  
  a, b, answer = -2, -3, 1
  print('PASS' if subtract(a,b) == answer else 'FAIL')
  
  a, b, answer = 2, -3, 5
  print('PASS' if subtract(a,b) == answer else 'FAIL')
  
  # divide
  a, b, answer = 6, 0, 0
  try:
    divide(a,b)
    print('FAIL')
  except ZeroDivisionError as err:
    print('PASS')
  
  a, b, answer = 6, 3, 2
  print('PASS' if divide(a,b) == answer else 'FAIL')
  
  a, b, answer = 7, 3, 2
  print('PASS' if divide(a,b) == answer else 'FAIL')
  
  a, b, answer = 0, 3, 0
  print('PASS' if divide(a,b) == answer else 'FAIL')
  
  a, b, answer = -6, -3, 2
  print('PASS' if divide(a,b) == answer else 'FAIL')

if __name__ == "__main__":
  test()
  
  
