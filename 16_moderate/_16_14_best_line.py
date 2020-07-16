'''
Given a 2D graph with points on it, find a line which passes the most number of points.
'''

import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from utils_python.geometry.point import Point

def best_line(points):
  best_slope, best_occur = None, 0
  l = len(points)
  threshold = l // 2 + 1
  for i in range(l):
    if best_occur >= threshold:
      break;
    slope_occur = {}
    identical_pts = 0
    for j in range(i+1, l):
      if points[i] == points[j]:
        identical_pts += 1
      else:
        curr_slope = points[i].calculate_slope(points[j])
        slope_occur[curr_slope] = slope_occur.get(curr_slope, 1) + 1

    curr_best_slope = max(slope_occur, key=slope_occur.get, default=None)
    curr_best_occur = slope_occur.get(curr_best_slope, 1) + identical_pts
    if curr_best_occur > best_occur:
      best_slope, best_occur = curr_best_slope, curr_best_occur
  return (best_slope, best_occur)

def test():
  points = []
  answer = (None, 0)
  print('PASS' if best_line(points) == answer else 'FAIL')

  points = [Point(2,2), Point(2,2), Point(2,2), Point(2,2), Point(2,2)]
  answer = (None, 5)
  print('PASS' if best_line(points) == answer else 'FAIL')
  
  points = [Point(2,2), Point(4,2), Point(1,1), Point(3,1), Point(5,1), Point(3,1)]
  answer = (0, 4)
  print('PASS' if best_line(points) == answer else 'FAIL')
  
  points = [Point(1,1), Point(3,1), Point(5,1), Point(3,1), Point(2,2), Point(4,2)]
  answer = (0, 4)
  print('PASS' if best_line(points) == answer else 'FAIL')

if __name__ == "__main__":
  test()
