'''
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
substring.
'''

def longest_valid_parentheses(str):
  stack = [-1]
  max_so_far = 0
  for i in range(len(str)):
    curr = str[i]
    if curr == '(':
      stack.append(i)
    else:
      stack.pop()
      if len(stack) == 0:
        stack.append(i)
      else:
        max_so_far = max(max_so_far, i - stack[-1])
  return max_so_far

def test():
  tests = [
    ('', 0),
    ('(', 0),
    (')', 0),
    ('()', 2),
    ('(()', 2),
    ('(()())(', 6),
    ('(()())()', 8),
    (')))()()()(', 6),
    (')))()(()()(', 4),
    ('())()()()(', 6)
  ]

  for input, output in tests:
    print('PASS' if longest_valid_parentheses(input) == output else 'FAIL')

if __name__ == '__main__':
  test()
