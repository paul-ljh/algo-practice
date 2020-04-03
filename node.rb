class Node
  attr_accessor :data, :children, :visited

  def initialize(data, *children)
    @data = data
    @children = children
    @visited = false
  end

  def get_all_nodes(node=self)
    return node if node.children.empty?
    result = [node]
    for child in node.children do
      result.push(*get_all_nodes(child))
    end
    return result
  end
end
