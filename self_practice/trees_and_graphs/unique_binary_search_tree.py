'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

Input: 3
Output: 5

Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

Source: https://leetcode.com/problems/unique-binary-search-trees/
'''

'''
The idea behind the algorithm:

First of all, 2 BSTs of different number of nodes must be structurally unique.

Second of all, given a set of distinctive, positive integers of size n, they can fullfill a BST of any arbitrary structure of size n.

Last but not least, a BST of size n must have (n-1) children nodes, how many unique BST pairs can you generate from (n-1) nodes?
'''
from math import ceil

def unique_binary_search_tree(n):
  result_cache = [1]
  for num_of_nodes in range(1, n+1):
    curr_result = 0
    for i in range(ceil(num_of_nodes / 2)):
      curr_result += (result_cache[i]
                      * result_cache[num_of_nodes - 1 - i]
                      * (1 if i == num_of_nodes - 1 - i else 2))
    result_cache.append(curr_result)
  return result_cache[n]

def test():
  answer = [1,1,2,5,14,42]
  for i in range(len(answer)):
    print('PASS' if unique_binary_search_tree(i) == answer[i] else 'FAIL')

if __name__ == "__main__":
  test()
