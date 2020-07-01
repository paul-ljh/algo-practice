class Book:
  def __init__(self, book):
    self.book = book
    self.build_occurrences()
    
  def build_occurrences(self):
    self.occurrences = {}
    for word in self.book:
      self.occurrences[word] = self.occurrences.get(word, 0) + 1
  
  def word_frequencies(self, word):
    if not word or word not in self.occurrences:
      return None
    else:
      return self.occurrences[word]

def test():
  book = ['paul', 'li', 'test', 'paul']
  b = Book(book)
  
  word = 'paul'
  answer = 2
  print('PASS' if b.word_frequencies(word) == answer else 'FAIL')
  
  word = 'li'
  answer = 1
  print('PASS' if b.word_frequencies(word) == answer else 'FAIL')
  
  word = ''
  answer = None
  print('PASS' if b.word_frequencies(word) == answer else 'FAIL')
  
  word = 'random'
  answer = None
  print('PASS' if b.word_frequencies(word) == answer else 'FAIL')

if __name__ == "__main__":
  test()
