'''
DataBricks, Software Engineer New Grad, 2020 June, via Karat

Given a list of strings - words, and a string - target
return any string in words such that target contains all its characters and of the same occurances, return None otherwise.

EX:
  target = 'pilautes'
  words = ['z', 'test', 'lii', 'aaaaaaaaaa', 'paul']
  
  'pilautes' does not contain 'z', but does contain 'paul'
'''


'''
l = len(words)
m = len(target)
n = max(len(word))

Runtime: O(max(nl,m))
Space: O(m+n)
'''
def find_embedded_word(words, target):
  target_map = build_map(target)
  for word in words:
    if len(word) <= len(target):
      word_map = build_map(word)
      for letter in word_map.keys():
          if letter not in target_map or word_map[letter] > target_map[letter]:
            break
      else:
        return word
  return None

def build_map(word):
  d = {}
  for letter in word:
    d[letter] = d.get(letter, 0) + 1
  return d

def test():
  target = 'pilautes'
  words = ['z', 'test', 'lii', 'aaaaaaaaaa', 'paul']
  answer = 'paul'
  print('PASS' if find_embedded_word(words, target) == answer else 'FAIL')
  
  target = 'pilautes'
  words = ['z', 'test', 'lii', 'aaaaaaaaaa', 'poul']
  answer = None
  print('PASS' if find_embedded_word(words, target) == answer else 'FAIL')

if __name__ == "__main__":
  test()
