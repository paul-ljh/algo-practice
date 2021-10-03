from sys import maxsize

'''
The idea is based on the following:
1. If seq[i] is smallest among all end candidates of active lists, we will start new active list of length 1.
2. If seq[i] is largest among all end candidates of active lists, we will clone the largest active list, and extend it by seq[i].
3. If seq[i] is in between, we will find a list with largest end element that is smaller than seq[i]. Clone and extend this list by seq[i]. We will discard all other lists of same length as that of this modified list.

Note that at any instance during our construction of active lists, the following condition is maintained.

end element of smaller list is smaller than end elements of larger lists.
'''

def longest_increasing_sequence(seq):
  length_list = [[]]
  for num in seq:
    best_index = find_best_lineup(length_list, num)
    curr_index = best_index + 1
    if curr_index > len(length_list)-1:
      length_list.append([])
    length_list[curr_index] = length_list[best_index] + [num]
  return length_list[-1]

def find_best_lineup(length_list, num):
  left, right, best = 0, len(length_list)-1, 0
  while right >= left:
    mid = (left+right) // 2
    pivot = length_list[mid][-1] if length_list[mid] else -maxsize-1
    if pivot > num:
      right = mid - 1
    else:
      left = mid + 1
      best = mid
  return best

def test():
  seq = []
  print('PASS' if longest_increasing_sequence(seq) == [] else 'FAIL')
  
  seq = [1]
  print('PASS' if longest_increasing_sequence(seq) == [1] else 'FAIL')
  
  seq = [1,2]
  print('PASS' if longest_increasing_sequence(seq) == [1,2] else 'FAIL')
  
  seq = [1,0]
  print('PASS' if longest_increasing_sequence(seq) == [0] else 'FAIL')
  
  seq = [1,4,3]
  print('PASS' if longest_increasing_sequence(seq) == [1,3] else 'FAIL')
  
  seq = [1,3,2,0,9,6,10,12,4]
  print('PASS' if longest_increasing_sequence(seq) == [1,2,6,10,12] else 'FAIL')

if __name__ == '__main__':
    test()
    
  