class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __eq__(self, other):
    if isinstance(other, Point):
      return (self.x == other.x and self.y == other.y)
    return NotImplemented
  
  def __str__(self):
    return f"({self.x}, {self.y})"
  
  def calculate_slope(self, other):
    if isinstance(other, Point):
      delta_x = other.x - self.x
      delta_y = other.y - self.y
      slope = float('inf') if delta_x == 0 else delta_y / delta_x 
      return slope
    else:
      raise Exception('Argument has to be of Point type')
    
