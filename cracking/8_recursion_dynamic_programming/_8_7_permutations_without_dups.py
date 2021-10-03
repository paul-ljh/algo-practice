def permutations_without_dups(string):
  if not string:
    return []

  result = [string[0]]
  for i in range(1, len(string)):
    curr_result = []
    for s in result:
      curr_result.extend(insert_at_all_pos(string[i:i+1], s))
    result = curr_result
  return result

def insert_at_all_pos(char, s):
  r = []
  for i in range(len(s) + 1):
    r.append(s[:i] + char + s[i:])
  return r

def test():
  string = ''
  print('PASS' if permutations_without_dups(string) == [] else 'FAIL')

  string = 'a'
  print('PASS' if permutations_without_dups(string) == ['a'] else 'FAIL')
  
  string = 'paul'
  print('PASS' if permutations_without_dups(string) == ['luap', 'ulap', 'ualp', 'uapl', 'laup', 'alup', 'aulp', 'aupl', 'lapu', 'alpu', 'aplu', 'apul', 'lupa', 'ulpa', 'upla', 'upal', 'lpua', 'plua', 'pula', 'pual', 'lpau', 'plau', 'palu', 'paul'] else 'FAIL')

if __name__ == '__main__':
  test()
