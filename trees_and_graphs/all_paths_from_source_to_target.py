'''
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

EX:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

https://leetcode.com/problems/all-paths-from-source-to-target/
'''

def all_paths_source_target(graph):
  cache = {}
  find_path(0, len(graph) - 1, cache, graph)
  return cache.get(0, [])

def find_path(curr, target, cache, graph):
  if curr in cache:
    return
  if curr == target:
    cache[target] = [[target]]
    return
  for neighbour in graph[curr]:
    find_path(neighbour, target, cache, graph)
    if neighbour in cache:
      if curr not in cache:
        cache[curr] = []
      cache[curr].extend(map(lambda l: [curr] + l, cache[neighbour]))
  return

'''
Idea:
cache[i]: an array contains all paths from node i to node N-1

Once all paths from 1 particular node have been explored, there is no need to do it again. All subsequent calls recursed on that node can fetch the result from cache and use it.
'''
