'''
IXL Learning, 2020.5

Some numbers are formed with closed paths. The digits 0, 4, 6 and 9 each have 1 closed path, and 8 has 2. None of the other number is formed with a closed path. Given a number, determine the total number of closed paths in all of its digits combined.

EX:
64957800 => 1+1+1+2+1+1=7
'''

def count_closed_path(n):
  quo, rem = n, 0
  result = 0
  while quo is not None:
    quo, rem = quo // 10, quo % 10
    if quo == 0:
      quo = None
    if (rem == 0 or rem == 4 or rem == 6 or rem == 9):
      result += 1
    if rem == 8:
      result += 2
  return result

def test():
  print('PASS' if count_closed_path(0) == 1 else 'FAIL')
  print('PASS' if count_closed_path(4) == 1 else 'FAIL')
  print('PASS' if count_closed_path(6) == 1 else 'FAIL')
  print('PASS' if count_closed_path(9) == 1 else 'FAIL')
  print('PASS' if count_closed_path(5) == 0 else 'FAIL')
  print('PASS' if count_closed_path(8) == 2 else 'FAIL')
  print('PASS' if count_closed_path(849500) == 6 else 'FAIL')

if __name__ == '__main__':
  test()
