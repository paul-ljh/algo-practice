def parens(n):
  cache = {}
  generate_combos('', cache, n, n)
  return cache[(n,n)]

def generate_combos(combo, cache, l_remain, r_remain):
  if (l_remain, r_remain) in cache:
    return
  if l_remain == 0:
    cache[(0, r_remain)] = [')' * r_remain]
    return

  generate_combos(combo+'(', cache, l_remain-1, r_remain)
  curr = ['(' + suffix for suffix in cache[(l_remain-1, r_remain)]]
  
  if l_remain < r_remain:
    generate_combos(combo+'(', cache, l_remain, r_remain-1)
    curr.extend([')' + suffix for suffix in cache[(l_remain, r_remain-1)]])
  cache[(l_remain,r_remain)] = curr
  return

def test():
  result = ['']
  print('PASS' if parens(0) == result else 'FAIL')
  
  result = ['()']
  print('PASS' if parens(1) == result else 'FAIL')
  
  result = ['(())','()()']
  print('PASS' if parens(2) == result else 'FAIL')
  
  result = ['((()))', '(()())', '(())()', '()(())', '()()()']
  print('PASS' if parens(3) == result else 'FAIL')
  
  result = ['(((())))', '((()()))', '((())())', '((()))()', '(()(()))', '(()()())', '(()())()', '(())(())', '(())()()', '()((()))', '()(()())', '()(())()', '()()(())', '()()()()']
  print('PASS' if parens(4) == result else 'FAIL')

if __name__ == '__main__':
  test()
