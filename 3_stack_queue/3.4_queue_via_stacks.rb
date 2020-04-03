load "#{Dir.home}/Documents/Interviews/algo-practice/stack.rb"

class QueueViaStack
  def initialize
    @original = Stack.new
    @reverse = Stack.new
  end

  def dump(src, dst)
    until src.is_empty? do
      dst.push(src.pop)
    end
  end

  def push(data)
    dump(@reverse, @original) if @original.is_empty?
    @original.push(data)
  end

  def pop
    dump(@original, @reverse) if @reverse.is_empty?
    @reverse.pop
  end

  def peek
    dump(@original, @reverse) if @reverse.is_empty?
    @reverse.peek
  end

  def is_empty?
    @original.is_empty? && @reverse.is_empty?
  end
end

def test
  s = QueueViaStack.new
  begin
    s.pop
  rescue StandardError => e
    puts e.message
    puts
  end

  begin
    s.peek
  rescue StandardError => e
    puts e.message
    puts
  end

  puts s.is_empty? ? 'PASS' : 'FAIL'
  s.push(1)
  puts !s.is_empty? ? 'PASS' : 'FAIL'

  s.push(2)
  puts s.peek == 1 ? 'PASS' : 'FAIL'
  puts s.pop == 1 ? 'PASS' : 'FAIL'
  puts s.peek == 2 ? 'PASS' : 'FAIL'
  puts !s.is_empty? ? 'PASS' : 'FAIL'

  s.push(3)
  puts s.peek == 2 ? 'PASS' : 'FAIL'
  puts s.pop == 2 ? 'PASS' : 'FAIL'
  puts s.peek == 3 ? 'PASS' : 'FAIL'
  puts s.pop == 3 ? 'PASS' : 'FAIL'
  puts s.is_empty? ? 'PASS' : 'FAIL'
end

