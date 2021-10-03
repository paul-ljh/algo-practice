'''
Given an array filled with letters and numbers, find the longest subarray with an equal number of letters and numbers.
'''

def letters_and_numbers(arr):
  diff_dict = {}
  ltr_num_diff = 0
  best_start_i = best_len = 0
  for i in range(len(arr)):
    elem = arr[i]
    ltr_num_diff += (1 if isinstance(elem, str) else -1)
    if ltr_num_diff == 0:
      best_start_i, best_len = 0, i+1
    else:
      if ltr_num_diff in diff_dict:
        curr_len = i - diff_dict[ltr_num_diff]
        if curr_len > best_len:
          best_start_i, best_len = diff_dict[ltr_num_diff]+1, curr_len
      else:
        diff_dict[ltr_num_diff] = i
  return (best_start_i, best_start_i+best_len)

def test():
  arr = []
  answer = (0,0)
  print('PASS' if letters_and_numbers(arr) == answer else 'FAIL')
  
  arr = ['a']
  answer = (0,0)
  print('PASS' if letters_and_numbers(arr) == answer else 'FAIL')
  
  arr = [1,2,3,4]
  answer = (0,0)
  print('PASS' if letters_and_numbers(arr) == answer else 'FAIL')
  
  arr = [0, 'a', 0, 'a', 0, 'a']
  answer = (0,6)
  print('PASS' if letters_and_numbers(arr) == answer else 'FAIL')
  
  arr = [0,0,0,0,0, 'a', 0, 'a', 0, 'a']
  answer = (4,10)
  print('PASS' if letters_and_numbers(arr) == answer else 'FAIL')
  
  arr = [0,0,0,0,0,'a', 'a', 'a']
  answer = (2,8)
  print('PASS' if letters_and_numbers(arr) == answer else 'FAIL')
  
  arr = [0,0,0,0,0,'a', 'a', 'a', 0, 'a', 'a', 'a']
  answer = (0,12)
  print('PASS' if letters_and_numbers(arr) == answer else 'FAIL')

if __name__ == "__main__":
  test()
