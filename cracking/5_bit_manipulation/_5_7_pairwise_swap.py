from sys import maxsize

def pairwise_swap(num):
  return (((0xaaaa_aaaa & num) >> 1) & maxsize) | ((0x5555_5555 & num) << 1)

def test():
  num = 0b0
  answer = 0b0
  print('PASS' if pairwise_swap(num) == answer else 'FAIL')

  num = 0b1
  answer = 0b10
  print('PASS' if pairwise_swap(num) == answer else 'FAIL')

  num = 0b01001110
  answer = 0b10001101
  print('PASS' if pairwise_swap(num) == answer else 'FAIL')

if __name__ == "__main__":
  test()
