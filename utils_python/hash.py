from linked_list import LinkedList;

class HashEntry:
  def __init__(self, key, value):
    self.key, self.value = key, value

  def __eq__(self, other):
    return other.key == self.key and other.value == other.value

  def to_tuple(self):
    return (self.key, self.value)

class Hash:
  def __init__(self):
    self.size = 10
    self.entries = [LinkedList() for _ in range(self.size)]
    self.counter = 0

  def __len__(self):
    return self.counter

  def __contains__(self, key):
    index = self.__get_index(key)
    l = self.entries[index]
    for data in l:
      if data.key == key:
        return True
    return False

  def __delitem__(self, key):
    index = self.__get_index(key)
    l = self.entries[index]

    for data in l:
      if data.key == key:
        l.delete(data)
        return data
    raise KeyError(key)

  def __setitem__(self, key, value):
    index = self.__get_index(key)
    l = self.entries[index]
    new_entry = HashEntry(key, value)

    for data in l:
      if data == new_entry:
        data.value = value
        return
    l.append(new_entry)

  def __getitem__(self, key):
    index = self.__get_index(key)
    l = self.entries[index]

    for data in l:
      if data.key == key:
        return data.value
    raise KeyError(key)

  def to_hash(self):
    r = []
    for l in self.entries:
      for data in l:
        r.append(data.to_tuple())
    return dict(r)

  def __get_index(self, key):
    return hash(key) % self.size

def test():
  h = Hash()
  print('PASS' if (1 in h) == False else 'FAIL')

  h[1] = 2
  h[2] = 3
  h[1] = 3
  h[3] = 3
  del h[3]
  print('PASS' if h.to_hash() == {1:3, 2:3} else 'FAIL')

  print('PASS' if 2 in h else 'FAIL')
  print('PASS' if h[1] == h[2] == 3 else 'FAIL')
  try:
    h[4]
  except KeyError as e:
    print('PASS')

  try:
    del h['a']
  except KeyError as e:
    print('PASS')

if __name__ == '__main__':
  test()
