class Node
  attr_accessor :data, :next_node

  def initialize(data, next_node=nil)
    @data = data
    @next_node = next_node
  end
end

class LinkedList
  attr_accessor :head, :length

  def initialize(data=nil)
    if data.nil? 
      @head = nil
      @length = 0
    else
      @head = Node.new(data)
      @length = 1
    end
  end

  def append_to_tail(data)
    new_node = Node.new(data)
    if @head.nil?
      @head = new_node
      @length += 1
      return
    end

    n = @head
    while !n.next_node.nil?
      n = n.next_node
    end
    n.next_node = new_node
    @length += 1
  end

  def delete_node(data)
    n = @head
    if n.data == data
      @head = n.next_node
      @length -= 1
      return data
    end

    while !n.next_node.nil?
      if n.next_node.data == data
        n.next_node = n.next_node.next_node
        @length -= 1
        return data
      end
      n = n.next_node
    end
  end

  def print_list
    h = @head
    while !h.nil? do
      print "#{h.data}->"
      h = h.next_node
    end
    puts "nil"
  end
end

def test
  l1 = LinkedList.new()
  l1.append_to_tail(5)
  puts "L1 Head is 5? #{l1.head.data == 5 ? "Pass" : "Fail"}"
  l1.print_list()

  l1.append_to_tail(4)
  l1.append_to_tail(3)
  l1.append_to_tail(4)
  puts "L1 Head is 5? #{l1.head.data == 5 ? "Pass" : "Fail"}"
  puts "L1 length is 4? #{l1.length == 4 ? "Pass" : "Fail"}"
  l1.print_list()

  l1.delete_node(2)
  puts "L1 length is 4? #{l1.length == 4 ? "Pass" : "Fail"}"
  l1.print_list()

  l1.delete_node(5)
  puts "L1 Head is 4? #{l1.head.data == 4 ? "Pass" : "Fail"}"
  l1.print_list()

  l1.delete_node(3)
  puts "L1 Head is 4? #{l1.head.data == 4 ? "Pass" : "Fail"}"
  puts "L1 length is 2? #{l1.length == 2 ? "Pass" : "Fail"}"
  l1.print_list()

  l1.delete_node(4)
  puts "L1 Head is 4? #{l1.head.data == 4 ? "Pass" : "Fail"}"
  l1.print_list()

  l1.delete_node(4)
  puts "L1 Head is nil? #{l1.head.nil? ? "Pass" : "Fail"}"
  puts "L1 length is 0? #{l1.length == 0 ? "Pass" : "Fail"}"
  l1.print_list()
end
