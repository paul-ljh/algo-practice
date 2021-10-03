'''
Given a pair of strings X of length M and Y of length N.

A common subsequence between X and Y is, suppose it is a string called Z of length K, such that Z[k] = X[ik] = Y[jk] where k is [0, K], ik is [0, N], jk is [0, M].

Find the length of the longest common subsequence of X and Y.
'''

def longest_common_subsequence(s1, s2):
  cache = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]
  best_sofar = 0
  for r in range(len(s2)):
    for c in range(len(s1)):
      cache[r+1][c+1] = max(cache[r][c+1],
                            cache[r+1][c],
                            cache[r][c]+1 if s1[c] == s2[r] else -1)
      best_sofar = max(cache[r+1][c+1], best_sofar)
  return best_sofar

def test():
  s1, s2 = "", ""
  answer = 0
  print('PASS' if longest_common_subsequence(s1, s2) == answer else 'FAIL')
  
  s1, s2 = "abs", ""
  answer = 0
  print('PASS' if longest_common_subsequence(s1, s2) == answer else 'FAIL')
  
  s1, s2 = "polynomial", "exponential"
  answer = 6
  print('PASS' if longest_common_subsequence(s1, s2) == answer else 'FAIL')
  
  s1, s2 = "longest", "long"
  answer = 4
  print('PASS' if longest_common_subsequence(s1, s2) == answer else 'FAIL')
  
  s1, s2 = "long", "long"
  answer = 4
  print('PASS' if longest_common_subsequence(s1, s2) == answer else 'FAIL')
  
if __name__ == "__main__":
  test()
      