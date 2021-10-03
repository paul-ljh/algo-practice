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

def t9(seq, valid_words, keyboard):
  char_to_digit = convert_keyboard(keyboard)
  digits_to_words = convert_words_to_digits(valid_words, char_to_digit)
  skimmed_seq = skim_0_1(seq)
  return digits_to_words[skimmed_seq]

def convert_keyboard(keyboard):
  char_to_digit = {}
  for digit, ltrs in keyboard.items():
    if ltrs:
      for letter in ltrs:
        char_to_digit[letter] = digit
  return char_to_digit

def convert_words_to_digits(valid_words, char_to_digit):
  digits_to_words = {}
  for word in valid_words:
    digits = convert_word(word, char_to_digit)
    if digits not in digits_to_words:
      digits_to_words[digits] = []  
    digits_to_words[digits].append(word)
  return digits_to_words

def convert_word(word, char_to_digit):
  digits = []
  for char in word:
    if char in char_to_digit:
      digits.append(char_to_digit[char])
  return ''.join(digits)

def skim_0_1(seq):
  skimmed_seq = []
  for ltr in seq:
    if ltr != '1' and ltr != '0':
      skimmed_seq.append(ltr)
  return ''.join(skimmed_seq)

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
  
  
