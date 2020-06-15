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
