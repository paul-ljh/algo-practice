def triple_step_recur(n):
  return count_ways(n, [None] * (n+1))

def count_ways(n, cache):
  if n < 0:
    return 0
  if n == 0:
    return 1
  if cache[n] is not None:
    return cache[n]
  cache[n] = count_ways(n-1, cache) + count_ways(n-2, cache) + count_ways(n-3, cache)
  return cache[n]

def better_triple_step_recur(n):
  return better_count_ways(n, [1,2,4])

def better_count_ways(n, cache):
  if n <= 3:
    return cache[n-1] if n != 0 else 1
  better_count_ways(n-1, cache)
  ways_n = sum(cache)
  cache[0], cache[1] = cache[1], cache[2]
  cache[2] = ways_n
  return cache[2]

def triple_step_iter(n):
  cache = [1,2,4]
  if n <= 3:
    return cache[n-1] if n != 0 else 1 
  for i in range(4, n+1):
    ways_i = sum(cache)
    cache[0], cache[1], cache[2] = cache[1], cache[2], ways_i
  return cache[2]

def test():
  for i in range(15):
    print('PASS' if triple_step_recur(i) == better_triple_step_recur(i) == triple_step_iter(i) else 'FAIL')

if __name__ == '__main__':
  test()
