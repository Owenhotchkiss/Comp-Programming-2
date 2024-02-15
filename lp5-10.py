num = int(input("Enter a Number: "))
num2 = int(input("Enter Another Number: "))
while (num2 > 0):
  temp = num % num2
  num = num2
  num2 = temp
print(str(num))