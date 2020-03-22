load "#{Dir.home}/Documents/Interviews/algo-practice/uni_node.rb"

class LinkedList
  attr_accessor :head, :tail
  attr_reader :length

  def initialize(data=nil)
    if data.nil? 
      @head = @tail = nil
      @length = 0
    elsif data.is_a?(Numeric)
      @head = Node.new(data)
      @tail = @head
      @length = 1
    elsif data.is_a?(Array)
      initialize_from_array(data)
      @length = data.length
    end
  end

  def initialize_from_array(data)
    h = nil
    for element in data do
      if h.nil?
        h = Node.new(element)
        @head = h
      else
        h.next_node = Node.new(element)
        h = h.next_node
      end
    end
    @tail = h
  end

  def append_to_tail(data)
    puts "Append #{data} to tail"
    new_node = Node.new(data)
    if @head.nil?
      @head = new_node
    else
      @tail.next_node = new_node
    end
    @tail = new_node
    @length += 1
  end

  def delete_node(data)
    puts "Delete #{data}"
    raise 'List is empty' if @head.nil?
    if @head.data == data
      @tail = nil if @head == @tail
      @head = @head.next_node
      @length -= 1
      return data
    end
      
    n = @head
    while !n.next_node.nil?
      if n.next_node.data == data
        n.next_node = n.next_node.next_node
        @tail = n if n.next_node.nil?
        @length -= 1
        return data
      end
      n = n.next_node
    end
  end

  def print_list
    print_msg = ''
    h = @head
    while !h.nil? do
      print_msg << "#{h.data}->"
      h = h.next_node
    end
    print_msg << "nil"
    return print_msg
  end
end

def test
  l1 = LinkedList.new
  l1.append_to_tail(5)
  puts "L1: #{l1.print_list}"

  l1.append_to_tail(4)
  l1.append_to_tail(3)
  l1.append_to_tail(4)
  puts "L1: #{l1.print_list}"
  puts "L1 length is 4? #{l1.length == 4 ? "Pass" : "Fail"}"
  puts
  
  l1.delete_node(4)
  puts "L1: #{l1.print_list}"
  puts "Tail is #{l1.tail.data}"
  
  l1.delete_node(4)
  puts "L1: #{l1.print_list}"
  puts "Tail is #{l1.tail.data}"

  l1.delete_node(2)
  puts "L1: #{l1.print_list}"

  l1.delete_node(5)
  puts "L1: #{l1.print_list}"
  puts "Tail is #{l1.tail.data}"

  l1.delete_node(3)
  puts "L1: #{l1.print_list}"
  puts

  puts "Print [] as #{LinkedList.new([]).print_list}"
  puts "Print [1] as #{LinkedList.new([1]).print_list}"
  puts "Print [1,2,3,4] as #{LinkedList.new([1,2,3,4]).print_list}"
end
