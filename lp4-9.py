import random
rnd = random.randint(1, 20)
num = int(input("Enter a number between 1 and 20: "))
print(rnd)
if rnd == num:
  print("You Won!!")
else:
  print("Better Luck Next Time!!")