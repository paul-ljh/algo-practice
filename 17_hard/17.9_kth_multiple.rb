load "#{Dir.home}/Documents/Interviews/algo-practice/queue.rb"

def kth_multiple(k)
  return nil if k.zero?
  queues = [Queue.new, Queue.new, Queue.new]
  init = 1
  1.upto(k-1) do
    queues.each_with_index { |q, index| q.push(init * (2 * index + 3)) }
    minimum = queues.map(&:peek).min
    queues.each { |q| q.pop if q.peek == minimum }
    init = minimum
  end
  return init
end

def test
  result = (1..14).map { |i| kth_multiple(i) }
  puts result == [1,3,5,7,9,15,21,25,27,35,45,49,63,75] ? 'PASS' : 'FAIL'
end
