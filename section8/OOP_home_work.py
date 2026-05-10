
class Line:
  def __init__(self, coordinates1, coordinates2):
    self.coordinates1 = coordinates1
    self.coordinates2 = coordinates2

  def distance(self):
    x1, y1 = self.coordinates1
    x2, y2 = self.coordinates2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

  def slope(self):
    x1, y1 = self.coordinates1
    x2, y2 = self.coordinates2
    if x2 - x1 == 0:
      return float('inf')
    return (y2 - y1) / (x2 - x1)
  
c1=(8, 2)
c2=(8, 10)
my_line = Line(c1, c2)
print(my_line.distance())  # Output: 10.0
print(my_line.slope())  # Output: inf