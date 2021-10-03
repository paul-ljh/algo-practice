def the_masseuse(times):
  one_away, two_away = 0, 0
  for t in times:
    best_with = t + two_away
    best_without = one_away
    two_away = one_away
    one_away = max(best_with, best_without)
  return one_away

def test():
  times = []
  print('PASS' if the_masseuse(times) == 0 else 'FAIL')
  
  times = [15]
  print('PASS' if the_masseuse(times) == 15 else 'FAIL')
  
  times = [15,30]
  print('PASS' if the_masseuse(times) == 30 else 'FAIL')
  
  times = [15,30,45]
  print('PASS' if the_masseuse(times) == 60 else 'FAIL')
  
  times = [15,60,30]
  print('PASS' if the_masseuse(times) == 60 else 'FAIL')
  
  times = [30,15,60,150,45,15,15,45]
  print('PASS' if the_masseuse(times) == 240 else 'FAIL')
  
if __name__ == '__main__':
  test()
