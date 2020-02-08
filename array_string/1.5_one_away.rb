def one_away(str1, str2)
  diff = (str1.length - str2.length).abs
  return false if diff >= 2

  action = diff == 1 ? 'rm' : 'rp'
  short = str1.length < str2.length ? str1 : str2
  long = str1.length < str2.length ? str2 : str1

  found_diff = false
  short_index, long_index = 0, 0
  while (short_index < short.length && long_index < long.length)
    if short[short_index] != long[long_index]
      return false if found_diff
      found_diff = true   
      short_index += 1 if action == 'rp'
    else
      short_index += 1 
    end
    long_index += 1
  end
  return true

  ## Alternative way
  # 0.upto(short.length-1) do |i|
  #   if short[i] != long[i]
  #     long[i] = short[i] if action == 'r'
  #     long.slice!(i) if action == 'i'
  #     return long == short
  #   end
  # end
  # return true
end

def test
  puts "EQUAL length"
  puts "('', '') renders #{one_away('', '')}"
  puts "('abb', 'abc') renders #{one_away('abb', 'abc')}"
  puts "('bbc', 'abc') renders #{one_away('bbc', 'abc')}"
  puts "('abbc', 'aabc') renders #{one_away('abbc', 'aabc')}"
  
  puts "('abbcc', 'aabxc') renders #{one_away('abbcc', 'aabxc')}"
  puts "('abbcc', 'bbbcb') renders #{one_away('abbcc', 'bbbcb')}"

  puts "DIFFER by 1"
  puts "(' ', '') renders #{one_away(" ", "")}"
  puts "('ale', 'pale') renders #{one_away("ale", "pale")}"
  puts "('ple', 'pale') renders #{one_away("ple", "pale")}"
  puts "('paul', 'paula') renders #{one_away("paul", "paula")}"
  puts "('paul', 'apaul') renders #{one_away("paul", "apaul")}"

  puts "('paal', 'paula') renders #{one_away("paal", "paula")}"
  puts "('paul', 'paulab') renders #{one_away("paul", "paulab")}"
  puts "('paul', 'abpaul') renders #{one_away("paul", "abpaul")}"
end
