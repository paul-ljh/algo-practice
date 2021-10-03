'''
Write a method to return all subsets of a set
'''

def power_set(origin):
  result = []
  generate_all_subset(origin, result, 0)
  return result

def generate_all_subset(origin, result, index):
  if index == len(origin):
    result.append([])
    return
  generate_all_subset(origin, result, index+1)
  curr_set = origin[index:index+1]
  curr_result = []
  for subset in result:
    curr_result.append(subset + curr_set)
  result.extend(curr_result)
  return

def power_set_alternative(origin):
  counter = 1 << len(origin)
  result = []
  for i in range(counter):
    result.append(build_set(origin, i))
  return result

def build_set(origin, pattern):
  result = []
  for i in range(len(origin)):
    mask = 1 << i
    if mask & pattern != 0:
      result.append(origin[i])
  return result

def test():
  print('PASS' if power_set_alternative([]) == power_set([]) == [[]] else 'FAIL')
  print('PASS' if power_set([1,4,5,6]) == [
    [],
    [6],
    [5],[6,5],
    [4],[6,4],[5,4],[6,5,4],
    [1],[6,1],[5,1],[6,5,1],[4,1],[6,4,1],[5,4,1],[6,5,4,1]
  ] else 'FAIL')
  
  print('PASS' if power_set_alternative([1,4,5,6]) == [
    [],
    [1],[4],[1,4],
    [5],[1,5],[4,5],[1,4,5],
    [6],[1,6],[4,6],[1,4,6],
    [5,6],[1,5,6],[4,5,6],[1,4,5,6]
  ] else 'FAIL')

if __name__ == '__main__':
  test()
