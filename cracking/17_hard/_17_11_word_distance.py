import sys

def group_words(words):
  words_dict = {}
  for i in range(len(words)):
    if words[i] not in words_dict:
      words_dict[words[i]] = []
    words_dict[words[i]].append(i)
  return words_dict

def word_distance(word1, word2, words_dict):
  if word1 not in words_dict or word2 not in words_dict:
    return -1
  if word1 == word2:
    return same_word_distance(words_dict[word1])
  else:
    return diff_word_distance(words_dict[word1], words_dict[word2])
  
def same_word_distance(indices):
  if len(indices) == 1:
    return -1
  diff = sys.maxsize
  for i in range(1, len(indices)):
    curr_diff = indices[i] - indices[i-1]
    if curr_diff < diff:
      diff = curr_diff
      if diff == 1:
        break
  return diff
  
def diff_word_distance(indices1, indices2):
  i1, i2, diff = 0, 0, sys.maxsize
  while diff != 0 and i1 < len(indices1) and i2 < len(indices2):
    curr_diff = indices2[i2] - indices1[i1]
    if abs(curr_diff) < diff:
      diff = abs(curr_diff) 
      if diff == 1: break
    if curr_diff > 0:
      i1 += 1
    else:
      i2 += 1
  return diff

def test():
  indices = [1]
  print('PASS' if same_word_distance(indices) == -1 else 'PASS')
  
  indices = [1,2]
  print('PASS' if same_word_distance(indices) == 1 else 'PASS')
  
  indices = [1,3,5,7,9,10]
  print('PASS' if same_word_distance(indices) == 1 else 'PASS')
  
  indices1 = [2]
  indices2 = [0]
  print('PASS' if diff_word_distance(indices1, indices2) == 2 else 'PASS')
  print('PASS' if diff_word_distance(indices2, indices1) == 2 else 'PASS')
  
  indices1 = [2,8,9,15,20,23]
  indices2 = [0,5,11,13,14]
  print('PASS' if diff_word_distance(indices1, indices2) == 1 else 'PASS')
  print('PASS' if diff_word_distance(indices2, indices1) == 1 else 'PASS')
  
  
  words = ['random', 'paul', 'li', 'jess', 'that', 'I', 'do', 'too', 'her', 'herb', 'brother', 'other', 'looked', 'just', 'like', 'her', 'herb', 'brother', 'other']
  words_dict = group_words(words)
  
  print('PASS' if word_distance('paul', 'paul', words_dict) == -1 else 'FAIL')
  print('PASS' if word_distance('brother', 'brother', words_dict) == 7 else 'FAIL')
  print('PASS' if word_distance('other', 'brother', words_dict) == 1 else 'FAIL')
  print('PASS' if word_distance('her', 'brother', words_dict) == 2 else 'FAIL')
  print('PASS' if word_distance('paul', 'herb', words_dict) == 8 else 'FAIL')
  print('PASS' if word_distance('herb', 'just', words_dict) == 3 else 'FAIL')

if __name__ == '__main__':
  test()
