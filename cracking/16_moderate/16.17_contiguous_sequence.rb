# Note the following algo is designed based on the premise that sequence can be of length 1
def contiguous_sequence(arr)
  return nil if arr.length == 0
  return arr[0] if arr.length == 1

  max_sum, running_sum = arr[0], arr[0]
  1.upto(arr.length - 1) do |i|
    max_sum = arr[i] if arr[i] > max_sum
    if running_sum + arr[i] < 0
      running_sum = arr[i]
    else
      running_sum += arr[i]
      max_sum = running_sum if running_sum > max_sum
    end
  end
  return max_sum
end

def test
  puts "Input ('[3,3,3]') #{contiguous_sequence([3,3,3]) == 9 ? "Pass" : "Fail"}"
  puts "Input ('[-10,-2,-1,-9]') #{contiguous_sequence([-10,-2,-1,-9]) == -1 ? "Pass" : "Fail"}"
  puts "Input ('[3,-2,1,-10,1,-1,15]') #{contiguous_sequence([3,-2,1,-10,1,-1,15]) == 15 ? "Pass" : "Fail"}"
  puts "Input ('[3,-2,3,-2,4,-10]') #{contiguous_sequence([3,-2,3,-2,4,-10]) == 6 ? "Pass" : "Fail"}"
end


