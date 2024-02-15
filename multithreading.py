import time
import threading as th

def print_nums(start, end, delay):
  for i in range(start, end):
    time.sleep(delay)
    print(i, " ")

def print_lets(delay):
   for letter in "abcdefghij":
     time.sleep(delay)
     print(letter)
     
t1 = th.Thread(target=print_nums, args=(1, 100000, 0.001)).start()
t2 = th.Thread(target=print_nums, args=(11, 100000, 0.001)).start()
t3 = th.Thread(target=print_nums, args=(11, 100000, 0.001)).start()
t4 = th.Thread(target=print_nums, args=(11, 100000, 0.001)).start()
t5 = th.Thread(target=print_nums, args=(11, 100000, 0.001)).start()
t6 = th.Thread(target=print_nums, args=(11, 100000, 0.001)).start()
# Wait for threads to complete before exiting
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()