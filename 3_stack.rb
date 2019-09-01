require './stack_node'

class Stack
  attr_reader :length

  def initialize
    @top = nil
    @length = 0
  end

  def push(data)
    new_top = StackNode.new(data, @top)
    new_top.next = @top
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
end


