def group_anagrams(arr):
  d = {}
  for s in arr:
    sorted_str = ''.join(sorted(s))
    if sorted_str not in d:
      d[sorted_str] = []
    d[sorted_str].append(s)
  return list(d.values())

def test():
  arr = []
  print('PASS' if group_anagrams(arr) == [] else 'FAIL')
  
  arr = ['rasp', 'spar', 'paul', 'paula', 'rap', 'par', 'apr']
  print('PASS' if group_anagrams(arr) == [['rasp', 'spar'], ['paul'], ['paula'], ['rap', 'par', 'apr']] else 'FAIL')
  
  arr = ['xye', 'abs', 'etu', 'df']
  print('PASS' if group_anagrams(arr) == [['xye'], ['abs'], ['etu'], ['df']] else 'FAIL')
  
if __name__ == '__main__':
    test()
