from trie_node import TrieNode

class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  def insert(self, str):
    return self.root.insert(str, 0)
  
  def search(self, str):
    return self.root.search(str, 0)
