class ThreeInOne
  def initialize(len)
    @data = Array.new(len, nil)
    @sizes = Array.new(3, 0)
    @capacities = [len/3, len/3, len - 2*len/3]
  end

  def is_empty?(stack_num)
    @sizes[stack_num-1].zero?
  end
  
  def is_full?(stack_num)
    @sizes[stack_num-1] >= @capacities[stack_num-1]
  end

  def top_index(stack_num)
    @sizes[stack_num-1] + @data.size / 3 * (stack_num-1) - 1
  end

  def peek(stack_num)
    puts "PEEKING STACK #{stack_num}"
    raise "Stack #{stack_num} is empty!" if is_empty?(stack_num)
    puts "STACK #{stack_num} top is #{@data[top_index(stack_num)]}"
    @data[top_index(stack_num)]
  end

  def pop(stack_num)
    puts "POPPING STACK #{stack_num}"
    data_to_return = peek(stack_num)
    @data[top_index(stack_num)] = nil
    @sizes[stack_num-1] -= 1
    puts "POPPED #{data_to_return} from STACK #{stack_num}"
    data_to_return
  end

  def add(item, stack_num)
    puts "ADDING #{item} to STACK #{stack_num}"
    raise "Stack #{stack_num} is full!" if is_full?(stack_num)
    @data[top_index(stack_num)+1] = item
    @sizes[stack_num-1] += 1
    top_index(stack_num)
  end
end

def test
  puts "INIT with length 7"
  t = ThreeInOne.new(7)

  t.add(1,3)
  t.add(2,2)

  begin
    t.peek(1)
  rescue
    puts "ERROR: Stack 1 is empty"
  end
  t.peek(3)
  t.peek(2)

  t.add(3,3)
  t.add(7,3)
  t.add(4,2)

  begin
    t.peek(3)
  rescue
    puts "ERROR: Stack 3 is full"
  end

  begin
    t.peek(2)
  rescue
    puts "ERROR: Stack 2 is full"
  end

  begin
    t.pop(1)
  rescue
    puts "ERROR: Stack 1 is empty"
  end

  t.pop(2)
  t.pop(2)
  begin
    t.pop(2)
  rescue
    puts "ERROR: Stack 2 is empty"
  end
end
