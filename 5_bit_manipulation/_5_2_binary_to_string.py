def binary_to_string(f):
  subtractor = 0.5
  result = []
  while len(result) < 32 and f != 0:
    if f >= subtractor:
      f -= subtractor
      result.append('1')
    else:
      result.append('0')
    subtractor /= 2
  
  if f != 0:
    return 'ERROR'
  else:
    return ''.join(result)
  
def test():
  f = 0.5
  print('PASS' if binary_to_string(f) == '1' else 'FAIL')
  
  f = 0.25
  print('PASS' if binary_to_string(f) == '01' else 'FAIL')
  
  f = 0.625
  print('PASS' if binary_to_string(f) == '101' else 'FAIL')
  
  f = pow(2, -32)
  print('PASS' if binary_to_string(f) == '00000000000000000000000000000001' else 'FAIL')
  
  f = pow(2, -35)
  print('PASS' if binary_to_string(f) == 'ERROR' else 'FAIL')
  
if __name__ == "__main__":
  test()
  
