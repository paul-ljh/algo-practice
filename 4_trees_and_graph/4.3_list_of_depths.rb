load "#{Dir.home}/Documents/Interviews/algo-practice/linked_list.rb"
load "#{Dir.home}/Documents/Interviews/algo-practice/bi_node.rb"

def list_of_depths(root)
  dict = {}
  list_of_depths_helper(root, dict, 0)
end

def list_of_depths_helper(root, dict, level)
  return dict if root.nil?
  if !dict.has_key?(level)
    dict[level] = LinkedList.new
  end
  dict[level].append_to_tail(root.data)
  list_of_depths_helper(root.left_node, dict, level+1)
  list_of_depths_helper(root.right_node, dict, level+1)
  return dict
end

def test
  root = BiNode.new(
    data: 5,
    left_node: BiNode.new(
      data: 8,
      left_node: BiNode.new(
        data: 7,
        left_node: BiNode.new(data: 10),
        right_node: BiNode.new(data: 9)
      )
    ),
    right_node: BiNode.new(data: 6)
  )
  result = list_of_depths(root)
  result.each do |key, value|
    puts "#{key}: #{value.print_list}"
  end
end
