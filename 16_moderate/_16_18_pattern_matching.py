'''
Given 2 strings, pattern and value. The pattern string consists of just the letters 'a' and 'b', describing a pattern within a string. For example, the string catcatgocatgo matches the pattern aabab. It also matches pattern like a, ab and b.

Write a method to determine if value matches pattern.
'''

def pattern_matching(pattern, value):
  if not pattern and not value:
    return True
  elif not pattern or not value:
    return False
  
  a_total, b_total = count_pattern(pattern)
  value_len, pattern_len = len(value), len(pattern)
  
  pattern_1 = pattern[0]
  max_pattern1_len = ((value_len - (a_total if pattern_1 == 'b' else b_total))
                      // (b_total if pattern_1 == 'b' else a_total))
  
  for pattern1_len in range(1, max_pattern1_len+1):
    subs = {'a': None, 'b': None}
    remain_count = {'a': a_total, 'b': b_total}
    remain_count[pattern_1] -= 1
    
    subs[pattern_1] = value[:pattern1_len]
    value_index = pattern1_len
    pattern_index = 1
    
    while value_index < value_len and pattern_index < pattern_len:
      p = pattern[pattern_index]
      if subs[p] != None:
        if subs[p] != value[value_index : value_index + len(subs[p])]:
          break
      else:
        remain_p_chars = value_len - value_index - len(subs[pattern_1]) * remain_count[pattern_1]
        if remain_p_chars < remain_count[p] or remain_p_chars % remain_count[p] != 0:
          break
        p_len = remain_p_chars // remain_count[p]
        subs[p] = value[value_index : value_index + p_len]
      
      pattern_index += 1
      value_index += len(subs[p])
      remain_count[p] -= 1
    else:
      if value_index == value_len and pattern_index == pattern_len:
        return True
  return False

def count_pattern(pattern):
  a_total = b_total = 0
  for char in pattern:
    if char == 'a':
      a_total += 1
    else:
      b_total += 1
  return (a_total, b_total)

def test():
  pattern, value = '', ''
  answer = True
  print('PASS' if pattern_matching(pattern, value) == answer else 'FAIL')
  
  pattern, value = 'a', ''
  answer = False
  print('PASS' if pattern_matching(pattern, value) == answer else 'FAIL')
  
  pattern, value = '', 'jhk'
  answer = False
  print('PASS' if pattern_matching(pattern, value) == answer else 'FAIL')
  
  pattern, value = 'a', 'cat'
  answer = True
  print('PASS' if pattern_matching(pattern, value) == answer else 'FAIL')
  
  pattern, value = 'ab', 'cat'
  answer = True
  print('PASS' if pattern_matching(pattern, value) == answer else 'FAIL')
  
  pattern, value = 'bb', 'catcat'
  answer = True
  print('PASS' if pattern_matching(pattern, value) == answer else 'FAIL')
  
  pattern, value = 'abab', 'catcat'
  answer = True
  print('PASS' if pattern_matching(pattern, value) == answer else 'FAIL')
  
  pattern, value = 'abababab', 'catcat'
  answer = False
  print('PASS' if pattern_matching(pattern, value) == answer else 'FAIL')
  
  pattern, value = 'aabab', 'catcatgocatgo'
  answer = True
  print('PASS' if pattern_matching(pattern, value) == answer else 'FAIL')
  
  pattern, value = 'aabab', 'caccaccoccaccoc'
  answer = True
  print('PASS' if pattern_matching(pattern, value) == answer else 'FAIL')

if __name__ == "__main__":
  test()
