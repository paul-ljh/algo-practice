def diving_board(k, shorter, longer):
  if longer == shorter:
    return set(shorter*k)
  else:
    result = set()
    for i in range(k+1):
      result.add(i*shorter + (k-i)*longer)
    return result

def test():
  print('PASS' if diving_board(3, 2, 2) == set(6) else 'FAIL')
  print('PASS' if diving_board(3, 1, 3) == set([3,5,7,9]) else 'FAIL')

if __name__ == '__main__':
  test()
