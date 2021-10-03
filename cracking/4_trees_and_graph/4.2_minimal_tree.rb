load "#{Dir.home}/Documents/Interviews/algo-practice/bi_node.rb"

def minimal_tree(arr)
  minimal_tree_helper(arr, 0, arr.size-1)
end

def minimal_tree_helper(arr, start, finish)
  return nil if start > finish
  return BiNode.new(data: arr[start]) if start == finish
  mid = (finish - start + 1) / 2
  left, right = minimal_tree_helper(arr, start, start+mid-1), minimal_tree_helper(arr, start+mid+1, finish)
  return BiNode.new(data: arr[start+mid], left_node: left, right_node: right)
end

def test
  a = minimal_tree([1])
  puts a.data == 1 ? 'PASS' : 'FAIL'

  a = minimal_tree([1,2,3,4,5])
  puts a.data == 3 ? 'PASS' : 'FAIL'
  puts a.left_node.data == 2 ? 'PASS' : 'FAIL'
  puts a.left_node.left_node.data == 1 ? 'PASS' : 'FAIL'
  puts a.right_node.data == 5 ? 'PASS' : 'FAIL'
  puts a.right_node.left_node.data == 4 ? 'PASS' : 'FAIL'

  a = minimal_tree([1,2,3,4,5,6])
  puts a.data == 4 ? 'PASS' : 'FAIL'
  puts a.left_node.data == 2 ? 'PASS' : 'FAIL'
  puts a.left_node.left_node.data == 1 ? 'PASS' : 'FAIL'
  puts a.left_node.right_node.data == 3 ? 'PASS' : 'FAIL'
  puts a.right_node.data == 6 ? 'PASS' : 'FAIL'
  puts a.right_node.left_node.data == 5 ? 'PASS' : 'FAIL'
end
