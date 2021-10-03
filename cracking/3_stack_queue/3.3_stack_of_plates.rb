load "#{Dir.home}/Documents/Interviews/algo-practice/stack.rb"

class SetOfStacks
  def initialize(limit)
    @limit = limit
    @stacks = []
  end

  def push(data)
    if @stacks.empty? || @stacks[-1].length == @limit
      @stacks.push(Stack.new)
    end
    @stacks[-1].push(data)
  end

  def pop(index=-1)
    raise 'EMPTY STACK' if @stacks.length == 0
    data_to_pop = @stacks[index].pop
    @stacks.slice!(index) if @stacks[index].is_empty?
    data_to_pop
  end

  def pop_at(index)
    raise 'INVALID INDEX' if @stacks.size <= index
    pop(index)
  end

  def is_empty?
    @stacks.length == 0
  end

  def peek(index=-1)
    raise 'EMPTY STACK' if is_empty?
    @stacks[index].peek
  end
end

def test
  s = SetOfStacks.new(2)
  begin
    s.pop_at(0)
  rescue StandardError => e
    puts e.message
    puts
  end

  begin
    s.pop
  rescue StandardError => e
    puts e.message
    puts
  end

  s.push(4)
  s.push(2)
  s.push(3)
  s.push(4)
  s.push(3)
  puts s.pop_at(1) == 4 ? 'PASS' : 'FAIL'
  puts s.pop_at(1) == 3 ? 'PASS' : 'FAIL'
  puts s.peek(1) == -2 ? 'PASS' : 'FAIL'
  puts s.pop == 3 ? 'PASS' : 'FAIL'
  puts s.pop == 2 ? 'PASS' : 'FAIL'
  puts s.pop == 4 ? 'PASS' : 'FAIL'
end

