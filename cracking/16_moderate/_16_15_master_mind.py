'''
The Game of Master Mind is played as follows:

The computer has 4 slots, and each slot will contain a ball that is red(R), yellow(Y), green(G) or blue(B). For example, the computer might have RGGB.

You, the user are trying to guess the solution. You might for example guess YRGB.

When you guess the correct color for the correct slot, you get a hit. If you guess a color that exists but is in the wrong slot, you get a "pseudo-hit". Note that a slot that is a hit can never count as a pseudo-hit.

For example, if the actualy solution is RGBY and you guess GGRR, you have 1 hit and 1 pseudo-hit.

Write a method that given a guess and a solution in string format, returns the number of hits and pseudo-hits.
'''

def master_mind(str1, str2):
  ltr_occur = {}
  hits = 0
  length = len(str1)
  for i in range(length):
    char1, char2 = str1[i], str2[i]
    if char1 == char2:
      hits += 1
    else:
      ltr_occur[char1] = ltr_occur.get(char1, 0) + 1
      ltr_occur[char2] = ltr_occur.get(char2, 0) - 1
  
  pseudo_hits = (length * 2 - hits * 2 - sum(list(map(abs, ltr_occur.values())))) // 2
  return (hits, pseudo_hits)

def test():
  solution, guess = 'YYYY', 'YYYY'
  answer = (4,0)
  print('PASS' if master_mind(solution, guess) == answer else 'FAIL')
  
  solution, guess = 'RYGB', 'YGBR'
  answer = (0,4)
  print('PASS' if master_mind(solution, guess) == answer else 'FAIL')
  
  solution, guess = 'RGBY', 'GGRR'
  answer = (1,1)
  print('PASS' if master_mind(solution, guess) == answer else 'FAIL')
  
  solution, guess = 'YYGG', 'GGYY'
  answer = (0,4)
  print('PASS' if master_mind(solution, guess) == answer else 'FAIL')
  
  solution, guess = 'YYYG', 'GGYY'
  answer = (1,2)
  print('PASS' if master_mind(solution, guess) == answer else 'FAIL')
  
if __name__ == "__main__":
  test()
