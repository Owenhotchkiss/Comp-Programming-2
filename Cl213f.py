# Cl213f.py
class Cl213f:
  def __init__(self, kwh):
      self.kwh = kwh
      self.cost = 0.0

  def calc(self):
    costPerHr = 0
    kwh = 0
    price = 0
    if kwh < 2000:
      costPerHr = 0.07
    elif 2000 < kwh < 8000:
      costPerHr = 0.05
    elif 8000 < kwh < 10000:
      costPerHr = 0.04
    price = costPerHr * kwh
    print(price)
      
    
    
    pass

  def __str__(self):
    return f"The cost of {self.kwh} is"