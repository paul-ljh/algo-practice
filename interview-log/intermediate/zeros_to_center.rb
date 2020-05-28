=begin

Given an array of numbers, move all zeros to the center of the array. Nonzero elements in the array should retain their relative positions. 

For the purpose of this question, the centre is floor(array.length/2)

=end

def zeros_to_center(arr)
  return arr if arr.empty?
  move_zeros_to_tail(arr, 0, arr.size/2)
  move_zeros_to_front(arr, arr.size-1, arr.size/2+1)
  return arr
end

def move_zeros_to_tail(arr, head, tail)
  return arr if arr.empty?
  zeros_index = nil
  head.upto(tail) do |index|
    if arr[index].zero? && zeros_index.nil?
      zeros_index = index
    elsif !arr[index].zero? && !zeros_index.nil?
      tmp = arr[index]
      arr[index] = arr[zeros_index]
      arr[zeros_index] = tmp
      zeros_index += 1
    end
  end
end

def move_zeros_to_front(arr, head, tail)
  return arr if arr.empty?
  zeros_index = nil
  head.downto(tail) do |index|
    if arr[index].zero? && zeros_index.nil?
      zeros_index = index
    elsif !arr[index].zero? && !zeros_index.nil?
      tmp = arr[index]
      arr[index] = arr[zeros_index]
      arr[zeros_index] = tmp
      zeros_index -= 1
    end
  end
end 

def test
  puts zeros_to_center([0,0,0,0,0,0]) == [0,0,0,0,0,0] ? "Pass" : "Fail"
  puts zeros_to_center([1,2,3,4,5,6]) == [1,2,3,4,5,6] ? "Pass" : "Fail"
  puts zeros_to_center([1,0,2,0,9,8]) == [1,2,0,0,9,8] ? "Pass" : "Fail"
  puts zeros_to_center([0,2,0,5,0,10,9,0,8,0,0,10]) == [2,5,10,9,0,0,0,0,0,0,8,10] ? "Pass" : "Fail"
end

