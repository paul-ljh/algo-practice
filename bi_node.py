class BiNode:
  def __init__(self, *, data, left_node=None, right_node=None):
    self.data = data
    self.left_node = left_node
    self.right_node = right_node
    self.visited = False

  def get_all_nodes(self):
    if self is None: return []
    result = [self]
    left = [] if self.left_node is None else self.left_node.get_all_nodes()
    right = [] if self.right_node is None else self.right_node.get_all_nodes()
    result.extend(left)
    result.extend(right)
    return result

def test():
  n = BiNode(
    data=4,
    left_node=BiNode(
      data=5,
      left_node=BiNode(data=8),
      right_node=BiNode(data=9)),
    right_node=BiNode(
      data=6,
      left_node=BiNode(
        data=19,
        left_node=BiNode(data=20),
      )),
  )
  for node in n.get_all_nodes():
    print(node.data)

if __name__ == '__main__':
    test()
