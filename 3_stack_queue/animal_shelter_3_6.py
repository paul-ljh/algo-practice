import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from my_queue import Queue

class Animal:
  VALID_SPECIES = ['cat', 'dog']
  def __init__(self, *, name, species, counter):
    self.name = name
    self.species = species
    self.counter = counter

class AnimalShelter:
  def __init__(self):
    self.dogs = Queue()
    self.cats = Queue()
    self.counter = 0

  def enqueue(self, *, name, species):
    if species in Animal.VALID_SPECIES:
      self.counter += 1
      getattr(self, f"{species}s").push(
        Animal(name=name, species=species, counter=self.counter)
      )
    else:
      raise AttributeError("INVALID TYPE")

  def dequeue_cat(self):
    if self.cats.is_empty():
      raise IndexError("EMPTY CAT QUEUE")
    else:
      return self.cats.pop().name

  def dequeue_dog(self):
    if self.dogs.is_empty():
      raise IndexError("EMPTY DOG QUEUE")
    else:
      return self.dogs.pop().name
  
  def dequeue_any(self):
    if self.dogs.is_empty() and self.cats.is_empty():
      raise IndexError("EMPTY QUEUE")
    elif self.dogs.is_empty():
      return self.dequeue_cat()
    elif self.cats.is_empty():
      return self.dequeue_dog()
    else:
      return self.dequeue_cat() if self.dogs.peek().counter > self.cats.peek().counter else self.dequeue_dog()

def test():
  shelter = AnimalShelter()
  try:
    shelter.enqueue(name='paul', species='human')
  except AttributeError as err:
    print(err)

  try:
    shelter.dequeue_any()
  except IndexError as err:
    print(err)
  
  shelter.enqueue(name='calvin', species='cat')
  shelter.enqueue(name='bob', species='cat')
  shelter.enqueue(name='alice', species='dog')

  print('PASS' if shelter.dequeue_any() == 'calvin' else 'FAIL')
  print('PASS' if shelter.dequeue_any() == 'bob' else 'FAIL')
  print('PASS' if shelter.dequeue_any() == 'alice' else 'FAIL')
  try:
    shelter.dequeue_any()
  except IndexError as err:
    print(err)

  try:
    shelter.dequeue_cat()
  except IndexError as err:
    print(err)

  try:
    shelter.dequeue_dog()
  except IndexError as err:
    print(err)

if __name__ == '__main__':
    test()
