import sys
import time

f = open("pentis.txt", "r+")
a = 2
b = 0
charcount = 0
sys.set_int_max_str_digits(2147483647)

with open("pentis.txt", "r+") as f:
  charcount = len(f.read())
  print("iterated (" + str(b) + ") times, " + str(charcount) + " digits long")
time.sleep(0.5)

while True:
  f = open("pentis.txt", "r+")
  a = int(f.read())
  a *= 2
  f.write(str(a))
  b += 1
  with open("pentis.txt", "r+") as f:
    charcount = len(f.read())
    print("iterated (" + str(b) + ") times, " + str(charcount) + " digits long")
  f.close()
  time.sleep(0.5)