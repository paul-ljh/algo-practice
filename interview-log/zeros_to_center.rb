=begin

Given an array of numbers, move all zeros to the center of the array. Nonzero elements in the array should retain their relative positions. 

For the purpose of this question, the centre is floor(array.length/2)

=end
require 'pp'

# 2-Pass in-place algo
def zeros_to_center(arr)
  return arr if arr.empty?

  non_zero_counts = count_non_zeros(arr)
  left_swaps, right_swaps = non_zero_counts / 2, non_zero_counts / 2 + non_zero_counts % 2
  swap_counts = 0
  0.upto(arr.length - 1) do |i|
    if swap_counts < left_swaps
      if !arr[i].zero?
        if swap_counts < i
          arr[swap_counts] = arr[i]
          arr[i] = 0
        end
        swap_counts += 1
      end
    else
      break
    end
  end

  swap_counts = 0
  (arr.length - 1).downto(0) do |i|
    if swap_counts < right_swaps
      if !arr[i].zero?
        if swap_counts < arr.length - 1 - i
          arr[arr.length - swap_counts - 1] = arr[i]
          arr[i] = 0
        end
        swap_counts += 1
      end
    else
      break
    end
  end
  return arr
end

def count_non_zeros(arr)
  count = 0
  for element in arr do
    count += 1 if !element.zero?
  end
  return count
end

def test
  puts "Input ([1, 0, 2, 0, 9, 8]) #{zeros_to_center([1, 0, 2, 0, 9, 8]) == [1,2,0,0,9,8] ? 
  "Pass" : "Fail"}"
  puts "Input ([0, 0, 2, 10, 9, 8, 0, 0, 10]) #{zeros_to_center([0, 0, 2, 10, 9, 8, 0, 0, 10]) == [2,10,0,0,0,0,9,8,10] ? "Pass" : "Fail"}"
end

