'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Source: https://leetcode.com/problems/valid-parentheses/
'''

from math import log

# Runtime O(n)
# Space O(n)
def valid_parentheses(s):
  l = len(s)
  if l % 2 == 1:
    return False

  stack = []
  left_to_right_d = {'(': ')', '[': ']', '{': '}'}
  for index, char in enumerate(s):
    if char in left_to_right_d:
      if index == l-1:
        return False
      else:
        stack.append(char)
    else:
      if len(stack) == 0 or left_to_right_d[stack[-1]] != char:
        return False
      else:
        stack.pop()
  return len(stack) == 0


'''
Use an integer to emulate a stack.
From most to least significant bit, the i-th bit is
- 1 if s[i] is a left bracket and yet to be closed
- 0 otherwise

# Runtime O(n)
# Space O(1)
'''
def valid_parentheses_bit_manipulation(s):
  l = len(s)
  if l % 2 == 1:
    return False

  bit_stack = 0
  left_to_right_d = {'(': ')', '[': ']', '{': '}'}
  for index, char in enumerate(s):
    if char in left_to_right_d:
      if index == l-1:
        return False
      else:
        bit_stack |= (1 << (l - index - 1))
    else:
      if bit_stack == 0 or left_to_right_d[get_char_in_s(bit_stack, s)] != char:
        return False
      else:
        bit_stack &= (bit_stack - 1)
  return bit_stack == 0

def get_char_in_s(bit_stack, s):
  index_in_bit_stack = int(log(((bit_stack ^ (bit_stack - 1)) + 1), 2)) - 1
  index_in_s = len(s) - index_in_bit_stack - 1
  return s[index_in_s]

def test():
  test_cases = {
    '': True,
    '()[]': True,
    '([{}])': True,
    '([{]})': False,
    '[[(())': False,
    '({})[[': False,
    '({})]]': False,
  }

  for test_input, exp_result in test_cases.items():
    print('PASS' if exp_result ==
          valid_parentheses(test_input) ==
          valid_parentheses_bit_manipulation(test_input) else 'FAIL')

if __name__ == "__main__":
  test()
