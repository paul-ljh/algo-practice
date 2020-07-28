=begin
Given a 2D matrix m and an integer k, complete the following tasks

1. find the maximal sum of all possible k x k sub-matrices within m
2. Compute and return the sum of all distinct elements within all k x k sub-matrices of the maximal sum 

Assume m is a non-empty matrix, and k is valid with respect to m's size

=end

require 'pp'
require 'set'

class BestSquare
  class Coordinate
    attr_reader :x, :y
    def initialize(x, y)
      @x, @y = x, y
    end
  end

  def initialize(m, k)
    @m = m
    @k = k
    @rows, @cols = m.size, m[0].size
    precompute_first_k_entries
    find_max_sum
  end

  def precompute_first_k_entries
    @first_k_entries = []
    0.upto(@rows-1) do |x|
      @first_k_entries << (0..@k-1).inject(0) { |sum, y| sum + @m[x][y] }
    end
  end
  
  def find_max_sum
    @max_sum, @coordinates = 0, []
    0.upto(@cols-@k) do |y|
      sum = 0
      0.upto(@rows-@k) do |x|
        if y.zero?
          if x.zero?
            sum = (x..x+@k-1).inject(0) { |result, i| result + @first_k_entries[i]}
            @max_sum = sum
          else
            sum += (@first_k_entries[x+@k-1] - @first_k_entries[x-1])
          end
        else
          if x.zero?
            sum = (x..x+@k-1).inject(0) do |result, i|
              @first_k_entries[i] += (@m[x+i][y+@k-1] - @m[x+i][y-1]) 
              result + @first_k_entries[i]
            end
          else
            @first_k_entries[x+@k-1] += (@m[x+@k-1][y+@k-1] - @m[x+@k-1][y-1]) 
            sum += (@first_k_entries[x+@k-1] - @first_k_entries[x-1])
          end
        end

        if sum >= @max_sum
          if sum > @max_sum
            @max_sum = sum
            @coordinates = []
          end
          @coordinates.push(Coordinate.new(x,y))
        end
      end
    end
  end

  def sum_distinct_element
    set = Set.new
  end
end

def test
  m = [
    [1,2,3,4],
    [2,5,6,7],
    [5,6,8,1],
    [10,2,9,4],
  ]
  bs = BestSquare.new(m, 2)
end
