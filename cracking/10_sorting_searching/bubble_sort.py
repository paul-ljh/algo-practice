def bubble_sort(arr):
  for l in reversed(range(len(arr))):
    for i in range(l):
      if arr[i] > arr[i+1]:
        tmp = arr[i+1]
        arr[i+1], arr[i] = arr[i], tmp
  return arr

def test():
  test_data = [
    ([], []),
    ([1], [1]),
    ([2,1], [1,2]),
    ([5,4,3,2,1], [1,2,3,4,5]),
  ]

  for input, output in test_data:
    print('PASS' if bubble_sort(input) == output else 'FAIL')

if __name__ == '__main__':
  test()
