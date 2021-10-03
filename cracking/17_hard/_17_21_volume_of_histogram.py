'''
Imagine a histogram (bar graph). Given an array of bar heights as input, design an algorithm to compute the volume of water it could hold if someone poured water across the top. You can assume that each histogram bar has width 1.
'''

'''
Runtime O(N)
Space O(1)
'''
def volume_of_histogram(heights):
  if not heights:
    return 0
  tallest_index = heights.index(max(heights))
  total_volume = 0
  total_volume += caculate_volume_from_left(heights, tallest_index)
  total_volume += caculate_volume_from_right(heights, tallest_index)
  return total_volume

def caculate_volume_from_left(heights, end_index):
  if not heights:
    return 0
  total_volume = 0
  pivot_index, pivot_height = 0, heights[0]
  running_area_sum = 0
  i = 1
  while i <= end_index:
    curr_height = heights[i]
    if curr_height >= pivot_height:
      total_volume += (i - pivot_index - 1) * pivot_height - running_area_sum
      pivot_index, pivot_height = i, curr_height
      running_area_sum = 0
    else:
      running_area_sum += curr_height
    i += 1
  return total_volume

def caculate_volume_from_right(heights, end_index):
  if not heights:
    return 0
  total_volume = 0
  pivot_index, pivot_height = len(heights) - 1, heights[-1]
  running_area_sum = 0
  i = len(heights) - 2
  while i >= end_index:
    curr_height = heights[i]
    if curr_height >= pivot_height:
      total_volume += (pivot_index - i - 1) * pivot_height - running_area_sum
      pivot_index, pivot_height = i, curr_height
      running_area_sum = 0
    else:
      running_area_sum += curr_height
    i -= 1
  return total_volume

'''
Runtime O(N)
Space O(N)
'''
def volume_of_histogram_dp(heights):
  if not heights:
    return 0

  left_maxes = []
  left_max_sofar = -1
  for height in heights:
    if height > left_max_sofar:
      left_max_sofar = height
    left_maxes.append(left_max_sofar)
  
  total_volume = 0
  right_max_sofar = -1
  for i in reversed(range(1, len(heights))):
    curr_height = heights[i]
    curr_threshold = min(right_max_sofar, left_maxes[i-1])
    if curr_height < curr_threshold:
      total_volume += curr_threshold - curr_height
    else:
      right_max_sofar = max(right_max_sofar, curr_height)
  return total_volume

def test():
  heights = []
  answer = 0
  print('PASS' if volume_of_histogram(heights) == volume_of_histogram_dp(heights) == answer else 'FAIL')
  
  heights = [4]
  answer = 0
  print('PASS' if volume_of_histogram(heights) == volume_of_histogram_dp(heights) == answer else 'FAIL')
  
  heights = [4,0,0,2]
  answer = 4
  print('PASS' if volume_of_histogram(heights) == volume_of_histogram_dp(heights) == answer else 'FAIL')
  
  heights = [4,2]
  answer = 0
  print('PASS' if volume_of_histogram(heights) == volume_of_histogram_dp(heights) == answer else 'FAIL')
  
  heights = [4,7]
  answer = 0
  print('PASS' if volume_of_histogram(heights) == volume_of_histogram_dp(heights) == answer else 'FAIL')
  
  heights = [4,1,0,7]
  answer = 7
  print('PASS' if volume_of_histogram(heights) == volume_of_histogram_dp(heights) == answer else 'FAIL')
  
  heights = [4,2,3,6,5,8,2,6,1,1,5]
  answer = 16
  print('PASS' if volume_of_histogram(heights) == volume_of_histogram_dp(heights) == answer else 'FAIL')
  
  heights = [0,0,4,0,0,6,0,0,3,0,5,0,1,0,0,0]
  answer = 26
  print('PASS' if volume_of_histogram(heights) == volume_of_histogram_dp(heights) == answer else 'FAIL')
  
  heights = [0,0,4,0,0,6,0,6,3,0,5,0,1,6,0,0]
  answer = 35
  print('PASS' if volume_of_histogram(heights) == volume_of_histogram_dp(heights) == answer else 'FAIL')

if __name__ == "__main__":
  test()
  

