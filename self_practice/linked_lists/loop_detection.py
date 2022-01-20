import sys
sys.path.append('../../utils_python')

from linked_list import LinkedList

def loop_detection(l):
  slow, fast = l.head, l.head
  while True:
    slow = slow.next_node
    fast = fast.next_node.next_node
    if slow == fast:
      break

  final = l.head
  while final != slow:
    final, slow = final.next_node, slow.next_node

  return final
