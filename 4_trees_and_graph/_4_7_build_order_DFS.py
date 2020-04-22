import sys
sys.path.append("/Users/pauLi/Documents/Interviews/algo-practice/")

from node import Node

def build_order(projs, deps):
  if projs is None:
    return []
  nodes = build_graph(projs, deps)
  return order(nodes, [])

def build_graph(projs, deps):
  nodes = {}
  for proj in projs:
    nodes[proj] = Node(data=proj, children=[], parents=[])
  for parent, child in deps:
    nodes[parent].children.add(nodes[child])
    nodes[child].parents.add(nodes[parent])
  return nodes

def order(nodes, result):
  for proj_name, node in nodes.items():
    if not node.visited:
      if not dfs(node, result):
        return False
  result.reverse()
  return result

def dfs(root, result):
  if root is None:
    return True
  root.visited = "visiting"
  for child in root.children:
    if child.visited == "visiting":
      return False
    elif child.visited == False:
      if not dfs(child, result):
        return False
  root.visited = True
  result.append(root.data)
  return True
  
def test():
  projs = [1,2,3,4,5,6]
  deps = [(1,4), (6,2), (2,4), (6,1), (4,3)]
  print('PASS' if build_order(projs, deps) == [6, 5, 2, 1, 4, 3] else 'FAIL')
  print(build_order(projs, deps))
  
  projs = [1,2,3,4,5,6,7]
  deps = [(6,1), (6,2), (7,1), (7,2), (1,3), (2,3), (4,3), (3,5)]
  print('PASS' if build_order(projs, deps) == [7, 6, 4, 2, 1, 3, 5] else 'FAIL')
  print(build_order(projs, deps))
    
  projs = [1,2,3,4,5,6,7]
  deps = [(1,2), (2,3), (3,4), (4,5), (5,6), (6,1)]
  print('PASS' if build_order(projs, deps) == False else 'FAIL')
    
if __name__ == '__main__':
  test()
  