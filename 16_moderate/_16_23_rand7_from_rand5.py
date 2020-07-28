'''
Implement a method called rand7() given rand5(). That is, given a method that generates a random integer between 0 and 4, all inclusive, write a method that generates a random integer between 0 and 6, all inclusive.
'''

from random import randint

def rand7():
  while True:
    first, second = rand5(), rand5()
    product, sum_total = first * second, first + second
    if sum_total == 0 or sum_total == 1:
      return 0
    elif sum_total == 2:
      return 1
    elif sum_total == 6:
      return 2
    elif sum_total == 7 or sum_total == 8:
      return 3
    else:
      if product == 0:
        continue
      elif product == 4:
        return 4
      elif second > first:
        return 5
      elif first > second:
        return 6

def rand5():
  return randint(0,4)

if __name__ == "__main__":
  for i in range(10):
    print(rand7())
