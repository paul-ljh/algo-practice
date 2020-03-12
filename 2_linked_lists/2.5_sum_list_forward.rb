load 'linked_list.rb'
require 'pp'

# EX: 7->1->6 + 5->9->4 = 1->3->1->0
def sum_list_forward(l1, l2)
  if l1.head.nil?
    return l2
  elsif l2.head.nil?
    return l1
  end

  diff = l1.length - l2.length
  if diff > 0
    l2.head = pad_zero(l2.head, diff)
  elsif diff < 0
    l1.head = pad_zero(l1.head, diff.abs)
  end

  carry_on = sum_list_forward_helper(l1.head, l2.head)
  if !carry_on.zero?
    new_node = Node.new(carry_on)
    new_node.next_node = l1.head
    l1.head = new_node
  end
  return l1
end

# l can't be nil
def pad_zero(l, diff)
  new_node = nil
  1.upto(diff) do
    new_node = Node.new(0)
    new_node.next_node = l
    l = new_node
  end
  return new_node
end

# l1 l2 have equal length
def sum_list_forward_helper(l1, l2)
  if l1.nil? && l2.nil?
    return 0
  end
  sum = l1.data + l2.data + sum_list_forward_helper(l1.next_node, l2.next_node)
  l1.data, carry_on = sum % 10, sum / 10
  return carry_on
end

def test
  puts "TEST for sum_list_forward"
  l1 = LinkedList.new([])
  l2 = LinkedList.new([])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"

  l1 = LinkedList.new([])
  l2 = LinkedList.new([9,7,6])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"

  l1 = LinkedList.new([1,2,3])
  l2 = LinkedList.new([])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"

  l1 = LinkedList.new([1])
  l2 = LinkedList.new([9,7,6])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"

  l1 = LinkedList.new([1,2,3])
  l2 = LinkedList.new([9])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"

  l1 = LinkedList.new([1,2,3])
  l2 = LinkedList.new([9,7,7])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"

  l1 = LinkedList.new([1,2,3])
  l2 = LinkedList.new([2,7,4])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"

  l1 = LinkedList.new([2,1,0,2,2])
  l2 = LinkedList.new([9,7,6])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"

  l1 = LinkedList.new([9,9,9,0,2,4])
  l2 = LinkedList.new([9,7,6])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"

  l1 = LinkedList.new([9,7,6])
  l2 = LinkedList.new([2,1,0,2,2])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"

  l1 = LinkedList.new([9,7,6])
  l2 = LinkedList.new([9,9,9,0,2,4])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_forward(l1, l2).print_list}"
end
