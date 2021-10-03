load "#{Dir.home}/Documents/Interviews/algo-practice/tree.rb"
load "#{Dir.home}/Documents/Interviews/algo-practice/queue.rb"

def routes_between_nodes(root, start, finish)
  return false if root.nil?
  return true if start == finish
  all_nodes = root.get_all_nodes
  all_nodes.each { |node| node.visited = false }
  start.visited = true
  q = Queue.new
  q.push(start)

  until q.is_empty? do
    parent = q.pop
    parent.children.each do |child|
      unless child.visited
        return true if child == finish
        child.visited = true
        q.push(child)
      end
    end
  end
  return false
end

def test
  finish, another_finish = Node.new(6), Node.new(-1)
  b = Node.new(5, Node.new(6), finish, Node.new(6))
  start = Node.new(3, b)
  a = Node.new(4, Node.new(3), start, Node.new(3))
  root = Node.new(1, a, b, another_finish)

  puts routes_between_nodes(nil, start, start) == false ? 'PASS' : 'FAIL'
  puts routes_between_nodes(root, start, start) ? 'PASS' : 'FAIL'

  puts routes_between_nodes(root, start, another_finish) == false ? 'PASS' : 'FAIL'
  puts routes_between_nodes(root, start, finish) ? 'PASS' : 'FAIL'
  puts routes_between_nodes(root, root, start) ? 'PASS' : 'FAIL'
  puts routes_between_nodes(root, root, finish) ? 'PASS' : 'FAIL'
  puts routes_between_nodes(root, root, another_finish) ? 'PASS' : 'FAIL'
  puts routes_between_nodes(root, a, b) ? 'PASS' : 'FAIL'
  puts routes_between_nodes(root, b, a) == false ? 'PASS' : 'FAIL'
end
