# def intersection(p1, p2, p3, p4):
#   x_range = calculate_range(p1[0], p2[0], p3[0], p4[0])
#   y_range = calculate_range(p1[1], p2[1], p3[1], p4[1])
#   if x_range[0] > x_range[-1] or y_range[0] > y_range[-1]:
#     return None
#   a1, b1, c1 = calculate_line(p1, p2)
#   a2, b2, c2 = calculate_line(p3, p4)
#   if a1 == a2:
#     for p in [p1, p2, p3, p4]:
#       if p[0] == x_range[0]:
#         return p
#   else:
#     denom = c2 * a1 - a2 * c1
#     x = (b2 * c1 - b1 * c2) / denom
#     y = (b2 * a1 - b1 * a2) / denom
#     if x_range[0] <= x <= x_range[-1] and y_range[0] <= y <= y_range[-1]:
#       return (x,y)
#     else:
#       return None        
  
# def calculate_line(p1, p2):
#   (x1, y1), (x2, y2) = p1, p2
#   if x1 == x2:
#     return (1, -x1, 0)
#   elif y1 == y2:
#     return (0, y1, 1)
#   else:
#     return (
#       (y1-y2)/(x1-x2),
#       (x2*y1 - x1*y2)/(x2-x1),
#       1
#     )

from math import isinf;

def calculate_range(c1, c2, c3, c4):
  return (max(min(c1, c2), min(c3, c4)),
          min(max(c1, c2), max(c3, c4)))

def intersection(p1, p2, p3, p4):
  x_range = calculate_range(p1[0], p2[0], p3[0], p4[0])
  y_range = calculate_range(p1[1], p2[1], p3[1], p4[1])
  if x_range[0] > x_range[-1] or y_range[0] > y_range[-1]:
    return None

  slope1, y_inter1 = calculate_line(p1, p2)
  slope2, y_inter2 = calculate_line(p3, p4)

  if slope1 == slope2 and y_inter1 == y_inter2:
      for p in [p1, p2, p3, p4]:
        if p[0] == x_range[0]:
          return p
  elif slope1 != slope2:
    # There is a vertical line
    if isinf(slope1):
      x = p1[0]
      y = x * slope2 + y_inter2
    elif isinf(slope2):
      x = p3[0]
      y = x * slope1 + y_inter1
    else:
      x = (y_inter1 - y_inter2) / (slope2 - slope1)
      y = x * slope1 + y_inter1

    if x_range[0] <= x <= x_range[-1] and y_range[0] <= y <= y_range[-1]:
      return (x,y)
  return None
    
def calculate_line(p1, p2):
  delta_x = p1[0] - p2[0]
  delta_y = p1[1] - p2[1]
  if delta_x == 0:
    y_inter = slope = float('inf')
  else:
    slope = delta_y / delta_x
    y_inter = p1[1] - p1[0] * slope
  return (slope, y_inter)

def test():
  # 2 identical points
  p1, p2, p3, p4 = (2,3), (2,3), (2,3), (2,3)
  answer = (2,3)
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')

  # 2 points
  p1, p2, p3, p4 = (2,3), (2,3), (3,4), (3,4)
  answer = None
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')
  
  # point, horizontal
  p1, p2, p3, p4 = (2,3), (2,3), (1,3), (3,3)
  answer = (2,3)
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')
    
  # point, horizontal
  p1, p2, p3, p4 = (2,3), (2,3), (1,4), (3,4)
  answer = None
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')
  
  # point, vertical
  p1, p2, p3, p4 = (2,3), (2,3), (2,1), (2,4)
  answer = (2,3)
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')

  # point, vertical
  p1, p2, p3, p4 = (2,3), (2,3), (3,1), (3,4)
  answer = None
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')

  # point, regular  
  p1, p2, p3, p4 = (2,3), (2,3), (0,1), (1,0)
  answer = None
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')
  
  # point, regular  
  p1, p2, p3, p4 = (2,3), (2,3), (0,5), (5,0)
  answer = (2,3)
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')

  # regular, regular
  p1, p2, p3, p4 = (1,1), (5,1), (0,-1), (4,2)
  answer = (8/3,1)
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')
  
  # regular, regular
  p1, p2, p3, p4 = (0,0), (1,1), (0,5), (5,0)
  answer = None
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')
  
  # parallel, overlapped
  p1, p2, p3, p4 = (0,0), (2.5,2.5), (1,1), (4,4)
  answer = (1,1)
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')
  
  # parallel, non-overlapped
  p1, p2, p3, p4 = (0,0), (2,2), (5,5), (7,7)
  answer = None
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')
  
  # parallel, different y-intercept
  p1, p2, p3, p4 = (0,0), (2,2), (1,0), (5,4)
  answer = None
  print('PASS' if intersection(p1, p2, p3, p4) == answer else 'FAIL')

if __name__ == "__main__":
  test()

