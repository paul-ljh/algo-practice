class Trie:
  class TrieNode:
    def __init__(self, data):
      self.data = data
      self.children = {}

    def insert(self, word, index):
      if index not in range(len(word)):
        return
      char = word[index]
      if char not in self.children:
        self.children[char] = type(self)(char)
      return self.children[char].insert(word, index + 1)

    def search(self, word, index):
      if index not in range(len(word)):
        return True
      char = word[index]
      if char not in self.children:
        return False
      return self.children[char].search(word, index + 1)

    def remove(self, word, index):
      char = word[index]
      if char not in self.children:
        return False
      if index == len(word) - 1:
        if len(self.children[char].children) == 0:
          self.children.pop(char)
        return
      else:
        return self.children[char].remove(word, index + 1)

  def __init__(self):
    self.root = {}

  def insert(self, word):
    if not word: return

    char = word[0]
    if char not in self.root:
      self.root[char] = self.TrieNode(char)
    self.root[char].insert(word, 1)

  def search(self, word):
    if not word: return True

    char = word[0]
    if char not in self.root:
      return False
    return self.root[char].search(word, 1)

  def remove(self, word):
      if not word: return
      char = word[0]
      if char not in self.root:
        return False
      return self.root[char].remove(word, 1)

def test_insert_and_search():
  t = Trie()
  for w in ['', 'Paul', 'PAULA', 'Pause', 'pal', 'tax']:
    t.insert(w)

  m = {
    '': True,
    'Paul': True,
    'PAULA': True,
    'Pause': True,
    'pal': True,
    'tax': True,
    'PAU': True,
    'P': True,
    'AXE': False,
    'A': False
  }
  for k, v in m.items():
    print('PASS' if t.search(k) == v else 'FAIL')

def test_remove_and_search():
  t = Trie()
  for w in ['paul', 'pal']:
    t.insert(w)

  print('PASS' if t.remove('pau') == True else 'FAIL')
  print('PASS' if t.search('pau') == True else 'FAIL')
  print('PASS' if t.remove('paul') == True else 'FAIL')
  print('PASS' if t.search('paul') == False else 'FAIL')
  print('PASS' if t.remove('pal') == True else 'FAIL')
  print('PASS' if t.search('pal') == False else 'FAIL')

if __name__ == '__main__':
  test_insert_and_search()
