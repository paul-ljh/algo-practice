from math import log

def get_bit(num, i):
  if i < 0 or i > int(log(num, 2)):
    return None
  mask = 1 << i
  return mask & num != 0

def set_bit(num, i):
  if i < 0 or i > int(log(num, 2)):
    return None
  mask = 1 << i
  return mask | num

'''
Int in python has 64 bits
1 if non-negative, 0 otherwise
'''
def get_sign(n):
  sign_mask = 1 << 63
  return int(n & sign_mask == 0)

'''compute the 2's complement of val'''
def twos_comp(bin_seq):
  mask = 1 << 63
  result = 0
  result += bin_seq & (mask - 1)
  if get_sign(bin_seq) == 0:
    result -= mask
  return result
