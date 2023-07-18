'''
https://leetcode.com/problems/pacific-atlantic-water-flow/description/

Flow from the 4 borders inwards into the matrix, any cells that are reachable can flow into pacific/atlantic
'''
import sys
sys.path.append('../../utils_python')

from queue import Queue

def pacific_atlantic(heights):
  pacific_q = Queue()
  atlantic_q = Queue()

  rows, cols = len(heights), len(heights[0])
  pacific_visited = [[False] * cols for _ in range(rows)]
  atlantic_visited = [[False] * cols for _ in range(rows)]

  for i in range(rows):
    pacific_q.put((i, 0))
    atlantic_q.put((i, cols - 1))
    pacific_visited[i][0] = True
    atlantic_visited[i][cols - 1] = True

  for i in range(cols):
    pacific_q.put((0, i))
    atlantic_q.put((rows - 1, i))
    pacific_visited[0][i] = True
    atlantic_visited[rows - 1][i] = True

  bfs(heights, pacific_q, pacific_visited, rows, cols)
  bfs(heights, atlantic_q, atlantic_visited, rows, cols)

  results = set()
  for r in range(rows):
    for c in range(cols):
      if pacific_visited[r][c] == atlantic_visited[r][c] == True:
        results.add((r,c))
  return results

def bfs(heights, q, visited, rows, cols):
  while not q.empty():
    x, y = q.get()
    level = heights[x][y]
    for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
      r, c = x + i, y + j
      if r in range(rows) and c in range(cols) and not visited[r][c] and heights[r][c] >= level:
        visited[r][c] = True
        q.put((r,c))
  return

def test():
  heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
  print('PASS' if pacific_atlantic(heights) == set([(0,4),(1,3),(1,4),(2,2),(3,0),(3,1),(4,0)]) else 'FAIL')

if __name__ == '__main__':
  test()
