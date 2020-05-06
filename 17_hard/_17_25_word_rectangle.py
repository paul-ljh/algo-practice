import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from heapq import *
from trie import Trie

def word_transformer(d):
  if not d:
    return None
  h = group_by_length(d)
  max_len = max(h.keys())
  max_product = max_len ** 2
  
  for p in reversed(range(1, max_product+1)):
    for l in reversed(range(1, max_len+1)):
      other_l = p // l
      if other_l > max_len:
        break
      if l in h and p % l == 0 and other_l in h:
        if len(h[l]) >= other_l and len(h[other_l]) >= l:
          trie = build_trie(h[l])
          r = find_rect(trie, [], set(), other_l, l, h[other_l])
          if r:
            return r
  return None

def group_by_length(d):
  h = {}
  for word in d:
    l = len(word)
    if l not in h:
      h[l] = []
    h[l].append(word)
  return h

def build_trie(group):
  t = Trie()
  for s in group:
    t.insert(s)
  return t

def find_rect(trie, result, index_set, word_l, r_l, group):
  if len(result) == r_l:
    return result
  for i in range(len(group)):
    if i not in index_set:
      next_result = result + [group[i]]
      if trie_look_up(trie, next_result, word_l):
        r = find_rect(trie, next_result, index_set | set([i]), word_l, r_l, group)
        if r:
          return r
  return None

def trie_look_up(trie, result, length):
  for l in range(length):
    prefix = []
    for i in range(len(result)):
      prefix.append(result[i][l])
    if not trie.search(''.join(prefix)):
      return False
  return True
  

def test():
  g1 = ['paulli', 'apples', 'applee', 'resist', 'liabdk', 'unions', 'liable', 'paueld']
  g2 = ['paull', 'apple', 'apple', 'resis', 'liabd', 'union', 'liabl', 'pauel']
  g3 = ['paul', 'pull', 'acid', 'apni', 'upia', 'elob', 'lend', 'desk']
  print('PASS' if word_transformer(g1+g2+g3) == ['paul', 'apni', 'upia', 'elob', 'lend', 'desk'] else 'FAIL')
  
  g1 = ['peep', 'adxu', 'uiil', 'lttl', 'rude', 'rand']
  g2 = ['paul', 'pull', 'edit', 'exit', 'uilk', 'rute']
  print('PASS' if word_transformer(g1+g2) == ['peep', 'adxu', 'uiil', 'lttl'] else 'FAIL')
  
  g1 = ['a', 'a']
  print('PASS' if word_transformer(g1) == ['a'] else 'FAIL')

if __name__ == '__main__':
  test()
