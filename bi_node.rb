class BiNode
  attr_accessor :data, :key, :left_node, :right_node

  def initialize(data:, key: nil, left_node: nil, right_node: nil)
    @data = data
    @key = key
    @left_node = left_node
    @right_node = right_node
  end
end
