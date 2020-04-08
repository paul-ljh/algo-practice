'''
We are given an array A consisting of N integers. In one move, we can choose any element in this array and replace it with any value.

What is the smallest possible amplitude of array A that we can achieve by performing at most three moves? The amplitude of an array is the difference between the largest and the smallest values it contains.

Write a function that given an array A of N integers, returns the smallest amplitude that can be obtained after replacing up to three elements of array A.
'''

def find_amplitude(A):
  size = len(A)
  if size in range(0, 5):
    return 0
  biggest, smallest = find_biggest_smallest_4(A)
  return min(biggest[0]-smallest[-1], biggest[-1]-smallest[0], biggest[1]-smallest[2], biggest[2]-smallest[1])
  
def find_biggest_smallest_4(A):
  biggest, smallest = [], []
  for i in range(0,4):
    cur_max = max(A)
    biggest.append(cur_max)
    A.remove(cur_max)

  A.extend(biggest)
  for i in range(0,4):
    cur_min = min(A)
    smallest.append(cur_min)
    A.remove(cur_min)
  return (biggest, smallest)

def test():
  print('PASS' if find_amplitude([1,2,3,4]) == 0 else 'FAIL')
  print('PASS' if find_amplitude([11,0,-6,-1,-3,5]) == 3 else 'FAIL')
  print('PASS' if find_amplitude([3,-1,4,5,11,-1]) == 2 else 'FAIL')
  print('PASS' if find_amplitude([-1,-1,4,5,11,-1]) == 0 else 'FAIL')
  print('PASS' if find_amplitude([-1,-10,9,10,11,-20]) == 2 else 'FAIL')

if __name__ == '__main__':
  test()
