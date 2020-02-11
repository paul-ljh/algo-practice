class ZeroMatrix
  attr_reader :matrix
  def initialize(matrix)
    @matrix = matrix
    
    if @matrix.any? && @matrix.length > 1
      @c, @r = matrix.length, matrix[0].length
      zero_it()
      nullify()
    end
  end

  def zero_it
    0.upto(@r-1) do |row|
      0.upto(@c-1) do |col|
        if @matrix[col][row] == 0
          @matrix[col][0], @matrix[0][row] = 0, 0
        end
      end
    end
  end

  def nullify
    (@c-1).downto(1) do |col|
      if @matrix[col][0] == 0
        nullify_column(col)
      end
    end

    (@r-1).downto(1) do |row|
      if @matrix[0][row] == 0
        nullify_row(row)
      end
    end

    if @matrix[0][0] == 0
      nullify_column(0)
      nullify_row(0)
    end
  end

  def nullify_column(col)
    0.upto(@r - 1) do |row|
      @matrix[col][row] = 0
    end
  end

  def nullify_row(row)
    0.upto(@c - 1) do |col|
      @matrix[col][row] = 0
    end
  end
end

def test
  puts "Input ('[]') #{ZeroMatrix.new([]).matrix == [] ? "Pass" : "Fail"}"
  puts "Input ('[0]') #{ZeroMatrix.new([0]).matrix == [0] ? "Pass" : "Fail"}"
  puts "Input ('[[1,3], [2,0]]') #{ZeroMatrix.new([[1,3], [2,0]]).matrix == [[1,0], [0,0]] ? "Pass" : "Fail"}"
  
  puts "Input ('[[0,4,7], [2,0,8],[3,6,0]]') #{
    ZeroMatrix.new([[1,4,7], [2,0,8],[3,6,0]]).matrix == [[1,0,0], [0,0,0], [0,0,0]] ? 
    "Pass" : "Fail"}"

  puts "Input ('[[0,4,7], [2,0,8],[3,6,0]]') #{
    ZeroMatrix.new([[0,4,7], [2,0,8],[3,6,0]]).matrix == [[0,0,0], [0,0,0], [0,0,0]] ? 
    "Pass" : "Fail"}"
end
