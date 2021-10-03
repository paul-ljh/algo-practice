def rotate_matrix(m)
  return m if m.length == 0 || m.length == 1
  0.upto(m.length / 2 - 1) do |c|
    tmp = nil
    c.upto(m.length - 2 - c) do |r|
      tmp = m[c][r]
      m[c][r] = m[r][m.length - 1 - c]
      m[r][m.length - 1 - c] = m[m.length - 1 - c][m.length - 1 - r]
      m[m.length - 1 - c][m.length - 1 - r] = m[m.length - 1 - r][c]
      m[m.length - 1 - r][c] = tmp
    end
  end
  return m
end

def test
  puts "Input ('[]') #{rotate_matrix([]) == [] ? "Pass" : "Fail"}"
  puts "Input ('[1]') #{rotate_matrix([1]) == [1] ? "Pass" : "Fail"}"
  puts "Input ('[[1,3], [2,4]]') #{rotate_matrix([[1,3], [2,4]]) == [[3,4], [1,2]] ? "Pass" : "Fail"}"
  puts "Input ('[[1,4,7], [2,5,8],[3,6,9]]') #{rotate_matrix(
    [[1,4,7], [2,5,8],[3,6,9]]) == [[7,8,9], [4,5,6], [1,2,3]] ? "Pass" : "Fail"}"

  puts "Input ('[[1,5,9,13], [2,6,10,14], [3,7,11,15], [4,8,12,16]]') #{rotate_matrix(
    [[1,5,9,13], [2,6,10,14], [3,7,11,15], [4,8,12,16]]) == 
    [[13,14,15,16], [9,10,11,12], [5,6,7,8], [1,2,3,4]] ? "Pass" : "Fail"}"
end
