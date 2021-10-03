load "#{Dir.home}/Documents/Interviews/algo-practice/stack.rb"

def sort_stack(s)
  return s if s.is_empty?
  storage = Stack.new
  until s.is_empty? do
    temp = s.pop
    until storage.is_empty? || storage.peek >= temp do
      s.push(storage.pop)
    end
    storage.push(temp)
  end
  return storage
end

def test
  s = Stack.new
  puts sort_stack(s).inspect

  s = Stack.new
  [1].each { |item| s.push(item) }
  puts sort_stack(s).inspect

  s = Stack.new
  [1,2,3,4,5].each { |item| s.push(item) }
  puts sort_stack(s).inspect

  s = Stack.new
  [5,4,3,2,1].each { |item| s.push(item) }
  puts sort_stack(s).inspect

  s = Stack.new
  [8,1,3,7,5,3,3].each { |item| s.push(item) }
  puts sort_stack(s).inspect
end
