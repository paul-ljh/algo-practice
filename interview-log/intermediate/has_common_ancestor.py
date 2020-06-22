'''
Databricks New Grad, June 22

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram, 6 and 8 have common ancestors of 4 and 14.

         14  13
         |   |
1   2    4   12
 \ /   / | \ /
  3   5  8  9
   \ / \     \
    6   7     11

pairs1 = [
  (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
  (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9)
]

Write a function that takes the graph, as well as two of the individuals in our dataset, as its inputs and returns true if and only if they share at least one ancestor.

Sample input and output:

has_common_ancestor(pairs1, 3, 8) => false
has_common_ancestor(pairs1, 5, 8) => true
has_common_ancestor(pairs1, 6, 8) => true
has_common_ancestor(pairs1, 6, 9) => true
has_common_ancestor(pairs1, 1, 3) => false
has_common_ancestor(pairs1, 3, 1) => false
has_common_ancestor(pairs1, 7, 11) => true
has_common_ancestor(pairs1, 6, 5) => true
has_common_ancestor(pairs1, 5, 6) => true

Additional example: In this diagram, 4 and 12 have a common ancestor of 11.

        11
       /  \
      10   12
     /  \
1   2    5
 \ /    / \
  3    6   7
   \        \
    4        8

pairs2 = [
  (11, 10), (11, 12), (2, 3), (10, 2), (10, 5),
  (1, 3), (3, 4), (5, 6), (5, 7), (7, 8),
]

has_common_ancestor(pairs2, 4, 12) => true
has_common_ancestor(pairs2, 1, 6) => false
has_common_ancestor(pairs2, 1, 12) => false

n: number of pairs in the input
'''

class Node:
  def __init__(self, node_id):
    self.node_id = node_id
    self.parents = []
    self.visited = 0

def has_common_ancestor(pairs, n1, n2):
  nodes = set_up_nodes(pairs)
  if n1 not in nodes or n2 not in nodes:
    return False
  explore(nodes, n1)
  nodes[n1].visited = 0
  nodes[n2].visited = 0
  return find_common_ancestor(nodes, n2)

def set_up_nodes(pairs):
  d = {}
  for parent, child in pairs:
    if parent not in d:
      d[parent] = Node(parent)
    if child not in d:
      d[child] = Node(child)
    d[child].parents.append(parent)
  return d

def explore(nodes, n1):
  nodes[n1].visited = 1
  for p in nodes[n1].parents:
    if nodes[p].visited == 0:
      explore(nodes, p)
  return

def find_common_ancestor(nodes, n2):
  nodes[n2].visited = 2
  for p in nodes[n2].parents:
    p_node = nodes[p]
    if p_node.visited == 1:
      return True
    if p_node.visited == 0:
      r = find_common_ancestor(nodes, p)
      if r:
        return r
  return False

def test():
  '''
          11
        /  \
        10   12
      /  \
  1   2    5
  \ /    / \
    3    6   7
    \        \
      4        8
  '''  
  pairs = [
    (11, 10), (11, 12), (2, 3), (10, 2), (10, 5),
    (1, 3), (3, 4), (5, 6), (5, 7), (7, 8),
  ]
  print('PASS' if has_common_ancestor(pairs, 1, 2) == False else 'FAIL')
  print('PASS' if has_common_ancestor(pairs, 1, 3) == False else 'FAIL')
  print('PASS' if has_common_ancestor(pairs, 3, 1) == False else 'FAIL')
  print('PASS' if has_common_ancestor(pairs, 1, 12) == False else 'FAIL')
  print('PASS' if has_common_ancestor(pairs, 1, 8) == False else 'FAIL')
  print('PASS' if has_common_ancestor(pairs, 1, 1) == False else 'FAIL')

  print('PASS' if has_common_ancestor(pairs, 2, 2) == True else 'FAIL')
  print('PASS' if has_common_ancestor(pairs, 3, 4) == True else 'FAIL')
  print('PASS' if has_common_ancestor(pairs, 12, 3) == True else 'FAIL')
  print('PASS' if has_common_ancestor(pairs, 8, 4) == True else 'FAIL')
  print('PASS' if has_common_ancestor(pairs, 6, 5) == True else 'FAIL')
  print('PASS' if has_common_ancestor(pairs, 3, 2) == True else 'FAIL')

if __name__ == "__main__":
  test()
