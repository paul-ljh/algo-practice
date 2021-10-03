def permutations_with_dups(string):
  if not string: return {}
  return generate_permutations(string, 0)

def generate_permutations(string, index):
  if index == len(string) - 1:
    return {string[-1]}
  prev = generate_permutations(string, index+1)
  curr = set()
  for perm in prev:
    curr.update(insert_at_all_pos(string[index], perm))
  return curr
  
def insert_at_all_pos(char, s):
  r = []
  for i in range(len(s) + 1):
    if i == 0 or s[i-1] != char:
      r.append(s[:i] + char + s[i:])
  return r

def test():
  string = ''
  print('PASS' if permutations_with_dups(string) == {} else 'FAIL')

  string = 'a'
  print('PASS' if permutations_with_dups(string) == {'a'} else 'FAIL')
  
  string = 'aaa'
  print('PASS' if permutations_with_dups(string) == {'aaa'} else 'FAIL')
  
  string = 'paul'
  print('PASS' if permutations_with_dups(string) == set(['paul', 'apul', 'aupl', 'aulp', 'pual', 'upal', 'uapl', 'ualp', 'pula', 'upla', 'ulpa', 'ulap', 'palu', 'aplu', 'alpu', 'alup', 'plau', 'lpau', 'lapu', 'laup', 'plua', 'lpua', 'lupa', 'luap']) else 'FAIL')
  
  string = 'balla'
  print('PASS' if permutations_with_dups(string) == {'llaab', 'labla', 'lbala', 'blaal', 'ablla', 'laalb', 'balla', 'allab', 'albla', 'llaba', 'lblaa', 'alalb', 'balal', 'bllaa', 'llbaa', 'aalbl', 'laabl', 'aallb', 'blala', 'baall', 'allba', 'lbaal', 'aabll', 'lalab', 'alabl', 'aball', 'lalba', 'labal', 'ablal', 'albal'} else 'FAIL')  

if __name__ == '__main__':
  test()
