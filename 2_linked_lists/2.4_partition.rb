load 'linked_list.rb'
require 'pp'

def partition(l, target)
  return l if l.head.nil?

  tail, head, prev, len = l.head, l.head, nil, l.length
  while !tail.next_node.nil? do
    tail = tail.next_node
  end
  new_tail = tail

  1.upto(len) do
    if head.data >= target
      tmp = head.data
      # Delete current node
      if prev.nil?
        l.head = head.next_node
      else
        prev.next_node = head.next_node
      end
      head = head.next_node

      # Append new node
      new_tail.next_node = Node.new(tmp)
      new_tail = new_tail.next_node
    else
      prev, head = head, head.next_node
    end
  end
  return l
end

def test
  l = LinkedList.new
  l.append_to_tail(2)
  l.append_to_tail(3)
  l.append_to_tail(4)
  partition(l, 5)
  print "Input [2->3->4, 5]: "
  l.print_list

  l1 = LinkedList.new
  l1.append_to_tail(2)
  l1.append_to_tail(3)
  l1.append_to_tail(4)
  partition(l1, 1)
  print "Input [2->3->4, 1]: "
  l1.print_list

  l2 = LinkedList.new
  l2.append_to_tail(3)
  l2.append_to_tail(6)
  l2.append_to_tail(2)
  l2.append_to_tail(7)
  l2.append_to_tail(1)
  partition(l2, 3)
  print "Input [3->6->2->7->1, 3]: "
  l2.print_list
end


