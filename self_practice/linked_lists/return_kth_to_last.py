import sys
sys.path.append('../../utils_python')

from linked_list import LinkedList

def return_kth_to_last(l, k):
  if k < 0:
    raise IndexError('k cannot be negative')

  first, second = l.head, l.head
  for i in range(k):
    if second == None:
      raise IndexError('k cannot be larger than the length of the linked list')
    second = second.next_node

  while second != None:
    first, second = first.next_node, second.next_node

  return first.data

def test():
  l = LinkedList()
  l.add(0,1)
  l.add(0,2)
  l.add(0,3)
  l.add(0,4)

  try:
    return_kth_to_last(l, 5)
  except IndexError as e:
    print(e)

  print('PASS' if return_kth_to_last(l, 3) == 3 else 'FAIL')

if __name__ == '__main__':
  test()
