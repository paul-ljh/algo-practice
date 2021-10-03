def longest_word(words):
  d = dict(zip(words, [True] * len(words)))
  result = None
  for word in words:
    if (valid_composition(word, d, True)
      and len(word) > (len(result) if result else 0)):
      result = word
  return result

def valid_composition(word, d, original):
  if word in d and not original:
    return d[word]
  for i in range(1, len(word)):
    left = word[:i]
    if d.get(left, False) and valid_composition(word[i:], d, False):
      return True
  d[word] = original
  return False
        

def test():
  words = ['pull', 'pullpullupup', 'pullup', 'up', 'dog', 'cat', 'walker', 'dogcatwalker', 'dogwalker', 'pulluprandom']
  print('PASS' if longest_word(words) == 'pullpullupup' else 'FAIL')
  
  d = dict(zip(words, [True] * len(words)))
  for word in words:
    print(f"{word}: {valid_composition(word, d, True)}")

if __name__ == '__main__':
  test()
