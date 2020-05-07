class HashTable:
  def __init__(self):
    self.size = 10
    self.entries = [[]] * self.size
    self.num_items = 0
    self.keys = []
  
  def __setitem__(self, name, value):
    hash_key = self.compute_hash_key(name)
    for pair in self.entries[hash_key]:
      if pair[0] == name:
        pair[1] = value
        break
    else:
      self.entries[hash_key].append([name, value])
      self.keys.append(name)
      self.num_items += 1
      
  def __getitem__(self, name):
    hash_key = self.compute_hash_key(name)
    for pair in self.entries[hash_key]:
      if pair[0] == name:
        return pair[1]
    raise KeyError(name)
  
  def __contains__(self, name):
    hash_key = self.compute_hash_key(name)
    for pair in self.entries[hash_key]:
      if pair[0] == name:
        return True
    return False
  
  def __delitem__(self, key):
    hash_key = self.compute_hash_key(key)
    for i, pair in enumerate(self.entries[hash_key]):
      if pair[0] == key:
        self.num_items -= 1
        self.entries[hash_key].pop(i)
        self.keys.remove(key)
        return 
    else:
      raise KeyError(key)
    
  def __len__(self):
    return self.num_items
  
  def __iter__(self):
    self.i = 0
    return self
  
  def __next__(self):
    if self.i < self.num_items:
      result = self.keys[self.i]
      self.i += 1 
      return result
    else:
      raise StopIteration

  def compute_hash_key(self, name):
    return hash(name) % self.size

def test():
  h = HashTable()
  h[1] = 2
  try:
    h[2]
  except KeyError:
    print("PASS KeyError 2")
  
  print('PASS' if len(h) == 1 else 'FAIL')
  print('PASS' if h[1] == 2 else 'FAIL')
  print('PASS' if 1 in h else 'FAIL')
  print('PASS' if not 3 in h else 'FAIL')
  
  h[1] = 3
  h[2] = 3
  try:
    h[[1]] = 3
  except TypeError:
    print("PASS TypeError unhashable type")
  
  print('PASS' if len(h) == 2 else 'FAIL')
  print('PASS' if h[1] == 3 else 'FAIL')
  print('PASS' if h[2] == 3 else 'FAIL')
  
  h[4] = 4
  key_arr = [1,2,4]
  for i, key in enumerate(h):
    print('PASS' if key == key_arr[i] else 'FAIL')
  
  del(h[1])
  del(h[2])
  del(h[4])
  print('PASS' if len(h) == 0 else 'FAIL')
  print('PASS' if not 1 in h else 'FAIL')
  print('PASS' if not 2 in h else 'FAIL')
  
  try:
    h[1]
  except KeyError:
    print("PASS KeyError 1")
    
  try:
    h[2]
  except KeyError:
    print("PASS KeyError 2")

  try:
    del(h[3])
  except KeyError:
    print("PASS KeyError 3")  

if __name__ == '__main__':
    test()
