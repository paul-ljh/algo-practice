=begin
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.

=end

def search_2D_matrix(m, target)
  return false if m.size.zero?
  rows, cols = m.size, m[0].size
  return false if target < m[0][0] || target > m[rows-1][cols-1]

  start_r, start_c = rows - 1, 0
  while start_r != 0 || start_c != cols - 1 do
    if target == m[start_r][start_c]
      return true
    elsif target < m[start_r][start_c]
      start_r -= 1
    else
      start_c += 1
    end
  end
  # Could use binary search when hits the border
  return m[start_r][start_c] == target
end

def test
  m = []
  puts "Input (#{m}, 3) #{search_2D_matrix(m, 3) == false ? "Pass" : "Fail"}"

  m = [[5, 6, 7]]
  puts "Input (#{m}, 3) #{search_2D_matrix(m, 3) == false ? "Pass" : "Fail"}"

  m = [[5, 6, 7]]
  puts "Input (#{m}, 9) #{search_2D_matrix(m, 9) == false ? "Pass" : "Fail"}"

  m = [
    [5, 14, 29],
    [7, 18, 32],
    [10, 22, 39]
  ]
  puts "Input (#{m}, 29) #{search_2D_matrix(m, 29) == true ? "Pass" : "Fail"}"
  puts "Input (#{m}, 39) #{search_2D_matrix(m, 39) == true ? "Pass" : "Fail"}"
  puts "Input (#{m}, 5) #{search_2D_matrix(m, 5) == true ? "Pass" : "Fail"}"
  puts "Input (#{m}, 28) #{search_2D_matrix(m, 28) == false ? "Pass" : "Fail"}"
  puts "Input (#{m}, 28) #{search_2D_matrix(m, 31) == false ? "Pass" : "Fail"}"
end
