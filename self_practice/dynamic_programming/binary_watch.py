'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

HOUR:
8 4 2 1
MINUTE:
32 16 8 4 2 1

Given an integer turned_on which represents the number of LEDs that are currently on, return all possible times the watch could represent. You can return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must be consist of two digits and must contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".

EX:
Input: turned_on = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

https://leetcode.com/problems/binary-watch/
'''

def compute_cache(result, sum_threshold, digit_threshold, curr_sum, used_digit, index):
  if curr_sum > sum_threshold:
    return

  if used_digit not in result:
    result[used_digit] = []
  result[used_digit].append(curr_sum)

  if used_digit == digit_threshold:
    return

  for i in range(index, digit_threshold):
    compute_cache(result, sum_threshold, digit_threshold, curr_sum + pow(2, index), used_digit + 1, i + 1)

  return

if __name__ == '__main__':
  result = {}
  compute_cache(result, 12, 4, 0, 0, 0)
  print(result)
