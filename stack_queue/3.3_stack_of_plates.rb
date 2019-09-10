require '../3_stack'

class NestedStack
  LIMIT = 2
  def initialize
    @nested_stack = []
  end

  def push(data)
    if @nested_stack.empty? || @nested_stack[-1].length == LIMIT
      @nested_stack.push(Stack.new)
    end
    @nested_stack[-1].push(data)
  end

  def pop
    raise 'empty stack' if @nested_stack.length == 0
    data_to_pop = @nested_stack[-1].pop
    @nested_stack.pop if @nested_stack[-1].is_empty?
    return data_to_pop
  end

  def pop_at(index)
    raise 'empty stack' if @nested_stack.length == 0
    raise 'invalid index' if @nested_stack.length < index + 1

    data_to_pop = @nested_stack[index].pop
    @nested_stack.slice!(index) if @nested_stack[index].is_empty?
    return data_to_pop
  end

  def is_empty?
    return @nested_stack.length == 0
  end

  def peek
    raise 'empty stack' if @nested_stack.length == 0
    return @nested_stack[-1].peek
  end
end    
