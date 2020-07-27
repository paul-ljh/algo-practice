'''
On old cell phones, users typed on a numeric keyboard and the phone would provide a list of words that matched these numbers. Each digit is mapped to a set of 0-4 digits. Implement an algorithm to return a list of matching words, given a sequence of digits and a list of valid words.

The keyboard is shown below:
0: None
1: None
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz
'''

from utils_python.trie.trie import Trie
from utils_python.trie.trie_node import TrieNode

def t9(seq, valid_words, keyboard):
  trie_words = Trie()
  for word in valid_words:
    if not word: # empty string
      trie_words.root.children[word] = TrieNode()
    else:
      trie_words.insert(word)

  result = []
  generate_valid_words(seq, trie_words.root, result, keyboard, 0, [])
  return result

def generate_valid_words(seq, trie_words, result, keyboard, index, sofar):
  if index == len(seq):
    final_word = ''.join(sofar)
    if final_word or final_word in trie_words.children:
      result.append(final_word)
      return
  
  curr_digit = seq[index]
  if curr_digit in keyboard:
    if keyboard[curr_digit] == None:
      return generate_valid_words(seq, trie_words, result, keyboard, index+1, sofar)
    else:
      for letter in keyboard[curr_digit]:
        if letter in trie_words.children:
          generate_valid_words(seq, trie_words.children[letter],
                               result, keyboard,
                               index+1, sofar + [letter])
  return

def test():
  valid_words = ['', 'apple', 'app', 'cat', 'dog', 'csr']
  keyboard = {
    '0': None,
    '1': None,
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
  }
  
  seq = '010101'
  answer = ['']
  print ('PASS' if t9(seq, valid_words, keyboard) == answer else 'FAIL')
  
  seq = '21707531'
  answer = ['apple']
  print ('PASS' if t9(seq, valid_words, keyboard) == answer else 'FAIL')
  
  seq = '277'
  answer = ['app', 'csr']
  print ('PASS' if t9(seq, valid_words, keyboard) == answer else 'FAIL')
  
if __name__ == "__main__":
  test()
  
  
