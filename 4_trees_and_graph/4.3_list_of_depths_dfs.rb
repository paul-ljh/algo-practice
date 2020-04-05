load "#{Dir.home}/Documents/Interviews/algo-practice/linked_list.rb"
load "#{Dir.home}/Documents/Interviews/algo-practice/bi_node.rb"

def list_of_depths(root)
  dict = {}
  list_of_depths_dfs(root, dict, 0)
  dict
end

def list_of_depths_dfs(root, dict, level)
  return if root.nil?
  root.visited = true
  dict[level] = LinkedList.new unless dict.has_key?(level)
  dict[level].append_to_tail(root.data)

  children = [root.left_node, root.right_node].compact
  children.each do |child|
    list_of_depths_dfs(child, dict, level+1) unless child.visited
  end
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
