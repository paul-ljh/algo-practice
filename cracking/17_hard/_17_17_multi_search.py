class TrieNode:
  def __init__(self):
    self.indices, self.children = [], {}
    
  def insert(self, str, original_index, index):
    if index == len(str):
      return
    if str[index] not in self.children:
      self.children[str[index]] = TrieNode()
    self.children[str[index]].indices.append(original_index)
    return self.children[str[index]].insert(str, original_index+1, index+1)
  
  def search(self, str, index):
    if index == len(str):
      return self.indices
    if str[index] in self.children:
      return self.children[str[index]].search(str, index+1)
    else:
      return []
    
class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  def insert(self, str, original_i):
    return self.root.insert(str, original_i, 0)
  
  def search(self, str):
    result = self.root.search(str, 0)
    if result:
      result = list(map(lambda end: end-len(str)+1, result))
    return result
  
def multi_search(T, b):
  trie = Trie()
  for i in range(len(b)):
    trie.insert(b[i:], i)
  result = {}
  for t in T:
    result[t] = trie.search(t)
  return result

def test():
  print('PASS' if not multi_search([], '') else 'FAIL')
  
  print('PASS' if not multi_search([], 'paul') else 'FAIL')
  
  print('PASS' if multi_search(['s', 'r'], '') == {'s': [], 'r': []} else 'FAIL')
  
  T = ['is', 'pp', 'ms', 'i', 'iss', 's']
  b = 'mississippi'
  print('PASS' if multi_search(T, b) == {'is': [1, 4], 'pp': [8], 'ms': [], 'i': [1, 4, 7, 10], 'iss': [1, 4], 's': [2, 3, 5, 6]} else 'FAIL')

if __name__ == '__main__':
  test()
