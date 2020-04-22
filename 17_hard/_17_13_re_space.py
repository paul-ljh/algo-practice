from sys import maxsize
from pprint import pprint

class Result:
  def __init__(self, invalid=None, output=None):
    self.invalid = invalid
    self.output = output
    
def re_space(d, document):
  cache = [Result() for i in range(len(document))] 
  cache.append(Result(0, []))
  find_optimal(d, document, 0, cache)
  return ' '.join(cache[0].output)

def find_optimal(d, document, start, cache):
  if start == len(document) or cache[start].output:
    return

  best_invalid, best_output = maxsize, []
  i = start
  while i < len(document):
    curr_invalid = 0 if document[start:i+1] in d else i+1-start
    if curr_invalid <= best_invalid:
      find_optimal(d, document, i+1, cache)
      if cache[i+1].invalid + curr_invalid <= best_invalid:
        best_invalid = cache[i+1].invalid + curr_invalid
        best_output = [document[start:i+1]] + cache[i+1].output
        if best_invalid == 0:
          break
    i += 1
  cache[start].invalid, cache[start].output = best_invalid, best_output
  return

def test():
  d = {'random', 'paul', 'lii'}
  document = 'jesslikedthatIdotoo'
  result = re_space(d, document)
  print('PASS' if result == 'jesslikedthatIdotoo' else 'FAIL')
  
  d = {'jess', 'that', 'jessliked', 'I', 'do', 'too'}
  document = 'jesslikedthatIdotoo'
  result = re_space(d, document)
  print('PASS' if result == 'jessliked that I do too' else 'FAIL')
  
  d = {'her', 'herb', 'brother', 'other'}
  document = 'timherbrother'
  result = re_space(d, document)
  print('PASS' if result == 'tim her brother' else 'FAIL')
  
  d = {'looked', 'just', 'like', 'her', 'herb', 'brother', 'other'}
  document = 'jesslookedjustliketimherbrother'
  result = re_space(d, document)
  print('PASS' if result == 'jess looked just like tim her brother' else 'FAIL')

if __name__ == '__main__':
  test()
