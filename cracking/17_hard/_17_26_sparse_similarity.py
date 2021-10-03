def sparse_similarity(d):
  intersection, elem = {}, {}
  ids = list(d.keys())
  for i in range(len(ids)-1):
    if len(d[ids[i]]) != 0:
      for word in d[ids[i]]:
        if word not in elem:
          elem[word] = set()
          for j in range(i+1, len(ids)):
            if word in d[ids[j]]:
              elem[word].add(ids[j])
          if len(elem[word]) == 0:
            elem.pop(word)
      compute_intersection(intersection, elem, ids[i], d[ids[i]])
  compute_similarities(intersection, d)
  return intersection

def compute_intersection(intersection, elem, doc_id, doc):
  words = list(elem.keys())
  for word in words:
    if word in doc:
      if doc_id in elem[word]:
        elem[word].remove(doc_id)
      if len(elem[word]) == 0:
        elem.pop(word)
      else:
        for other_id in elem[word]:
          intersection[(doc_id, other_id)] = intersection.get((doc_id, other_id), 0) + 1

def compute_similarities(intersection, d):
  for pair, count in intersection.items():
    intersection[pair] = count / (len(d[pair[0]]) + len(d[pair[-1]]) - count)
    
def test():
  d = {'a': set([1,2,3,4,5]),
       'b': set([6,7,8]),
       'c': set([9,10,11,12,13,14]),
       'd': set([15,16,17,18,19]),
       'e': set()}
  result = {}
  print('PASS' if sparse_similarity(d) == result else 'FAIL')
  
  d = {'a': set([1,2,3,4]),
       'b': set([1,2,3,4]),
       'c': set([1,2,3,4]),
       'd': set([1,2,3,4]),
       'e': set()}
  result = {('a','b'): 1,
            ('a','c'): 1,
            ('a','d'): 1,
            ('b','c'): 1,
            ('b','d'): 1,
            ('c','d'): 1}
  print('PASS' if sparse_similarity(d) == result else 'FAIL')
  
  d = {'a': set([10,14,15,9,3]),
       'b': set([10,5,7,16]),
       'c': set([9,12,17,22,25]),
       'd': set([3,9,16,10,17,22]),
       'e': set()}
  result = {('a', 'd'): 0.375,
            ('a', 'c'): 0.1111111111111111,
            ('a', 'b'): 0.125,
            ('b', 'd'): 0.25,
            ('c', 'd'): 0.375}
  print('PASS' if sparse_similarity(d) == result else 'FAIL')
  
  d = {'a': set([100,14,15,9,3]),
       'b': set([32,1,9,3,5]),
       'c': set([15,29,2,6,8,7]),
       'd': set([7,10])}
  result = {('a', 'b'): 0.25,
            ('a', 'c'): 0.1,
            ('c', 'd'): 0.14285714285714285}
  print('PASS' if sparse_similarity(d) == result else 'FAIL')


if __name__ == '__main__':
  test()
  
