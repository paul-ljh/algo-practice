'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

EX1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

EX2:
Input: height = [4,2,0,3,2,5]
Output: 9

https://leetcode.com/problems/trapping-rain-water/
'''

def trapping_rain_water(arr):
  right_max = []
  max_so_far = 0
  for i in reversed(range(1, len(arr))):
    if arr[i] > max_so_far:
      max_so_far = arr[i]
    right_max.append(max_so_far)

  result = threshold = 0
  for i in range(len(arr) - 1):
    curr_height = arr[i]
    tallest_remain = right_max.pop()
    if curr_height >= threshold:
      threshold = curr_height if tallest_remain >= curr_height else tallest_remain
    else:
      result += (threshold - curr_height)
  return result

def test():
  heights = []
  answer = 0
  print('PASS' if trapping_rain_water(heights) == answer else 'FAIL')

  heights = [4]
  answer = 0
  print('PASS' if trapping_rain_water(heights) == answer else 'FAIL')

  heights = [4,0,0,2]
  answer = 4
  print('PASS' if trapping_rain_water(heights) == answer else 'FAIL')

  heights = [4,2]
  answer = 0
  print('PASS' if trapping_rain_water(heights) == answer else 'FAIL')

  heights = [4,7]
  answer = 0
  print('PASS' if trapping_rain_water(heights) == answer else 'FAIL')

  heights = [4,1,0,7]
  answer = 7
  print('PASS' if trapping_rain_water(heights) == answer else 'FAIL')

  heights = [4,2,3,6,5,8,2,6,1,1,5]
  answer = 16
  print('PASS' if trapping_rain_water(heights) == answer else 'FAIL')

  heights = [0,0,4,0,0,6,0,0,3,0,5,0,1,0,0,0]
  answer = 26
  print('PASS' if trapping_rain_water(heights) == answer else 'FAIL')

  heights = [0,0,4,0,0,6,0,6,3,0,5,0,1,6,0,0]
  answer = 35
  print('PASS' if trapping_rain_water(heights) == answer else 'FAIL')

if __name__ == "__main__":
  test()
