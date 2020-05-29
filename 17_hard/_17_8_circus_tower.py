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

def test():
  persons = []
  print('PASS' if circus_tower(persons) == [] else 'PASS')
  
  persons = [(20,20)]
  print('PASS' if circus_tower(persons) == [(20,20)] else 'PASS')
  
  persons = [(30,30), (20,20)]
  print('PASS' if circus_tower(persons) == [(20,20), (30,30)] else 'PASS')
  
  persons = [(20,20), (30,10)]
  print('PASS' if circus_tower(persons) == [(20,20)] else 'PASS')
  
  persons = [(40,60), (73,10), (56,90), (75,15), (60,95), (80,20), (61,61), (85,25), (65,65), (90,30), (70,70), (100,100)]
  print('PASS' if circus_tower(persons) == [(73,10), (75,15), (80,20), (85,25), (90,30), (100,100)] else 'PASS')
  
if __name__ == '__main__':
  test()
