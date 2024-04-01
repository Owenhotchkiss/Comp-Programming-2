def main():
    try:
      with open("Landdat/prog213f.dat, 'r'") as f:
        for line in f:
            ldata = line.split(" ")

    except Exception as e:
      print("Error:", e)



if __name__ == "__main__":
  main()