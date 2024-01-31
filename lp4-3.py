eggs = int(input("Enter number of eggs to be purchased: "))
dozens = eggs // 12
remainder = eggs % 12
price = 0.0

if 0 < dozens < 4:
  price = 0.5
elif 4 < dozens < 6:
  price = 0.45
elif 6 < dozens < 11:
  price = 0.40
elif 11 < dozens:
  price = 0.35

numeggs = (dozens * 12)
total = numeggs * price
print("Total Price is: $" + str(total))