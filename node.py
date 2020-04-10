class Node:
  def __init__(self, *, data, children, parents):
    self.data = data
    self.children = set(children)
    self.parents = set(parents)
    self.visited = False

  def get_all_descendants(self):
    if self is None: return []
    result = [self]
    for child in self.children:
      result.extend(child.get_all_descendants())
    return result
