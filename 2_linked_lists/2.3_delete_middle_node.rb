load 'linked_list.rb'
require 'pp'

class DeleteMiddleNode
  attr_accessor :list, :middle
  
  def initialize(list)
    @list = list.head
    @middle = find_middle()
  end

  def find_middle
    slow, fast = @list, @list
    while (!fast.nil? && !fast.next_node.nil?) do
      fast = fast.next_node.next_node
      slow = slow.next_node
    end
    return slow
  end

  def delete_middle_node
    loop do
      if @middle.next_node.nil?
        @middle = nil
        return
      else
        @middle.data = @middle.next_node.data
        @middle = @middle.next_node
      end
    end
  end
end

def test
  l = LinkedList.new
  l.append_to_tail(1)
  l.append_to_tail(2)
  l.append_to_tail(3)
  l.append_to_tail(4)
  d = DeleteMiddleNode.new(l)
  puts "d Middle is 3? #{d.middle.data == 3 ? "Pass" : "Fail"}"
  d.delete_middle_node()
  pp d.list

  l1 = LinkedList.new
  l1.append_to_tail(1)
  l1.append_to_tail(2)
  l1.append_to_tail(3)
  l1.append_to_tail(4)
  l1.append_to_tail(5)
  d1 = DeleteMiddleNode.new(l1)
  puts "d1 Middle is 3? #{d1.middle.data == 3 ? "Pass" : "Fail"}"
  d1.delete_middle_node()
  pp d1.list
end

