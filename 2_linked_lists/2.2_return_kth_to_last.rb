load 'linked_list.rb'

def iterative_kth_to_last(l, k)
  return false if k.zero?
  first, second = l.head, l.head
  1.upto(k) do
    return false if first.nil?
    first = first.next_node
  end

  while !first.nil? do
    first, second = first.next_node, second.next_node
  end
  return second.data
end

def test
  l = LinkedList.new()
  l.append_to_tail(1)
  l.append_to_tail(2)
  l.append_to_tail(3)
  l.append_to_tail(4)
  l.append_to_tail(5)
  puts "Input [5]: #{iterative_kth_to_last(l, 5) == 1 ? "Pass" : "Fail"}"
  puts "Input [1]: #{iterative_kth_to_last(l, 1) == 5 ? "Pass" : "Fail"}"
  puts "Input [2]: #{iterative_kth_to_last(l, 2) == 4 ? "Pass" : "Fail"}"
  puts "Input [0]: #{iterative_kth_to_last(l, 0) == false ? "Pass" : "Fail"}"
  puts "Input [6]: #{iterative_kth_to_last(l, 6) == false ? "Pass" : "Fail"}"
  puts "Input [8]: #{iterative_kth_to_last(l, 8) == false ? "Pass" : "Fail"}"
end
