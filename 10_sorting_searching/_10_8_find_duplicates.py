class BitVector:
  def __init__(self, num_bits):
    self.vector = [0] * (num_bits >> 5 + 1)
  
  def get_bit(self, pos):
    mask = 1 << (pos & 0x1f)
    index = pos >> 5
    return mask & self.vector[index] != 0
  
  def set_bit(self, pos):
    mask = 1 << (pos & 0x1f)
    index = pos >> 5
    self.vector[index] |= mask

def find_duplicates(arr):
  bit_vector = BitVector(32000)
  result = set()
  for elem in arr:
    if bit_vector.get_bit(elem-1):
      result.add(elem)
    else:
      bit_vector.set_bit(elem-1)
  return result

def test():
  arr = [1,2,3,4,5,6,7,32,33,34,35]
  print('PASS' if find_duplicates(arr) == set([]) else 'FAIL')
  
  arr = [1,2,3,4,5,6,4,7,32,33,34,35,33,32]
  print('PASS' if find_duplicates(arr) == set([32,33,4]) else 'FAIL')
  

if __name__ == '__main__':
  test()
