load 'linked_list.rb'

def intersection_iter(l1, l2)
  return nil if l1.head.nil? || l2.head.nil?

  diff = l1.length - l2.length
  if diff > 0
    fir, sec = l1.head, l2.head
  else
    fir, sec = l2.head, l1.head
  end

  fir = move_head(fir, diff.abs)
  while !fir.nil? && !sec.nil? do
    return fir if fir == sec
    fir, sec = fir.next_node, sec.next_node
  end
  return nil
end

def move_head(head, diff)
  return head if diff.zero?
  1.upto(diff) do
    head = head.next_node
  end
  return head
end

def intersection_recur(l1, l2)
  return nil if l1.head.nil? || l2.head.nil?

  diff = l1.length - l2.length
  if diff < 0
    return intersection_helper(l2.head, l1.head, diff.abs)
  else
    return intersection_helper(l1.head, l2.head, diff.abs)
  end
end

def intersection_helper(long, short, diff)
  if long.nil? && short.nil?
    return nil
  end
  if diff > 0
    return intersection_helper(long.next_node, short, diff-1)
  end
  if long == short
    return long
  else
    return intersection_helper(long.next_node, short.next_node, diff)
  end
end


def test
  l1 = LinkedList.new([])
  l2 = LinkedList.new([])
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_iter(l1, l2)).nil? ? 'NIL' : r.data}"
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_recur(l1, l2)).nil? ? 'NIL' : r.data}"

  l1 = LinkedList.new([1, 2])
  l2 = LinkedList.new([])
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_iter(l1, l2)).nil? ? 'NIL' : r.data}"
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_recur(l1, l2)).nil? ? 'NIL' : r.data}"

  l1 = LinkedList.new([])
  l2 = LinkedList.new([1, 2])
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_iter(l1, l2)).nil? ? 'NIL' : r.data}"
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_recur(l1, l2)).nil? ? 'NIL' : r.data}"

  # Same Length, non-intersect
  l1 = LinkedList.new([1, 2, 5])
  l2 = LinkedList.new([1, 2, 5])
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_iter(l1, l2)).nil? ? 'NIL' : r.data}"
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_recur(l1, l2)).nil? ? 'NIL' : r.data}"

  # Diff Length, non-intersect
  l1 = LinkedList.new([1, 2, 5, 6,])
  l2 = LinkedList.new([1, 2, 5])
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_iter(l1, l2)).nil? ? 'NIL' : r.data}"
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_recur(l1, l2)).nil? ? 'NIL' : r.data}"

  # Same Length, intersect
  common = LinkedList.new([6, 2])
  l1 = LinkedList.new([1])
  l2 = LinkedList.new([1])
  l1.head.next_node = common.head
  l2.head.next_node = common.head
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_iter(l1, l2)).nil? ? 'NIL' : r.data}"
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_recur(l1, l2)).nil? ? 'NIL' : r.data}"

  # Diff Length, intersect
  common = LinkedList.new([6, 2])
  l1 = LinkedList.new([1])
  l2 = LinkedList.new([1, 2])
  l1.head.next_node = common.head
  l2.head.next_node.next_node = common.head
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_iter(l1, l2)).nil? ? 'NIL' : r.data}"
  puts "l1: #{l1.print_list}, l2: #{l2.print_list} intersect at #{(r = intersection_recur(l1, l2)).nil? ? 'NIL' : r.data}"
end
