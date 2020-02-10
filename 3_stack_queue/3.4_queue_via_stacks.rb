require '../3_stack'

class MyQueue
  def initialize
    @original = Stack.new
    @reverse = Stack.new
  end

  def dump(src, dst)
    while !src.is_empty? do
      dst.push(src.pop)
    end
  end

  def push(data)
    dump(@reverse, @original) if @original.is_empty? && !@reverse.is_empty?
    @original.push(data)
  end

  def pop
    dump(@original, @reverse) if !@original.is_empty? && @reverse.is_empty?
    return @reverse.pop
  end

  def peek
    dump(@reverse, @original) if @original.is_empty? && !@reverse.is_empty?
    return @original.peek
  end

  def is_empty?
    return @original.is_empty? && @reverse.is_empty?
  end
end

