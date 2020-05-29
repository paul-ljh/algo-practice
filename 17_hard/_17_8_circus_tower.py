# O(n^2) dynamic programming
def circus_tower(persons):
  persons.sort(key=lambda p: p[0])
  result = [[] for _ in range(len(persons))]
  for i in range(1, len(persons)):
    best = find_best_lineup(persons, i, result)
    result[i] = result[best] + [persons[i]]
  return max(result, key=lambda l: len(l), default=[])

def find_best_lineup(persons, index, result):
  best = index
  target = persons[index]
  for i in reversed(range(index)):
    curr = persons[i]
    if (target[0] > curr[0] and
        target[1] > curr[1] and
        len(result[i]) > len(result[best])):
      best = i
      if len(result[best]) == i+1: break
  return best

# O(nlog(n)) dynamic programming inspired by Longest Increasing Sequence
def circus_tower_lis(persons):
  results = [[]]
  for person in persons:
    best_index = find_best(results, person)
    curr_index = best_index + 1
    if curr_index > len(results) - 1:
      results.append([])
    results[curr_index] = results[best_index] + [person]
  return results[-1]

def find_best(results, person):
  left, right, best = 0, len(results)-1, 0
  while right >= left:
    mid = (left+right) // 2
    pivot = results[mid][-1] if results[mid] else (-1, -1)
    if person[0] > pivot[0] and person[1] > pivot[1]:
      best = mid
      left = mid+1
    else:
      right = mid-1
  return best

def test():
  persons = []
  print('PASS' if circus_tower_lis(persons) == circus_tower(persons) == [] else 'PASS')
  
  persons = [(20,20)]
  print('PASS' if circus_tower_lis(persons) == circus_tower(persons) == [(20,20)] else 'PASS')
  
  persons = [(30,30), (20,20)]
  print('PASS' if circus_tower_lis(persons) == circus_tower(persons) == [(20,20), (30,30)] else 'PASS')
  
  persons = [(20,20), (30,10)]
  print('PASS' if circus_tower_lis(persons) == circus_tower(persons) == [(20,20)] else 'PASS')
  
  persons = [(40,60), (73,10), (56,90), (75,15), (60,95), (80,20), (61,61), (85,25), (65,65), (90,30), (70,70), (100,100)]
  print('PASS' if circus_tower_lis(persons) == circus_tower(persons) == [(73,10), (75,15), (80,20), (85,25), (90,30), (100,100)] else 'PASS')
  
if __name__ == '__main__':
  test()
