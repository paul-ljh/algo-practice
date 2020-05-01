from heapq import *

class ContinuousMedian:
  def __init__(self):
    self.max_heap = []
    self.min_heap = []
    heapify(self.max_heap)
    heapify(self.min_heap)
    
  def add(self, num):
    # always keep (max_heap - min_heap) between [0,1]
    if len(self.max_heap) == len(self.min_heap):
      if len(self.max_heap) == 0 or num <= self.min_heap[0]:
        heappush(self.max_heap, num * -1)
      else:
        new_max = heappushpop(self.min_heap, num)
        heappush(self.max_heap, new_max * -1)

    else:
      if num >= self.max_heap[0] // -1:
        heappush(self.min_heap, num)
      else:
        new_min = heappushpop(self.max_heap, num * -1)
        heappush(self.min_heap, new_min // -1)
        
  def get_median(self):
    if len(self.max_heap) == 0:
      return 0
    elif len(self.max_heap) == len(self.min_heap):
      return (self.max_heap[0] // -1 + self.min_heap[0]) / 2
    else:
      return self.max_heap[0] // -1
  
def test():
  c = ContinuousMedian()
  arr = [2,5,4,3,5,1,6,7]
  ans = [2, 3.5, 4, 3.5, 4, 3.5, 4, 4.5]
  
  print('PASS' if c.get_median() == 0 else 'FAIL')
  
  for i in range(len(ans)):
    c.add(arr[i])
    print('PASS' if c.get_median() == ans[i] else 'FAIL')

if __name__ == '__main__':
  test()
