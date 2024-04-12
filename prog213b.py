quant = int(input("Enter the amount of products you're buying"))
cpi = 0
if 0 < quant and quant < 99:
  cpi = 5.95
elif quant > 99 and quant < 199:
  cpi = 5.75
elif quant > 199 and quant < 299:
  cpi = 5.40
elif quant > 99 and quant < 199:
  cpi = 5.75
elif quant > 300:
  cpi = 5.15
price = quant * cpi
print(str(price))