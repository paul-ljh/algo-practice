'''
Find all permutations of a string.
'''

'''
Runtime: O(n^2 * n!)
Space: O(n)
'''
def permutation(str):
  find_permutation('', str)

def find_permutation(prefix, rem):
  if (len(rem) == 0):
    print(prefix)
    return

  for i in range(len(rem)):
    new_rem = rem[:i] + rem[i+1:]
    find_permutation(prefix + rem[i], new_rem)

def test():
  permutation('abcd')

if __name__ == "__main__":
  test()
