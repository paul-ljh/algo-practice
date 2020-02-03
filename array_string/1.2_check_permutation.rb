def check_permutation(s1, s2)
  return true if s1 == s2
  return false if s1.length != s2.length

  occur = Hash.new(0)
  s1.each_char do |letter|
    occur[letter] += 1
  end

  s2.each_char do |letter|
    occur[letter] -= 1 if occur.has_key?(letter)
  end
  return all_zero?(occur.values)
end

def all_zero?(arr)
  arr.each do |item|
    return false if item != 0
  end
  return true
end

def test
  puts "input &tT and &Tt renders #{check_permutation("&tT", "&Tt")}"
  puts "input    and    renders #{check_permutation("  ", "  ")}"
  puts "input CAD and cad renders #{check_permutation("CAD", "cad")}"
  puts "input ccd and cd renders #{check_permutation("ccd", "cd")}"
  puts "input 2123 and 3221 renders #{check_permutation("2123", "3221")}"
  puts "input 1111 and 1111 renders #{check_permutation("1111", "1111")}"
  puts "input 1111 and 111 renders #{check_permutation("1111", "111")}"
end

