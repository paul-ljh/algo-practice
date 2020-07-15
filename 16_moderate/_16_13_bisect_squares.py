import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from utils_python.geometry.square import *
from utils_python.geometry.point import *
from utils_python.geometry.line import *

def bisect_squares(p1,p2,p3,p4,p5,p6,p7,p8):
  sq1 = Square(p1, p2, p3, p4)
  sq2 = Square(p5, p6, p7, p8)
  if sq1.centre == sq2.centre:
    return (
      Point(sq1.centre.x, sq1.bottom_left.y),
      Point(sq2.centre.x, sq2.top_left.y),
    )

  line = Line(sq1.centre, sq2.centre)
  sq1_intersec, sq2_intersect = None, None
  if line.slope <= 0:
    sq1_intersec, sq2_intersect = (
      (sq1.bottom_left.x, line.intersect_x(sq1.bottom_left.x)),
      (sq2.bottom_right.x, line.intersect_x(sq2.bottom_right.x)))
  else:
    sq1_intersec, sq2_intersect = (
      (line.intersect_y(sq1.bottom_left.y), sq1.bottom_left.y),
      (line.intersect_y(sq2.top_left.y), sq2.top_left.y))
  return (Point(*sq1_intersec), Point(*sq2_intersect))

def test():
  p1, p2, p3, p4 = Point(2,2), Point(4,4), Point(4,2), Point(2,4)
  print('PASS' if bisect_squares(p1,p2,p3,p4,p1,p2,p3,p4) == (Point(3,2), Point(3,4)) else 'FAIL')
  
  p1, p2, p3, p4 = Point(2,2), Point(4,4), Point(4,2), Point(2,4)
  p5, p6, p7, p8 = Point(0,0), Point(1,0), Point(1,1), Point(0,1)
  print('PASS' if bisect_squares(p1,p2,p3,p4,p5,p6,p7,p8) == (Point(2,2), Point(1,1)) else 'FAIL')
  print('PASS' if bisect_squares(p5,p6,p7,p8,p1,p2,p3,p4) == (Point(0,0), Point(4,4)) else 'FAIL')
  
  p1, p2, p3, p4 = Point(0,5), Point(0,3), Point(2,3), Point(2,5)
  p5, p6, p7, p8 = Point(3,2), Point(3,4), Point(5,2), Point(5,4)
  print('PASS' if bisect_squares(p1,p2,p3,p4,p5,p6,p7,p8) == (Point(0,13/3), Point(5,8/3)) else 'FAIL')

if __name__ == "__main__":
  test()
