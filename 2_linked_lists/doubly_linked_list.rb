class Node
  attr_accessor :data, :key, :next_node, :prev_node

  def initialize(data, key = nil, next_node = nil, prev_node = nil)
    @data = data
    @key = key
    @next_node = next_node
    @prev_node = prev_node
  end
end

class DoublyLinkedList
  attr_accessor :length, :head, :tail

  def initialize
    @length = 0
    @head, @tail = nil, nil
  end

  def pop
    raise "empty list" if @length.zero?
    return_node = @tail
    if @length == 1
      @tail, @head = nil, nil
    else
      @tail.prev_node.next_node = nil
      @tail = @tail.prev_node
    end
    @length -= 1
    return return_node
  end

  def add(data:, key: nil)
    new_node = Node.new(data, key)
    if @head.nil?
      @head = @tail = new_node
    else
      if @length == 1
        new_node.next_node = @tail
        @tail.prev_node = new_node
      end
      new_node.next_node = @head
      @head.prev_node = new_node
      @head = new_node
    end
    @length += 1
    return new_node
  end

  def delete(node)
    raise "empty list" if @length.zero?
    h = @head
    while h != node do
      h = h.next_node
      raise "couldn't find #{node.data}" if h.nil?
    end
    return_node = h
    if h == @tail
      pop
    elsif h == @head
      @head.next_node.prev_node = nil
      @head = @head.next_node
      @length -= 1
    else
      h.next_node.prev_node = h.prev_node
      h.prev_node.next_node = h.next_node
      @length -= 1
    end
    return return_node
  end

  def print
    forward, backward = "", ""
    h = @head
    while !h.nil? do
      forward << "#{h.data}->"
      backward << "#{h.data}<-"
      h = h.next_node
    end
    forward << "nil" << "\n" 
    backward << "nil" << "\n"
    return "\n" + forward + backward
  end
end

def test
  l = DoublyLinkedList.new
  puts "INIT: #{l.print}"
  puts

  l.add(data: 1)
  l.add(data: 2)
  l.add(data: 3)
  l.add(data: 4)
  puts "ADDED 1, 2, 3, 4: #{l.print}"
  puts

  begin
    l.delete(Node.new(5))
  rescue
    puts 'ERROR from deleting node with data 5'
    puts
  end
  l.delete(l.head.next_node)
  puts "DELETED Node 3: #{l.print}"
  puts

  l.delete(l.tail)
  puts "DELETED Node 1: #{l.print}"
  puts

  l.delete(l.head)
  puts "DELETED Node 4: #{l.print}"
  puts

  l.delete(l.head)
  puts "DELETED Node 2: #{l.print}"
  puts

  l.add(data: 1)
  l.add(data: 2)
  puts "ADDED 1, 2: #{l.print}"
  puts

  l.pop
  puts "POPED 1: #{l.print}"
  puts

  l.pop
  puts "POPED 2: #{l.print}"
  puts

  begin
    l.pop
  rescue
    puts 'ERROR from POPING an empty list'
  end
end

