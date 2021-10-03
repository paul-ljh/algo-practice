'''
Write a method to shuffle a deck of cards. It must be a perfect shuffle -- in other words, each of the 52! permutations of the deck has to be equally likely. Assume that you are given a random number generator which is perfect.
'''

from random import randint

def shuffle():
  num_cards = 52
  cards = [i for i in range(num_cards)]
  for i in range(num_cards):
    rand_index = randint(i, num_cards-1)
    temp = cards[i]
    cards[i] = cards[rand_index]
    cards[rand_index] = temp
  return cards

def test():
  result = shuffle()
  print('PASS' if set(result) == set(list(range(52))) else 'FAIL')

if __name__ == "__main__":
  test()
