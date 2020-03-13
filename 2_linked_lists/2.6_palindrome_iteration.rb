load 'linked_list.rb'

def palindrome(l)
  return true if l.head.nil?
  stack = []
  slow, fast = l.head, l.head
  while !fast.nil? && !fast.next_node.nil? do
    stack.push(slow.data)
    slow = slow.next_node
    fast = fast.next_node.next_node
  end

  # odd length
  if !fast.nil?
    slow = slow.next_node
  end

  while !slow.nil? do
    return false if stack.pop != slow.data
    slow = slow.next_node
  end
  return true
end

def test
  l = LinkedList.new([])
  puts "Is l: #{l.print_list} a palindrome? #{palindrome(l)}"

  l = LinkedList.new([1])
  puts "Is l: #{l.print_list} a palindrome? #{palindrome(l)}"

  l = LinkedList.new([1,2,1])
  puts "Is l: #{l.print_list} a palindrome? #{palindrome(l)}"

  l = LinkedList.new([1,3,4,4,3,1])
  puts "Is l: #{l.print_list} a palindrome? #{palindrome(l)}"

  l = LinkedList.new([1,3,4,2,1])
  puts "Is l: #{l.print_list} a palindrome? #{palindrome(l)}"

  l = LinkedList.new([1,3,4,4,3,0])
  puts "Is l: #{l.print_list} a palindrome? #{palindrome(l)}"

  l = LinkedList.new([0,3,4,4,3,1])
  puts "Is l: #{l.print_list} a palindrome? #{palindrome(l)}"

  l = LinkedList.new([1,3,5,4,3,1])
  puts "Is l: #{l.print_list} a palindrome? #{palindrome(l)}"
end

