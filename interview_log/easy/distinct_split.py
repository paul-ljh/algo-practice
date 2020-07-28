'''
You are given a string S consisting of N lowercase English letters. A split of string S is a partition into two non-empty strings S1 and S2 such that S1 + S2 = S.

You would like to find the number of distinct letters in S1 equals the number of distinct letters in S2.

For exmaple, given S="abaca" we can split S into S1 = "ab" and S2 = "aca". The number of distinct letters in S1 and S2 is equal to 2, so the split is valid.

On the other hand, splitting into S1 = "a" and S2 = "baca" is invalid. In this split S1 has one distinct letter and S2 has three distinct letters.

Write a function that given a non-empty string S consisting of N letters, returns the number of possible splits into two parts such that the number of distince letters in each part is equal.
'''

def distinct_split(S):
  if not S:
    return 0
  d = prepopulate_dict(S)
  dis_set = set()
  counter = 0
  for letter in S:
    dis_set.add(letter)
    d[letter] -= 1
    if d[letter] == 0: d.pop(letter)
    if len(dis_set) == len(d): counter += 1
  return counter

def prepopulate_dict(S):
  dict = {}
  for letter in S:
    if letter not in dict:
      dict[letter] = 1
    else:
      dict[letter] += 1
  return dict

def test():
  print('PASS' if distinct_split("a") == 0 else 'FAIL')
  print('PASS' if distinct_split("aaaaa") == 4 else 'FAIL')
  print('PASS' if distinct_split("abaca") == 2 else 'FAIL')
  print('PASS' if distinct_split("abcdef") == 1 else 'FAIL')
  print('PASS' if distinct_split("aabbcc") == 1 else 'FAIL')

if __name__ == '__main__':
  test()
      
