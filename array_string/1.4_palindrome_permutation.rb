def palindrome_permutation(str)
  return true if str.length <= 1
  occur = Hash.new(0)
  str.each_char do |letter|
    occur[letter] = (occur[letter] + 1) % 2
  end
  return occur.values.sum <= 1
end

def test
  puts "('') renders #{palindrome_permutation('')}"
  puts "(' ') renders #{palindrome_permutation(" ")}"
  puts "('abccbb') renders #{palindrome_permutation("abccbb")}"
  puts "('abccbb&h') renders #{palindrome_permutation("abccbb&h")}"
  puts "('cbaaaac') renders #{palindrome_permutation("cbaaaac")}"
  puts "('abaccbcc') renders #{palindrome_permutation("abaccbcc")}"
end

def alternative_palindrome_permutation(str)
  return true if str.length <= 1
  occur = 0
  str.each_char do |letter|
    current = 1 << letter.ord
    occur ^= current
  end

  # a hack to detect whether one integer has exactly one 1's in its binary representation
  # EX: 00010000 - 1 = 00001111
  #     00010000 & 00001111 = 0
  return (occur - 1) & occur == 0
end

def test
  puts "('') renders #{alternative_palindrome_permutation('')}"
  puts "(' ') renders #{alternative_palindrome_permutation(" ")}"
  puts "('abccbb') renders #{alternative_palindrome_permutation("abccbb")}"
  puts "('abccbb&h') renders #{alternative_palindrome_permutation("abccbb&h")}"
  puts "('cbaaaac') renders #{alternative_palindrome_permutation("cbaaaac")}"
  puts "('abaccbcc') renders #{alternative_palindrome_permutation("abaccbcc")}"
end
