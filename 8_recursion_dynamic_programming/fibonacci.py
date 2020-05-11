def fibonacci_recur(i):
  cache = [0,0]
  fibonacci_helper(i, cache)
  return sum(cache)

def fibonacci_helper(i, cache):
  if i == 0:
    return
  if i == 1 or i == 2:
    cache[1] = 1
    return
  fibonacci_helper(i-1, cache)
  temp = cache[0] + cache[1]
  cache[0], cache[1] = cache[1], temp
  return

def fibonacci_iter(i):
  cache = [0,1]
  if i == 0 or i == 1:
    return cache[i]
  for j in range(2,i+1):
    new_fibo = sum(cache)
    cache[0], cache[1] = cache[1], new_fibo
  return cache[1]

def test():
  answer = [0,1,1,2,3,5,8,13,21,34]
  for index in range(len(answer)):
    print('PASS' if fibonacci_iter(index) == fibonacci_recur(index) == answer[index] else 'FAIL')
  
if __name__ == '__main__':
  test()
