def insertion_sort(arr):
  for i in range(len(arr)):
    curr = arr[i]
    for j in reversed(range(i)):
      if curr >= arr[j]:
        break;
      else:
        temp = arr[j]
        arr[j], arr[j+1] = curr, temp
  return arr

def test():
  print('PASS' if insertion_sort([]) == [] else 'FAIL')
  print('PASS' if insertion_sort([1]) == [1] else 'FAIL')
  print('PASS' if insertion_sort([5,2,4,6,1,3]) == [1,2,3,4,5,6] else 'FAIL')

if __name__ == '__main__':
  test()
