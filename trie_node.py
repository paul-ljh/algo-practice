class TrieNode:
  def __init__(self):
    self.children = {}
    
  def insert(self, str, index):
    if index == len(str):
      return
    curr_char = str[index]
    if curr_char not in self.children:
      self.children[curr_char] = TrieNode()
    return self.children[curr_char].insert(str, index+1)
  
  def search(self, str, index):
    if index == len(str):
      return True
    if str[index] in self.children:
      return self.children[str[index]].search(str, index+1)
    else:
      return False
