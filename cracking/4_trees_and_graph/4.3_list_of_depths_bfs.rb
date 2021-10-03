load "#{Dir.home}/Documents/Interviews/algo-practice/linked_list.rb"
load "#{Dir.home}/Documents/Interviews/algo-practice/bi_node.rb"
load "#{Dir.home}/Documents/Interviews/algo-practice/queue.rb"

BiNode.class_eval { attr_accessor :level }

def list_of_depths(root)
  return {} if root.nil?
  dict, q = Hash.new, Queue.new
  root.get_all_nodes.each do |node| 
    node.visited = false
    node.level = nil
  end
  root.visited, root.level = true, 0
  q.push(root)

  until q.is_empty? do
    parent = q.pop
    unless dict.has_key?(parent.level)
      dict[parent.level] = LinkedList.new
    end
    dict[parent.level].append_to_tail(parent.data)
    children = [parent.left_node, parent.right_node].compact
    children.each do |child|
      unless child.visited
        child.visited = true
        child.level = parent.level + 1
        q.push(child)
      end
    end
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
