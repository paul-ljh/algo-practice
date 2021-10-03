def missing_int(ints):
  range_size = 1 << 20
  
  counts = get_block_counts(ints, range_size)
  
  block_index = find_missing_block(counts, range_size)
  if block_index is None:
    return None
  
  bit_vector = fill_bit_vector(ints, block_index, range_size)
  index = find_missing_bit(bit_vector)
  if index is None:
    return None

  return block_index * range_size + index

def get_block_counts(ints, range_size):
  counts = [0] * (2**31 // range_size + 1)
  for elem in ints:
    counts[elem // range_size] += 1
  return counts

def find_missing_block(counts, range_size):
  for i in range(len(counts)):
    if counts[i] != range_size:
      return i
  return None

def fill_bit_vector(ints, block_index, range_size):
  left, right = block_index * range_size, (block_index+1) * range_size
  bit_vector = 0
  for item in ints:
    if item in range(left, right):
      bit_vector |= 1 << (item - left)
  return bit_vector

def find_missing_bit(bit_vector):
  for i in range(bit_vector.bit_length()):
    if 1 << i & bit_vector == 0:
      return i
  return None

def test():
  ints = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16]
  print('PASS' if missing_int(ints) == 14 else 'FAIL')

  ints = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16]
  print('PASS' if missing_int(ints) == 0 else 'FAIL')
  
  ints = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
  print('PASS' if missing_int(ints) is None else 'FAIL')


if __name__ == '__main__':
    test()
