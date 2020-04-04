class BiNode
  attr_accessor :data, :visited, :key, :left_node, :right_node

  def initialize(data:, key: nil, left_node: nil, right_node: nil)
    @data = data
    @key = key
    @visited = false
    @left_node = left_node
    @right_node = right_node
  end

  def get_all_nodes
    return [] if nil?
    result = [self]
    left = @left_node.nil? ? [] : @left_node.get_all_nodes
    right = @right_node.nil? ? [] : @right_node.get_all_nodes
    result.push(*left, *right)
    return result
  end

  def print
    return 'nil' if self.nil?
    result = [@data]
    left, right = @left_node, @right_node
    while !left.nil? || !right.nil? do
      unless right.nil?
        result.push("#{right.data}")
        right = right.right_node
      end
      unless left.nil?
        result.prepend("#{left.data}")
        left = left.left_node
      end
    end
    result = result.join("<->")
    return result + "\n"
  end
end
