def sorted_merge(A, B):
  insert_i = len(A)-1
  i_a, i_b = find_end_index(A), len(B)-1
  
  while i_b >= 0:
    if i_a is None or B[i_b] >= A[i_a]:
      A[insert_i] = B[i_b]
      i_b -= 1
    else:
      A[insert_i] = A[i_a]
      i_a = None if i_a == 0 else i_a-1
    insert_i -= 1
  return

def find_end_index(A):
  for i in range(len(A)):
    if A[i] is None:
      return None if i == 0 else i-1
  return None

def test():
  A = []
  B = []
  sorted_merge(A,B)
  print('PASS' if A == [] else 'FAIL')
  
  A = [2,3]
  B = []
  sorted_merge(A,B)
  print('PASS' if A == [2,3] else 'FAIL')
  
  A = [None,None,None]
  B = [1,2,3]
  sorted_merge(A,B)
  print('PASS' if A == [1,2,3] else 'FAIL')
  
  A = [4,7,9,None,None,None]
  B = [7,9,10]
  sorted_merge(A,B)
  print('PASS' if A == [4,7,7,9,9,10] else 'FAIL')
  
  A = [7,9,10,None,None,None]
  B = [4,5,15]
  sorted_merge(A,B)
  print('PASS' if A == [4,5,7,9,10,15] else 'FAIL')
  
  A = [3,4,7,9,None,None]
  B = [1,2]
  sorted_merge(A,B)
  print('PASS' if A == [1,2,3,4,7,9] else 'FAIL')
  
  A = [1,2,3,None,None]
  B = [7,9]
  sorted_merge(A,B)
  print('PASS' if A == [1,2,3,7,9] else 'FAIL')

if __name__ == '__main__':
    test()
