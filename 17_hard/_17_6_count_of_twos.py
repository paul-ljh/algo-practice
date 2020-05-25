def count_of_twos(num):
  count = 0
  for i in range(len(str(num))):
    count += get_quotient_count(num, i)
    count += get_remainder_count(num, i)
  return count

def get_quotient_count(num, i):
  quo = num // (10 ** (i + 1))
  return quo * (10 ** i)

def get_remainder_count(num, i):
  rem = num % (10 ** (i + 1))
  left, right = int(10 ** (i + 1) * 0.2), int(10 ** (i + 1) * 0.3)
  if rem >= right:
    return 10 ** i
  elif rem in range(left, right):
    return rem - left + 1
  else:
    return 0

def test():
  print('PASS' if count_of_twos(0) == 0 else 'FAIL')
  print('PASS' if count_of_twos(1) == 0 else 'FAIL')
  print('PASS' if count_of_twos(2) == 1 else 'FAIL')
  print('PASS' if count_of_twos(9) == 1 else 'FAIL')
  print('PASS' if count_of_twos(10) == 1 else 'FAIL')
  print('PASS' if count_of_twos(20) == 3 else 'FAIL')
  print('PASS' if count_of_twos(30) == 13 else 'FAIL')
  print('PASS' if count_of_twos(222) == 69 else 'FAIL')
  
if __name__ == '__main__':
  test()
