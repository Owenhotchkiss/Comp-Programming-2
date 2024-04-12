class Shape:
  # Constructor sets up class data
  def __init__(self, radius):
    self._radius = radius

  # Mutators/setters modify class data
  def calculate(self):
    self._area = 3.14 * self._radius**2
    self._circum = 2 * 3.14 * self._radius

  # Accessor/Getter: returns class data
  def getArea(self):
    return self._area

  def getCircumfrence(self):
    return self._circum


def main():
  radius = int(input("Enter radius: "))
  # Make a new 'shape' object
  shape = Shape(radius)  # Call the "shape" constructor
  # shape.setLength(5)
  shape.calculate()
  print("Area:", shape.getArea())
  print("Perimeter:", shape.getCircumfrence())
  pass


if __name__ == "__main__":
  main()
