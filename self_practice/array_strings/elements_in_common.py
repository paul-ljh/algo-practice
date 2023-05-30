'''
Given 2 sorted arrays, find the number of elements in common. The arrays are of the same length and each has all distinct elements.
'''

'''
O(N) runtime, where N is the length of a or b
'''

def elements_in_common(a, b):
  i = j = 0
  result = 0
  while i < len(a) and j < len(b):
    if a[i] == b[j]:
      result += 1
      i += 1
      j += 1
    elif a[i] > b[j]:
      j += 1
    else:
      i += 1
  return result

def test():
  inputs = [
    ([1], [2]),
    ([1,1], [1,1]),
    ([1,4,7,9,11,13,15,16], [1,5,7,11,12,13,14,15]),
  ]

  outputs = [
    0,
    2,
    5,
  ]

  for i in range(len(inputs)):
    print('PASS' if elements_in_common(*inputs[i]) == outputs[i] else 'FAIL')

if __name__ == "__main__":
  test()
