load 'linked_list.rb'
require 'pp'

# EX: 7->1->6 + 5->9->4->1 = 2->1->1->2
def sum_list_reverse(l1, l2)
  if l1.head.nil?
    return l2
  elsif l2.head.nil?
    return l1
  end

  result, carry_on = l1, 0
  l1, l2 = l1.head, l2.head
  while !l1.nil? || !l2.nil? do
    sum = (l1.nil? ? 0 : l1.data) + (l2.nil? ? 0 : l2.data) + carry_on
    l1.data, carry_on = sum % 10, sum / 10
    if l1.next_node.nil? && (!carry_on.zero? || (!l2.nil? && !l2.next_node.nil?))
      l1.next_node = Node.new(0)
    end
    l1, l2 = l1.next_node, (l2.nil? ? nil : l2.next_node)
  end
  return result
end

def test
  puts "TEST for sum_list_reverse"
  l1 = LinkedList.new([1,2,3])
  l2 = LinkedList.new([9,7,6])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_reverse(l1, l2).print_list}"

  l1 = LinkedList.new([1,2,3])
  l2 = LinkedList.new([9,7,4])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_reverse(l1, l2).print_list}"

  l1 = LinkedList.new([1,2,3,9])
  l2 = LinkedList.new([9,7,6])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_reverse(l1, l2).print_list}"

  l1 = LinkedList.new([1,2,3,7,8,9])
  l2 = LinkedList.new([9,7,6])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_reverse(l1, l2).print_list}"

  l1 = LinkedList.new([1,2,3,7])
  l2 = LinkedList.new([9,7,5])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_reverse(l1, l2).print_list}"

  l1 = LinkedList.new([1,2,3])
  l2 = LinkedList.new([9,7,6,9])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_reverse(l1, l2).print_list}"

  l1 = LinkedList.new([1,2,3])
  l2 = LinkedList.new([9,7,6,7])
  puts "#{l1.print_list} + #{l2.print_list} = #{sum_list_reverse(l1, l2).print_list}"
end
