'''
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
substring.
'''

def longest_valid_parentheses(s):
  stack = []
  max_so_far = 0
  start_index = -1

  for i in range(len(s)):
    curr_char = s[i]
    if curr_char == '(':
      stack.append(i)
    elif len(stack) == 0:
      start_index = i
    else:
      stack.pop()
      d = i - (start_index if len(stack) == 0 else stack[-1])
      max_so_far = max(max_so_far, d)
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
