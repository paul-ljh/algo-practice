require 'pp'

class ThreeInOne
  attr_reader :data
  def initialize(len)
    @data = Array.new(len, nil)
    @sizes = Array.new(3, 0)
    @bottom_indices = [0, len/3, 2*len/3]
  end

  def is_empty?(stack_num)
    @sizes[stack_num-1].zero?
  end
  
  def is_full?
    @sizes.sum >= @data.size
  end

  def top_index(stack_num)
    @bottom_indices[stack_num-1] + @sizes[stack_num-1] - 1
  end

  def bottom_index(stack_num)
    @bottom_indices[stack_num-1]
  end

  def peek(stack_num)
    raise "Stack #{stack_num} is empty!" if is_empty?(stack_num)
    @data[top_index(stack_num)]
  end

  def pop(stack_num)
    data_to_return = peek(stack_num)
    @data[top_index(stack_num)] = nil
    @sizes[stack_num-1] -= 1
    data_to_return
  end

  def add(item, stack_num)
    raise "Stack #{stack_num} is full!" if is_full?

    if (stack_num != 3 && bottom_index(stack_num+1) == top_index(stack_num) + 1) ||
      (stack_num == 3 && top_index(stack_num) == @data.size-1)
      extend(stack_num, item)
    end
    @data[top_index(stack_num)+1] = item
    @sizes[stack_num-1] += 1
    top_index(stack_num)
  end

  def extend(stack_num, item)
    indicator = how_to_extend(stack_num)
    if indicator > stack_num
      right_shift(bottom_index(stack_num+1), top_index(indicator))
      if indicator - stack_num == 2
        @bottom_indices[indicator-2] += 1
      end
      @bottom_indices[indicator-1] += 1
    else
      left_shift(bottom_index(indicator), top_index(stack_num))
      if stack_num - indicator == 1
        @bottom_indices[indicator-1] -= 1
      end
      @bottom_indices[stack_num-1] -= 1
    end
  end

  def right_shift(start, finish)
    finish.downto(start) do |i|
      @data[i+1] = @data[i]
    end
  end

  def left_shift(start, finish)
    start.upto(finish) do |i|
      @data[i-1] = @data[i]
    end
  end

  def how_to_extend(stack_num)
    case stack_num
    when 1
      top_index(stack_num+1) < bottom_index(stack_num+2)-1 ? stack_num+1 : stack_num+2
    when 2
      (bottom_index(stack_num) - top_index(stack_num-1) > @data.size - top_index(stack_num+1)) ?
        stack_num : stack_num+1
    when 3
      top_index(stack_num-1) < bottom_index(stack_num)-1 ? stack_num : stack_num-1
    end
  end
end

def test
  puts "INIT with length 7"
  t = ThreeInOne.new(7)

  t.add(3,3)
  t.add(2,2)
  puts "INSPECT ALL STACKS #{t.data == [nil, nil ,2, nil, 3, nil, nil] ? 'PASS' : 'FAIL'}"

  puts "PEEK STACK 3 #{t.peek(3) == 3 ? 'PASS' : 'FAIL'}"
  puts "PEEK STACK 2 #{t.peek(2) == 2 ? 'PASS' : 'FAIL'}"
  
  t.add(3,3)
  t.add(3,3)
  t.add(2,2)
  puts "INSPECT ALL STACKS #{t.data == [nil, nil ,2, 2, 3, 3, 3] ? 'PASS' : 'FAIL'}"
  
  begin
    t.peek(1)
  rescue StandardError => e
    puts e.message
    puts
  end

  t.add(3, 3)
  puts "INSPECT ALL STACKS #{t.data == [nil, 2, 2, 3, 3, 3, 3] ? 'PASS' : 'FAIL'}"

  t.add(2, 2)
  puts "INSPECT ALL STACKS #{t.data == [2, 2, 2, 3, 3, 3, 3] ? 'PASS' : 'FAIL'}"

  begin
    t.add(1, 1)
  rescue StandardError => e
    puts e.message
    puts
  end

  begin
    t.pop(1)
  rescue StandardError => e
    puts e.message
    puts
  end

  puts "POP STACK 3 #{t.pop(3) == 3 ? 'PASS' : 'FAIL'}"
  t.add(1, 1)
  puts "INSPECT ALL STACKS #{t.data == [1, 2, 2, 2, 3, 3, 3] ? 'PASS' : 'FAIL'}"

  puts "POP STACK 3 #{t.pop(2) == 2 ? 'PASS' : 'FAIL'}"
  t.add(1, 1)
  puts "INSPECT ALL STACKS #{t.data == [1, 1, 2, 2, 3, 3, 3] ? 'PASS' : 'FAIL'}"

  puts "POP STACK 3 #{t.pop(3) == 3 ? 'PASS' : 'FAIL'}"
  t.add(2, 2)
  puts "INSPECT ALL STACKS #{t.data == [1, 1, 2, 2, 2, 3, 3] ? 'PASS' : 'FAIL'}"

  puts "POP STACK 1 #{t.pop(1) == 1 ? 'PASS' : 'FAIL'}"
  t.add(2, 2)
  puts "INSPECT ALL STACKS #{t.data == [1, 2, 2, 2, 2, 3, 3] ? 'PASS' : 'FAIL'}"
end
