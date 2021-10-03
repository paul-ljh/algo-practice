'''
You are given two arrays, one shorter (with all distinct elements) and one longer. Find the shortest subarray in the longer array that contains all the elements in the shorter array. The items can appear in any order.

EX:
shorter: [1,5,9]
longer: [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
answer: [7,10]
'''

from queue import Queue
from sys import maxsize

def shortest_supersequence(shorter, longer):
  short_set = set(shorter)
  occur_dict = {}
  index_queue = Queue()
  best_distance, best_result = maxsize, None
  
  for i in range(len(longer)):
    elem = longer[i]
    if elem in short_set:
      occur_dict[elem] = occur_dict.get(elem, 0) + 1
      index_queue.put(i)
      while len(occur_dict) == len(short_set):
        earliest_index = index_queue.get()
        curr_distance = i - earliest_index
        
        earliest_elem = longer[earliest_index]
        occur_dict[earliest_elem] -= 1
        if occur_dict[earliest_elem] == 0:
          occur_dict.pop(earliest_elem)

        if curr_distance < best_distance:
          best_distance, best_result = curr_distance, (earliest_index, i)
          if best_distance + 1 == len(short_set):
            break
  return best_result

def test():
  shorter = []
  longer = [2,3,4]
  answer = None
  print('PASS' if shortest_supersequence(shorter, longer) == answer else 'FAIL')
  
  shorter = []
  longer = []
  answer = None
  print('PASS' if shortest_supersequence(shorter, longer) == answer else 'FAIL')
  
  shorter = [4]
  longer = [2,3,4]
  answer = (2,2)
  print('PASS' if shortest_supersequence(shorter, longer) == answer else 'FAIL')
  
  shorter = [1,5,9]
  longer = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
  answer = (7,10)
  print('PASS' if shortest_supersequence(shorter, longer) == answer else 'FAIL')
  
  shorter = [1,5,9]
  longer = [7,5,9,2,2,1,3,1,5,3,9,7,1,7,5,9,1,9,7]
  answer = (14,16)
  print('PASS' if shortest_supersequence(shorter, longer) == answer else 'FAIL')

if __name__ == "__main__":
  test()
