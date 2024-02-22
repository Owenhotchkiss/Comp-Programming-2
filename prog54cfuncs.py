


def calcArea(radius, pi) -> float:
  return radius**2 * pi


def calcCircumference(radius: int , pi: int) -> int:
  return 2 * pi * radius
def main():
  radius = float(input("Enter radius here:"))
  pi = 3.14
  area = calcArea(radius, pi)
  circumference = calcCircumference(radius, pi)
  print(str(area))
  print(str(circumference))
  pass


if __name__ == "__main__":
  main()