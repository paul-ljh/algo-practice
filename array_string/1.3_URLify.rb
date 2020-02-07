def URLify(str, len)
  return str if str.length == len
  
  num_space = (str.length - len) / 2
  sp_counter, result_counter = 0, str.length - 1

  (len - 1).downto(0) do |i|
    if str[i] == ' '
      break if sp_counter == num_space
      str[result_counter-2..result_counter] = "%20"
      result_counter -= 3
      sp_counter += 1
    else
      str[result_counter] = str[i]
      result_counter -= 1
    end
  end
  return str
end

def test
  puts "PAUL, 4 renders #{URLify("PAUL", 4)}"
  puts " PAUL     , 6 renders #{URLify(" PAUL     ", 6)}"
  puts "   , 1 renders #{URLify("   ", 1)}"
  puts " P A UL      , 7 renders #{URLify(" P A UL      ", 7)}"
end
      