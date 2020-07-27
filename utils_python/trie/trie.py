from utils_python.trie.trie_node import TrieNode

class Trie:
  def __init__(self, words=None):
    self.root = TrieNode()
    if words:
      for word in words:
        self.insert(word)
  
  def insert(self, str):
    return self.root.insert(str, 0)
  
  def search(self, str):
    return self.root.search(str, 0)
