class Shape:
  # Constructor sets up class data
  def __init__(self, length, width):
    self.length = length
    self.width = width
    self._area = 0 #_prefix basically means 'private' so 
    self._perim = 0 # it should only be called in the class

  # Mutators/setters modify class data
  def calculate(self):
    self._area = self.length * self.width
    self._perim = 2 * self.width + 2 * self.length

  def setLength(self, length):
    self.length = length

  # Accessor/Getter: returns class data
  def getArea(self):
    return self._area

  def getPerimeter(self):
    return self._perim
  

def main():
  len = int(input("Enter Length: "))
  wid = int(input("Enter width"))
  # Make a new 'shape' object
  shape = Shape(len, wid) # Call the "shape" constructor
  # shape.setLength(5)
  shape.calculate()
  print("Area:", shape.getArea())
  print("Perimeter:", shape.getPerimeter())
  pass


if __name__ == "__main__":
  main()