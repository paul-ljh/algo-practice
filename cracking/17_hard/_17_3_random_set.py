'''
Write a method to randomly generate a set of m integers from an array of size n. Each element must have equal probability of being chosen.
'''

from random import randint

def random_set(arr, m):
  for i in range(m):
    rand_index = randint(i, len(arr)-1)
    temp = arr[i]
    arr[i] = arr[rand_index]
    arr[rand_index] = temp
  return arr[:m]
