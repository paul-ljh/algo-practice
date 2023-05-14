'''
Given an array of distinct integers, count the number of pairs of intergers that have difference k.
For instance, given the array [1,7,5,9,2,12,3] and the difference k = 2, there are 4 pairs with difference 2: [(1,3), (7,9), (7,5), (5,3)].
'''

def find_k_difference(arr, k):
  if k == 0 or len(arr) <= 1:
    return []
  s = set(arr)
  result = []
  for pivot in arr:
    targets = [pivot + k, pivot - k]
    for target in targets:
      if target in s:
        result.append((pivot, target))
    s.remove(pivot)
  return result

def test():
  inputs = [
    ([], 2),
    ([1], 2),
    ([1,2], 0),
    ([1,7,5,9,2,12,3], 2),
  ]

  outputs = [
    [],
    [],
    [],
    [(1,3), (7,9), (7,5), (5,3)],
  ]

  for i in range(len(outputs)):
    print('PASS' if find_k_difference(*inputs[i]) == outputs[i] else 'FAIL')

if __name__ == "__main__":
  test()
