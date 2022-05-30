# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

class Solution:
  def countSubTrees(self, n, edges, labels):
    self.label_hash = {}
    self.output = [0] * n
    self.visited = [False] * n
    self.labels = labels

    self.build_adjacency_matrix(edges)
    self.count_label(0)
    return self.output

  def build_adjacency_matrix(self, edges):
    self.matrix = {}
    for edge in edges:
      self.matrix.setdefault(edge[0], []).append(edge[1])
      self.matrix.setdefault(edge[1], []).append(edge[0])
    return

  def count_label(self, root):
    self.visited[root] = True
    if len(self.matrix[root]) == 1 and self.visited[self.matrix[root][0]]:
      self.label_hash.setdefault(self.labels[root], 0)
      self.label_hash[self.labels[root]] += 1
      self.output[root] = 1
      return

    prev_count = self.label_hash.get(self.labels[root], 0)
    for child in self.matrix[root]:
      if not self.visited[child]:
        self.count_label(child)
    self.label_hash.setdefault(self.labels[root], 0)
    self.label_hash[self.labels[root]] += 1
    self.output[root] = self.label_hash[self.labels[root]] - prev_count
    return
