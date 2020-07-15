import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from utils_python.geometry.point import Point

class Square:
  def __init__(self,p1,p2,p3,p4):
    self.order_corners(p1,p2,p3,p4)
    self.calculate_centre()
  
  def validate_points(self):
    pass
    
  # Tailered for 16.13, assume square's top and bottom lines are parallel to x axis
  def order_corners(self,p1,p2,p3,p4):
    line1, line2 = [], []
    for p in [p1,p2,p3,p4]:
      if p.y == p1.y:
        line1.append(p)
      else:
        line2.append(p)
    
    line1.sort(key=lambda pt: pt.x)
    line2.sort(key=lambda pt: pt.x)
    if line1[0].y < line2[0].y:
      self.bottom_left, self.bottom_right = line1
      self.top_left, self.top_right = line2
    else:
      self.top_left, self.top_right = line1
      self.bottom_left, self.bottom_right = line2
    return
  
  def calculate_centre(self):
    self.centre = Point(
      (self.bottom_left.x + self.bottom_right.x) / 2,
      (self.bottom_left.y + self.top_left.y) / 2,
    )

    
def test():
  p1, p2, p3, p4 = Point(2,2), Point(4,4), Point(4,2), Point(2,4)
  sq = Square(p1,p2,p3,p4)
  print('PASS' if sq.centre == Point(3,3) else 'FAIL')
  print('PASS' if sq.bottom_left == Point(2,2) else 'FAIL')
  print('PASS' if sq.bottom_right == Point(4,2) else 'FAIL')
  print('PASS' if sq.top_left == Point(2,4) else 'FAIL')
  print('PASS' if sq.top_right == Point(4,4) else 'FAIL')

if __name__ == "__main__":
  test()
