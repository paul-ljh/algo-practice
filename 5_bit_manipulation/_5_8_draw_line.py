from math import ceil

def draw_line(screen, width, x1, x2, y):
  full_start = ceil(x1 / 8)
  full_stop = (x2 + 1) // 8
  for i in range(full_start, full_stop):
    screen[y * width // 8 + i] = 0xff
    
  start, end = x1 % 8, x2 % 8
  if start != 0 or end != 7:
    if x1 // 8 == x2 // 8:
      mask = 0xff
      mask &= (1 << (8-start)) - 1
      mask ^= (1 << (8-end-1)) - 1
      screen[y * width // 8 + x1 // 8] |= mask
    else:
      front_mask = 0xff
      front_mask &= (1 << (8-start)) - 1
      screen[y * width // 8 + x1 // 8] |= front_mask
      
      back_mask = 0xff
      back_mask ^= (1 << (8-end-1)) - 1
      screen[y * width // 8 + x2 // 8] |= back_mask
  return screen

def test():
  screen = [0x00,0x00,0x00,0x00,0x00,0x00]
  answer = [0x40,0x00,0x00,0x00,0x00,0x00]
  width, x1, x2, y = 8, 1, 1, 0
  print('PASS' if draw_line(screen, width, x1, x2, y) == answer else 'FAIL')
  
  screen = [0x00,0x00,0x00,0x00,0x00,0x00]
  answer = [0b111111,0x00,0x00,0x00,0x00,0x00]
  width, x1, x2, y = 8, 2, 7, 0
  print('PASS' if draw_line(screen, width, x1, x2, y) == answer else 'FAIL')
  
  screen = [0x00,0x00,0x00,0x00,0x00,0x00]
  answer = [0x00,0x00,0x00,0x00,0b1111111,0xff]
  width, x1, x2, y = 16, 1, 15, 2
  print('PASS' if draw_line(screen, width, x1, x2, y) == answer else 'FAIL')
  
  screen = [0x00,0x00,0x00,0x00,0x00,0x00]
  answer = [0x00,0x00,0x00,0xff,0b11111110,0x00]
  width, x1, x2, y = 8, 0, 14, 3
  print('PASS' if draw_line(screen, width, x1, x2, y) == answer else 'FAIL')
  
  screen = [0x00,0x00,0x00,0x00,0x00,0x00]
  answer = [0x00,0x00,0x00,0b111111,0xff,0b11111110]
  width, x1, x2, y = 24, 2, 22, 1
  print('PASS' if draw_line(screen, width, x1, x2, y) == answer else 'FAIL')

if __name__ == "__main__":
  test()
