def coins(n):
  return compose(n, {}, 25)

def compose(n, cache, prev):
  if n < 0:
    return 0
  if n == 0:
    return 1
  if (n, prev) in cache:
    return cache[(n, prev)]
  r = 0
  if prev == 25:
    r += compose(n-25, cache, 25)
  if prev >= 10:
    r += compose(n-10, cache, 10)
  if prev >= 5:
    r += compose(n-5, cache, 5)
  r += 1
  cache[(n, prev)] = r
  return r

def alternative_coins(n):
  return alternative_compose(n, [25,10,5,1], 0, {})

def alternative_compose(n, denoms, index, cache):
  if index == len(denoms) - 1 or n == 0:
    return 1
  if (n, index) in cache:
    return cache[(n, index)]

  r = 0
  for i in range(n // denoms[index] + 1):
    r += alternative_compose(n- i*denoms[index], denoms, index+1, cache)
  cache[(n, index)] = r
  return r

def test():
  n = 0
  print('PASS' if alternative_coins(n) == coins(n) == 1 else 'FAIL')
  
  n = 1
  print('PASS' if alternative_coins(n) == coins(n) == 1 else 'FAIL')
  
  n = 4
  print('PASS' if alternative_coins(n) == coins(n) == 1 else 'FAIL')
  
  n = 5
  print('PASS' if alternative_coins(n) == coins(n) == 2 else 'FAIL')
  
  n = 10
  print('PASS' if alternative_coins(n) == coins(n) == 4 else 'FAIL')
  
  n = 15
  print('PASS' if alternative_coins(n) == coins(n) == 6 else 'FAIL')
  
  n = 20
  print('PASS' if alternative_coins(n) == coins(n) == 9 else 'FAIL')
  
  n = 25
  print('PASS' if alternative_coins(n) == coins(n) == 13 else 'FAIL')
  
  for n in range(1, 400):
    if alternative_coins(n) != coins(n):
      print(f'FAIL at {n}')

if __name__ == '__main__':
  test()
