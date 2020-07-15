import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from utils_python.geometry.point import Point

class Line:
  def __init__(self, p1, p2):
    self.construct_line(p1,p2)
    
  def construct_line(self, p1, p2):
    if p1.x == p2.x:
      self.slope = self.y_inter = float('inf')
      self.x_inter = p1.x
    else:
      self.slope = (p1.y - p2.y) / (p1.x - p2.x)
      self.y_inter = p1.y - self.slope * p1.x
      self.x_inter = float('inf') if self.slope == 0 else -self.y_inter / self.slope
  
  def intersect_x(self, x):
    return self.slope * x + self.y_inter
  
  def intersect_y(self, y):
    return (y - self.y_inter) / self.slope
      
  def test(self, slope, y_inter, x_inter):
    return self.slope == slope and self.y_inter == y_inter and x_inter == x_inter

def test():
  p1, p2 = Point(1,1), Point(1,2)
  line = Line(p1, p2)
  print('PASS' if line.test(float('inf'), float('inf'), p1.x) else 'FAIL')
  
  p1, p2 = Point(2,2), Point(1,2)
  line = Line(p1, p2)
  print('PASS' if line.test(0, p1.y, float('inf')) else 'FAIL')
  
  p1, p2 = Point(2,2), Point(1,1)
  line = Line(p1, p2)
  print('PASS' if line.test(1, 0, 0) else 'FAIL')
   
  p1, p2 = Point(1,1), Point(-1,3)
  line = Line(p1, p2)
  print('PASS' if line.test(-1, 2, 2) else 'FAIL')
  
if __name__ == "__main__":
  test()
  
