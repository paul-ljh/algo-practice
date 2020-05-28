=begin
Given an integer n, representing the length of a binary string a, which is all '0's in the beginning.

Also given operations, an array of strings, each representing an operation of the following 2 types:
1. 'L' - find the smallest index i, for which a[i] = '0' and set a[i] = '1'. If there is no such index, do nothing

2. 'C#{index}' - set a[index] = '0' regardless of the previous value of a[index]. Index is also guaranteed to be smaller than n.

Return a binary string after all operations have been applied.

=end

def boolean_queue(n, operations)
  reversed_result = 0b0
  for op in operations do
    if op[0] == 'C'
      op_index = op[1..-1].to_i
      # bit inverse then bit AND
      reversed_result &= (~(1 << op_index))
    elsif op == 'L'
      inversion = ~reversed_result
      two_complement = reversed_result + 1
      reversed_result |= (inversion & two_complement)
    end
  end
  return 0.upto(n-1).map { |i| reversed_result[i] }.join
end

=begin
Above algo is based on the following idea: 

Bit Operations: how to find first zero, least significant bit

1. Invert the number
2. Compute the two's complement of the inverted number
3. AND the results of (1) and (2)
3. Find the position by computing the binary logarithm of (3)

e.x.
For the number 10110111

1. 01001000
2. 10111000
3. 01001000 AND 10111000 = 00001000
4. log2(00001000) = 3

=end

def test
  puts "Input (1, ['L', 'L', 'L', 'L', 'L']) #{boolean_queue(1, ['L', 'L', 'L', 'L', 'L']) == '1' ? "Pass" : "Fail"}"
  puts "Input (1, ['C0', 'C0', 'C0', 'C0', 'C0']) #{boolean_queue(1, ['C0', 'C0', 'C0', 'C0', 'C0']) == '0' ? "Pass" : "Fail"}"
  puts "Input (4, ['L', 'L', 'L', 'L', 'L']) #{boolean_queue(4, ['L', 'L', 'L', 'L', 'L']) == '1111' ? "Pass" : "Fail"}"
  puts "Input (4, ['C0', 'C1', 'C2', 'C3', 'C1']) #{boolean_queue(4, ['C0', 'C1', 'C2', 'C3', 'C1']) == '0000' ? "Pass" : "Fail"}"

  puts "Input (4, ['L', 'L', 'L', 'C2']) #{boolean_queue(4, ['L', 'L', 'L', 'C2']) == '1100' ? "Pass" : "Fail"}"
  puts "Input (4, ['L', 'C0', 'L', 'C0', 'L', 'C0']) #{boolean_queue(4, ['L', 'C0', 'L', 'C0', 'L', 'C0']) == '0000' ? "Pass" : "Fail"}"
  puts "Input (4, ['C0', 'L', 'C0', 'L', 'C0', 'L']) #{boolean_queue(4, ['C0', 'L', 'C0', 'L', 'C0', 'L']) == '1000' ? "Pass" : "Fail"}"
end


