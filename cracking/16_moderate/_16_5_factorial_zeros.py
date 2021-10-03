'''
Write an algorithm that computes the number of trailing zeros in n!
'''

def factorial_zero(num):
  if num <= 0:
    return 0
  
  count = 0
  denom = 5
  while num >= denom:
    count += num // denom
    denom *= 5
  return count

def test():
  num = 0
  answer = 0
  print('PASS' if factorial_zero(num) == answer else 'FAIL')
  
  num = 2
  answer = 0
  print('PASS' if factorial_zero(num) == answer else 'FAIL')
  
  num = 5
  answer = 1
  print('PASS' if factorial_zero(num) == answer else 'FAIL')
  
  num = 10
  answer = 2
  print('PASS' if factorial_zero(num) == answer else 'FAIL')
  
  num = 15
  answer = 3
  print('PASS' if factorial_zero(num) == answer else 'FAIL')
  
  num = 25
  answer = 6
  print('PASS' if factorial_zero(num) == answer else 'FAIL')

if __name__ == "__main__":
  test()
