require './stack_node'

class Queue
  attr_reader :length

  def initialize
    @first = nil
    @last = nil
    @length = 0
  end

  def push(data)
    @length += 1
    new_last = StackNode.new(data)
    @last.next_node = new_last if !@last.nil?
    @first = new_last if @first.nil?
    @last = new_last
  end

  def pop
    raise "no item in the queue" if @first.nil?
    first_to_pop = @first.data
    @first = @first.next_node
    @last = nil if @first.nil?
    @length -= 1
    return first_to_pop
  end

  def is_empty?
    return @first.nil?
  end

  def peek
    raise "no item in the queue" if @first.nil?
    return @last.data
  end    
end


