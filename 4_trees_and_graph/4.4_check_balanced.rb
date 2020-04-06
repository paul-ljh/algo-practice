load "#{Dir.home}/Documents/Interviews/algo-practice/bi_node.rb"

def check_balanced(root)
  return true if root.nil?
  check_by_height(root) != -1
end

def check_by_height(root)
  return 1 if root.left_node.nil? && root.right_node.nil?
  left = root.left_node.nil? ? 0 : check_by_height(root.left_node)
  right = root.right_node.nil? ? 0 : check_by_height(root.right_node)
  return -1 if left == -1 || right == -1 || (left-right).abs > 1
  return [left, right].max + 1
end

def test
  t = nil
  puts check_balanced(t) ? 'PASS' : 'FAIL'

  t = BiNode.new(data: 6)
  puts check_balanced(t) ? 'PASS' : 'FAIL'

  t = BiNode.new(
    data: 6,
    left_node: BiNode.new(data: 7),
    right_node: BiNode.new(
      data: 8,
      right_node: BiNode.new(data: 9)
    )
  )
  puts check_balanced(t) ? 'PASS' : 'FAIL'

  t = BiNode.new(
    data: 6,
    left_node: BiNode.new(data: 7),
    right_node: BiNode.new(
      data: 9,
      left_node: BiNode.new(
        data: 10,
        right_node: BiNode.new(data: 11)
      ),
      right_node: BiNode.new(data: 12)
    )
  )
  puts !check_balanced(t) ? 'PASS' : 'FAIL'

  t = BiNode.new(
    data: 6,
    left_node: BiNode.new(data: 7),
    right_node: BiNode.new(
      data: 9,
      left_node: BiNode.new(data: 10),
      right_node: BiNode.new(
        data: 12,
        left_node: BiNode.new(
          data: 15,
          left_node: BiNode.new(data: 11)
        )
      )
    )
  )
  puts !check_balanced(t) ? 'PASS' : 'FAIL'
end

