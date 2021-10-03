def paint_fill_dfs(screen, x, y, new):
  if screen[x][y] == new:
    return
  return fill(screen, x, y, screen[x][y], new)

def fill(screen, x, y, old, new):
  screen[x][y] = new
  surrounding = [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]
  for r,c in surrounding:
    if (r in range(len(screen)) and
        c in range(len(screen[0])) and
        screen[r][c] == old):
      fill(screen, r, c, old, new)
  return
  
def test():
  screen = [[0]]
  paint_fill_dfs(screen, 0, 0, 1)
  print('PASS' if screen == [[1]] else 'FAIL')
  
  screen = [[1]]
  paint_fill_dfs(screen, 0, 0, 1)
  print('PASS' if screen == [[1]] else 'FAIL')
  
  screen = [[0,0,0],
            [0,0,1],
            [0,0,0]]
  paint_fill_dfs(screen, 1, 1, 1)
  print('PASS' if screen == [
      [1,1,1],
      [1,1,1],
      [1,1,1],
    ] else 'FAIL')
  
  screen = [[0,0,0],
            [0,0,1],
            [0,1,0]]
  paint_fill_dfs(screen, 1, 1, 1)
  print('PASS' if screen == [
      [1,1,1],
      [1,1,1],
      [1,1,0],
   ] else 'FAIL')

if __name__ == '__main__':
  test()
