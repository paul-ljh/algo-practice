import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from my_queue import Queue

def paint_fill_bfs(screen, x, y, new):
  old = screen[x][y]
  if old == new:
    return
  q = Queue()
  q.push((x,y))
  screen[x][y] = new

  while q.length > 0:
    r, c = q.pop()
    surrounding = [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]
    for t,s in surrounding:
      if (t in range(len(screen)) and
        s in range(len(screen[0])) and
        screen[t][s] == old):
        screen[t][s] = new
        q.push((t,s))
  return
  
def test():
  screen = [[0]]
  paint_fill_bfs(screen, 0, 0, 1)
  print('PASS' if screen == [[1]] else 'FAIL')
  
  screen = [[1]]
  paint_fill_bfs(screen, 0, 0, 1)
  print('PASS' if screen == [[1]] else 'FAIL')
  
  screen = [[0,0,0],
            [0,0,1],
            [0,0,0]]
  paint_fill_bfs(screen, 1, 1, 1)
  print('PASS' if screen == [
      [1,1,1],
      [1,1,1],
      [1,1,1],
    ] else 'FAIL')
  
  screen = [[0,0,0],
            [0,0,1],
            [0,1,0]]
  paint_fill_bfs(screen, 1, 1, 1)
  print('PASS' if screen == [
      [1,1,1],
      [1,1,1],
      [1,1,0],
   ] else 'FAIL')

if __name__ == '__main__':
  test()
