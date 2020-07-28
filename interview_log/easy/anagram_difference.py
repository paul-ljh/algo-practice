def anagram_difference(s, t):
  if len(s) != len(t):
    return -1
  d = {}
  for char in s:
    d[char] = d.get(char, 0) + 1
  
  result = 0
  for char in t:
    if char not in d:
      result += 1
    else:
      d[char] -= 1
      if d[char] == 0:
        d.pop(char)
  return result

def test():
  s, t = '', ''
  print('PASS' if anagram_difference(s,t) == 0 else 'FAIL')
  
  s, t = 'l', ''
  print('PASS' if anagram_difference(s,t) == -1 else 'FAIL')
  
  s, t = 'l', 'a'
  print('PASS' if anagram_difference(s,t) == 1 else 'FAIL')
  
  s, t = 'xyzxyz', 'xxyyzz'
  print('PASS' if anagram_difference(s,t) == 0 else 'FAIL')

  s, t = 'paul', 'paula'
  print('PASS' if anagram_difference(s,t) == -1 else 'FAIL')
  
  s, t = 'leetcode', 'practice'
  print('PASS' if anagram_difference(s,t) == 5 else 'FAIL')
  
if __name__ == '__main__':
  test()
