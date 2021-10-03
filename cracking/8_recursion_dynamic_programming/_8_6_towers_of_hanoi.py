def towers_of_hanoi(n, src, dest, other):
  if n == 0:
    return
  towers_of_hanoi(n-1, src, other, dest)
  dest.append(src.pop())
  towers_of_hanoi(n-1, other, dest, src)
  return

def test():
  n = 0
  t1, t2, t3 = [i for i in range(n)], [], []
  towers_of_hanoi(n, t1, t3, t2)
  print('PASS' if t3 == [] else 'FAIL')
  
  n = 5
  t1, t2, t3 = [i for i in range(n)], [], []
  towers_of_hanoi(n, t1, t3, t2)
  print('PASS' if t3 == [i for i in range(n)] else 'FAIL')
  
  n = 10
  t1, t2, t3 = [i for i in range(n)], [], []
  towers_of_hanoi(n, t1, t3, t2)
  print('PASS' if t3 == [i for i in range(n)] else 'FAIL')
  
if __name__ == '__main__':
  test()
