import sys
sys.setrecursionlimit(5000)



def fact(n):
  if n == 3:  return 3   #Base?Ending Case
  return n + fact(n-3)   #Recursive Case

def main():
  print(str(fact(9669)))

if __name__ == "__main__":
  main()