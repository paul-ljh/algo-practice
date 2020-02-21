load 'linked_list.rb'

def remove_dups(l)
  return l if l.head.nil? || l.head.next_node.nil?
  dict = Hash.new
  curr, prev = l.head, nil

  while curr != nil
    if dict.has_key?(curr.data)
      prev.next_node = curr.next_node
    else
      dict[curr.data] = true
      prev = curr
    end
    curr = curr.next_node
  end
  return l
end

def test
  l = LinkedList.new(3)
  l.append_to_tail(3)
  l.append_to_tail(3)
  remove_dups(l)
  puts "L Head is 3? #{l.head.data == 3 ? "Pass" : "Fail"}"
  puts "L only has one node? #{l.head.next_node == nil ? "Pass" : "Fail"}"
end
