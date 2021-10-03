load "#{Dir.home}/Documents/Interviews/algo-practice/stack.rb"

class MinStack
  def initialize
    @top = nil
    @min_stack = Stack.new
  end

  def push(item)
    new_node = UniNode.new(item, @top)
    @min_stack.push(item) if @min_stack.is_empty? || @min_stack.peek >= item
    @top = new_node
  end

  def pop
    raise 'EMPTY STACK' if @top.nil?
    data_to_pop = @top.data
    @top = @top.next_node
    @min_stack.pop if data_to_pop == @min_stack.peek
    data_to_pop
  end

  def min
    raise 'EMPTY STACK' if @top.nil?
    @min_stack.peek
  end

  def peek
    raise 'EMPTY STACK' if @top.nil?
    @top.data
  end
end

def test
  s = MinStack.new

  s.push(5)
  s.push(4)
  s.push(1)
  s.push(1)
  s.push(10)

  puts s.peek == 10 ? 'PASS' : 'FAIL'
  puts s.min == 1 ? 'PASS' : 'FAIL'
  s.pop
  puts s.min == 1 ? 'PASS' : 'FAIL'
  s.pop
  puts s.min == 1 ? 'PASS' : 'FAIL'
  s.pop
  puts s.min == 4 ? 'PASS' : 'FAIL'
  s.pop
  puts s.min == 5 ? 'PASS' : 'FAIL'

  begin
    s.pop
    s.min
  rescue StandardError => e
    puts e.message
    puts
  end
end

