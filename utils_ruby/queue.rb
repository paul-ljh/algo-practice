load "#{Dir.home}/Documents/Interviews/algo-practice/uni_node.rb"

class Queue
  attr_reader :length

  def initialize
    @first = nil
    @last = nil
    @length = 0
  end

  def push(data)
    new_last = UniNode.new(data)
    @last.next_node = new_last unless @last.nil?
    @last = new_last
    @first = new_last if @first.nil?
    @length += 1
  end

  def pop
    raise "EMPTY QUEUE" if is_empty?
    data_to_pop = @first.data
    @first = @first.next_node
    @last = nil if @first.nil?
    @length -= 1
    data_to_pop
  end

  def is_empty?
    @first.nil?
  end

  def peek
    raise "EMPTY QUEUE" if is_empty?
    return @first.data
  end    
end

def test
  q = Queue.new
  q.push(5)
  puts q.peek == 5 ? 'PASS' : 'FAIL'
  puts q.is_empty? == false ? 'PASS' : 'FAIL'
  puts q.length == 1 ? 'PASS' : 'FAIL'

  q.push(4)
  puts q.peek == 5 ? 'PASS' : 'FAIL'
  puts q.is_empty? == false ? 'PASS' : 'FAIL'
  puts q.length == 2 ? 'PASS' : 'FAIL'

  puts q.pop == 5 ? 'PASS' : 'FAIL'
  puts q.is_empty? == false ? 'PASS' : 'FAIL'
  puts q.length == 1 ? 'PASS' : 'FAIL'

  puts q.pop == 4 ? 'PASS' : 'FAIL'
  puts q.is_empty? ? 'PASS' : 'FAIL'
  puts q.length == 0 ? 'PASS' : 'FAIL'
end


