'''
A majority element is an element that makes up more than half of items in an array. Given a positive intergers array, find the majority element. 

If there is no majority element, return None. Do this in O(N) runtime and O(1) space.
'''


'''
Proof of Correctness:

Suppose array A has no majority element, no matter the index of whichever element majority_element() returns, is_majority() would guarrantee to reject it as majority element in the end.

Suppose array A has a majority element M, notice there could only be at most one majority element in any array, because it requires strictly more than half of the items in the array.

Lemma 1: 
For every prefixed subarray that the while loop in majority_element() "got rid of", neither of them has a majority element.

  PF:
  Due to the if-statement check, we cut off the subarray whenever other_count == tmp_majority_count, therefore there cannot be a majority element present.


Lemma 2:
Due to Lemma 1, after any step of slicing, the remaining portion of the array will always preserve M's majority element status.

  PF by contrdiction:
  Suppose after i-th step of slicing which cuts off arr[0] to arr[m], M is not the majority element of the remaining portion of the array.
  Because we have only been slicing out majority-element-less subarrays, M is definitely not the majority element of arr[0:m], moreover it is not the majority element of the remaining either. Thus M cannot be the majority element of the entire array. Contradiction reached.
  

Lemma 3:
Due to Lemma 2, at some time, the remaining portion of A will start with M and all its possible prefixed subarrays have M as its majority element.

  PF by contrdiction:
  Suppose there is none of such suffixed subarrays (remaining portion), meaning the algorithm will dissect the entire array into segments which have no majority element whatsoever.
  Thus the entire array mustn't have a majority element, moreever M cannot be the majority element of the entire array. Contradiction reached.
  
Due to all three lemma, we know majority_element() must locate the majority element of array A, and is_majority() will find it.
'''

def majority_element(arr):
  tmp_majority_index, tmp_majority_count = 0, 1
  other_count = 0
  i = 1
  
  while i < len(arr):
    if arr[i] == arr[tmp_majority_index]:
      tmp_majority_count += 1
    else:
      other_count += 1
      if other_count == tmp_majority_count:
        tmp_majority_index = i+1
        tmp_majority_count = other_count = 0
    i += 1
  return arr[tmp_majority_index] if is_majority(tmp_majority_index, arr) else None

def is_majority(majority_index, arr):
  if majority_index >= len(arr):
    return False
  majority = arr[majority_index]
  count = 0
  for elem in arr:
    count += 1 if elem == majority else 0
  return count >= len(arr) // 2 + 1

def test():
  arr = []
  answer = None
  print('PASS' if majority_element(arr) == answer else 'FAIL')
  
  arr = [1,1,2,2]
  answer = None
  print('PASS' if majority_element(arr) == answer else 'FAIL')
  
  arr = [1,2,3,4,5,6,7]
  answer = None
  print('PASS' if majority_element(arr) == answer else 'FAIL')
  
  arr = [1,2]
  answer = None
  print('PASS' if majority_element(arr) == answer else 'FAIL')
  
  arr = [1]
  answer = 1
  print('PASS' if majority_element(arr) == answer else 'FAIL')
  
  arr = [2,2,2]
  answer = 2
  print('PASS' if majority_element(arr) == answer else 'FAIL')
  
  arr = [3,1,7,1,1,7,7,3,7,7,7]
  answer = 7
  print('PASS' if majority_element(arr) == answer else 'FAIL')

if __name__ == "__main__":
  test()
  
