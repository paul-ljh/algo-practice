load "#{Dir.home}/Documents/Interviews/algo-practice/uni_node.rb"

class Stack
  attr_reader :length

  def initialize
    @top = nil
    @length = 0
  end

  def push(data)
    new_top = UniNode.new(data, @top)
    new_top.next_node = @top
    @top = new_top
    @length += 1
  end

  def pop
    raise "no item in the stack" if @top.nil?
    data_to_pop = @top.data
    @top = @top.next_node
    @length -= 1
    return data_to_pop
  end

  def is_empty?
    return @top.nil?
  end

  def peek
    raise "no item in the stack" if @top.nil?
    return @top.data
  end

  def inspect
    msg = ''
    node = @top
    while !node.nil? do
      msg << "#{node.data}" << "->"
      node = node.next_node
    end
    msg << "nil"
    msg
  end
end

def test
  s = Stack.new
  begin
    puts "PEEK empty stack"
    s.peek
  rescue StandardError => e
    puts e.message
    puts
  end

  begin
    puts "POP empty stack"
    s.pop
  rescue StandardError => e
    puts e.message
    puts
  end

  puts "ADD 3, 5, 6"
  s.push(3)
  s.push(5)
  s.push(6)
  puts s.length == 3 ? 'PASS' : 'FAIL'
  puts s.inspect
  puts

  puts "POP and PEEK"
  puts s.pop == 6 ? 'PASS' : 'FAIL'
  puts s.peek == 5 ? 'PASS' : 'FAIL'
  puts s.length == 2 ? 'PASS' : 'FAIL'
  puts s.inspect
  puts
end
