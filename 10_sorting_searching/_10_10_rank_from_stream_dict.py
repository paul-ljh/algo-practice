class RankStream:
  def __init__(self):
    self.ranks = {}
    
  def track(self, elem):
    new_key = elem not in self.ranks
    self.ranks[elem] = self.ranks.get(elem, 0) + 1
    for k in self.ranks.keys():
      if new_key and k < elem:
        self.ranks[elem] += self.ranks[k]
      if k > elem:
        self.ranks[k] += 1
  
  def get_rank_of(self, elem):
    if elem in self.ranks:
      return self.ranks[elem] - 1
    else:
      return None
    
def test():
  int_stream = [5,5,6,5,1,1,0]
  r = RankStream()
  for elem in int_stream:
    r.track(elem)
  
  print('PASS' if r.get_rank_of(0) == 0 else 'FAIL')
  print('PASS' if r.get_rank_of(1) == 2 else 'FAIL')
  print('PASS' if r.get_rank_of(5) == 5 else 'FAIL')
  print('PASS' if r.get_rank_of(6) == 6 else 'FAIL')
  print('PASS' if r.get_rank_of(7) == None else 'FAIL')

if __name__ == '__main__':
  test()
  
