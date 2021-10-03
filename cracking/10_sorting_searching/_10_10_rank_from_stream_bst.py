class BiNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.left_count = 0
    
  def insert(self, elem):
    if self.data >= elem:
      self.left_count += 1
      if self.left:
        return self.left.insert(elem)
      else:
        self.left = BiNode(elem)
        return
    else:
      if self.right:
        return self.right.insert(elem)
      else:
        self.right = BiNode(elem)
        return
  
  def get_rank_of(self, elem):
    if self.data == elem:
      return self.left_count
    elif self.data > elem:
      if self.left:
        return self.left.get_rank_of(elem)
      else:
        return None
    else:
      if self.right:
        r_count = self.right.get_rank_of(elem)
        return r_count if r_count is None else r_count + 1 + self.left_count
      else:
        return None
    

class RankStream:
  def __init__(self):
    self.ranks = None
    
  def track(self, elem):
    if self.ranks:
      self.ranks.insert(elem)
    else:
      self.ranks = BiNode(elem)
  
  def get_rank_of(self, elem):
    if self.ranks:
      return self.ranks.get_rank_of(elem)
    else:
      return None
    
def test():
  r = RankStream()
  
  print('PASS' if r.get_rank_of(5) == None else 'FAIL')
  r.track(5)
  print('PASS' if r.get_rank_of(5) == 0 else 'FAIL')
  r.track(-1)
  print('PASS' if r.get_rank_of(5) == 1 else 'FAIL')
  r.track(10)
  r.track(-5)
  r.track(0)
  print('PASS' if r.get_rank_of(10) == 4 else 'FAIL')
  print('PASS' if r.get_rank_of(-11) == None else 'FAIL')
  print('PASS' if r.get_rank_of(1) == None else 'FAIL')
  r.track(6)
  r.track(15)
  print('PASS' if r.get_rank_of(6) == 4 else 'FAIL')
  print('PASS' if r.get_rank_of(15) == 6 else 'FAIL')

if __name__ == '__main__':
  test()
  
