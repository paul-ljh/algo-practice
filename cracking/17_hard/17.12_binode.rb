load "#{Dir.home}/Documents/Interviews/algo-practice/bi_node.rb"

def bi_node(bin_tree)
  return bin_tree, bin_tree if bin_tree.nil? || (bin_tree.left_node.nil? && bin_tree.right_node.nil?)
  left_s, left_b = bin_tree.left_node.nil? ? [bin_tree, nil] : bi_node(bin_tree.left_node)
  right_s, right_b = bin_tree.right_node.nil? ? [nil, bin_tree] : bi_node(bin_tree.right_node)
  bin_tree.left_node, bin_tree.right_node = left_b, right_s
  left_b.right_node = bin_tree unless left_b.nil?
  right_s.left_node = bin_tree unless right_s.nil?
  return left_s, right_b
end

def test
  puts "TREE: 5"
  left, right = bi_node(BiNode.new(data: 5))
  puts "LIST:\n#{left.print}#{right.print}\n"
  
  puts 'TREE: 3<-5'
  n = BiNode.new(data: 5, left_node: BiNode.new(data: 3))
  left, right = bi_node(n)
  puts "LIST:\n#{left.print}#{right.print}\n"
  
  puts 'TREE: 5->8'
  n = BiNode.new(data: 5, right_node: BiNode.new(data: 8))
  left, right = bi_node(n)
  puts "LIST:\n#{left.print}#{right.print}\n"

  puts 'TREE: 3<-5->8'
  n = BiNode.new(data: 5, left_node: BiNode.new(data: 3), right_node: BiNode.new(data: 8))
  left, right = bi_node(n)
  puts "LIST:\n#{left.print}#{right.print}\n"

  puts 'TREE: [3, 4, 5, 6, 8]'
  n = BiNode.new(data: 5,
    left_node: BiNode.new(
      data: 3,
      right_node: BiNode.new(data: 4),
    ),
    right_node: BiNode.new(
      data: 8,
      left_node: BiNode.new(data: 6),
    ))
  left, right = bi_node(n)
  puts "LIST:\n#{left.print}#{right.print}\n"

  puts 'TREE: [1, 3, 4, 5, 6, 8, 9]'
  n = BiNode.new(data: 5,
    left_node: BiNode.new(
      data: 3,
      left_node: BiNode.new(data: 1),
      right_node: BiNode.new(data: 4),
    ),
    right_node: BiNode.new(
      data: 8,
      left_node: BiNode.new(data: 6),
      right_node: BiNode.new(data: 9),
    ))
  left, right = bi_node(n)
  puts "LIST:\n#{left.print}#{right.print}\n"
end
