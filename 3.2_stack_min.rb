require './3_stack'

class MinStack
  class StackNode
    attr_reader :data, :next_node

    def initialize(data, next_node=nil)
      @data = data
      @next_node = next_node
    end
  end

  def initialize
    @top = nil
    @min_stack = Stack.new
  end

  def push(item)
    new_node = StackNode.new(item, @top)
    @min_stack.push(item) if @min_stack.is_empty? || @min_stack.peek >= item
    @top = new_node
  end

  def pop
    raise 'empty stack' if @top.nil?
    data_to_pop = @top.data
    @top = @top.next_node
    @min_stack.pop if data_to_pop == @min_stack.peek
    return data_to_pop
  end

  def min
    raise 'empty stack' if @top.nil?
    return @min_stack.peek
  end
end

