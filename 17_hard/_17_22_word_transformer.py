import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from my_queue import Queue
from math import ceil, floor

class Word:
  def __init__(self, str, visited=False):
    self.str = str
    self.visited = visited
    self.ancestry = []    

def transform_d(d, l):
  h = {}
  for word in d:
    if len(word) == l:
      w = Word(word)
      options = generate_options(word)
      for opt in options:
        if opt not in h:
          h[opt] = []
        h[opt].append(w)
  return h

def generate_options(str):
  r = []
  for i in range(len(str)):
    r.append(str[:i] + '_' + str[i+1:])
  return r

def compare(w1, w2):
  diff = 0
  for i in range(len(w1)):
    if w1[i] != w2[i]:
      diff += 1
  return diff

def word_transformer_dfs(start, target, d):
  if start == target:
    return [start, target]
  h = transform_d(d, len(target))
  r = transform_dfs(start, target, h)
  if r:
    r.append(start)
  return r

def transform_dfs(word, target, h):
  if compare(word, target) == 1:
    return [target]
  options = generate_options(word)
  for opt in options:
    if opt in h:
      for candidate in h[opt]:
        if not candidate.visited:
          candidate.visited = True
          r = transform_dfs(candidate.str, target, h)
          if r:
            r.append(candidate.str)
            return r
  return None

def word_transformer_bfs(start, target, d):
  if start == target:
    return [start, target]
  h = transform_d(d, len(target))
  
  first = transform_bfs(start, target, h, floor(len(d)/2), 1)
  if first:
    return first
  else:
    return transform_bfs(target, start, h, ceil(len(d)/2), 2)

def transform_bfs(start, target, h, t, flag):
  q = Queue()
  q.push(Word(start, True))
  counter = 0
  
  while not q.is_empty() and counter <= t:
    word = q.pop()
    options = generate_options(word.str)
    for opt in options:
      if opt in h:
        for candidate in h[opt]:
          if candidate.visited != flag:
            if candidate.visited == False:
              if compare(candidate.str, target) == 1:
                return word.ancestry + [word.str, candidate.str, target]
              else:
                candidate.visited = flag
                candidate.ancestry = word.ancestry + [word.str]
                q.push(candidate)
                counter += 1
            else:
              return word.ancestry + [word.str, candidate.str] + candidate.ancestry[::-1]
  return None


def test():
  start, target = 'RADE', 'LETF'
  d = set(['RADD', 'RACD', 'LACD', 'LACE', 'LECE', 'LECF'])
  print('PASS' if word_transformer_bfs(target, start, d) == word_transformer_dfs(target, start, d) == ['RADE', 'RADD', 'RACD', 'LACD', 'LACE', 'LECE', 'LECF', 'LETF'] else 'FAIL')
  
  d = set(['RACD', 'LACD', 'LACE', 'LECE', 'LECF'])
  print('PASS' if word_transformer_bfs(target, start, d) == word_transformer_dfs(target, start, d) == None else 'FAIL')

  d = set(['RADA', 'RADD', 'RACD', 'LACD', 'LACE', 'LECE', 'LECF'])
  print('PASS' if word_transformer_bfs(target, start, d) == word_transformer_dfs(target, start, d) == ['RADE', 'RADD', 'RACD', 'LACD', 'LACE', 'LECE', 'LECF', 'LETF'] else 'FAIL')
  
if __name__ == '__main__':
  test()
