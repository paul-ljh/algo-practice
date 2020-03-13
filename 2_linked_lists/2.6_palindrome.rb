load 'linked_list.rb'

def palindrome(l)
  return true if l.head.nil?

  result, m = is_palindrome(l.head, l.head, 0, l.length)
  return result
end

def is_palindrome(l, m, index, len)
  if len.odd? && index == len / 2
    return true, m
  elsif len.even? && index == len / 2 - 1
    m = m.next_node
    return l.data == m.data, m
  end

  result, m = is_palindrome(l.next_node, m.next_node, index + 1, len)
  m = m.next_node
  return result && m.data == l.data, m
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

