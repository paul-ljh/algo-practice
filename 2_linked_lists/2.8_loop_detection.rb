load 'linked_list.rb'

def loop_detection(l)
  return nil if l.head.nil?
  slow, fast, head = l.head, l.head, l.head
  loop do
    slow, fast = slow.next_node, fast.next_node.next_node
    break if slow == fast
  end

  while slow != head do
    slow, head = slow.next_node, head.next_node
  end
  return head.data
end

def test
  l = LinkedList.new([1, 2, 3, 4])
  l.tail.next_node = l.head
  puts "l has a loop starting at #{loop_detection(l)}"

  l = LinkedList.new([1, 2, 3, 4])
  l.tail.next_node = l.head.next_node
  puts "l has a loop starting at #{loop_detection(l)}"

  l = LinkedList.new([1, 2, 3, 4])
  l.tail.next_node = l.head.next_node.next_node
  puts "l has a loop starting at #{loop_detection(l)}"
end

