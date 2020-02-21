class LinkedList
  attr_accessor :head

  class Node
    attr_accessor :data, :next_node

    def initialize(data, next_node=nil)
      @data = data
      @next_node = next_node
    end
  end

  def initialize(data=nil)
    @head = data.nil? ? nil : Node.new(data)
  end

  def append_to_tail(data)
    new_node = Node.new(data)
    if @head.nil?
      @head = new_node 
      return
    end

    n = @head
    while !n.next_node.nil?
      n = n.next_node
    end
    n.next_node = new_node
  end

  def delete_node(data)
    n = @head
    if n.data == data
      @head = n.next_node
      return data
    end

    while !n.next_node.nil?
      if n.next_node.data == data
        n.next_node = n.next_node.next_node
        return data
      end
      n = n.next_node
    end
  end
end

def test
  l1 = LinkedList.new()
  l1.append_to_tail(5)
  puts "L1 Head is 5? #{l1.head.data == 5 ? "Pass" : "Fail"}"

  l1.append_to_tail(4)
  l1.append_to_tail(3)
  l1.append_to_tail(4)
  puts "L1 Head is 5? #{l1.head.data == 5 ? "Pass" : "Fail"}"

  l1.delete_node(5)
  puts "L1 Head is 4? #{l1.head.data == 4 ? "Pass" : "Fail"}"
  l1.delete_node(3)
  puts "L1 Head is 4? #{l1.head.data == 4 ? "Pass" : "Fail"}"
  l1.delete_node(4)
  puts "L1 Head is 4? #{l1.head.data == 4 ? "Pass" : "Fail"}"
  l1.delete_node(4)
  puts "L1 Head is nil? #{l1.head.nil? ? "Pass" : "Fail"}"
end
