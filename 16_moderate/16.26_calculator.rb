def calculator(str)
  return 0 if str.empty?
  add_or_sub(str, str.size-1)
end

def add_or_sub(str, index)
  i = index
  loop do
    break if str[i] == '+' || str[i] == '-'
    break if i.zero?
    i -= 1
  end
  if i.zero?
    return div_or_mult(str[i..index], index-i)
  else
    return add_or_sub(str, i-1).send(str[i], div_or_mult(str[i+1..index], index-i-1))
  end
end

def div_or_mult(str, index)
  i = index
  loop do
    break if str[i] == '/' || str[i] == '*'
    break if i.zero?
    i -= 1
  end
  if i.zero?
    return str[0..index].to_i
  else
    return div_or_mult(str, i-1).send(str[i], str[i+1..index].to_i)
  end
end

def test
  e1 = "785"
  e2 = "22+45+10"
  e3 = "6-9-10"
  e4 = "34-67+45"

  e5 = "1+2-3"
  e6 = "16*10"
  e7 = "68/34"
  e8 = "30*2/3"

  e9 = "10+30/2*10-90+10"
  e10 = "10*10+30/2*10-90+10"

  puts "e1: #{calculator(e1) == 785 ? 'Pass' : 'Fail'}"
  puts "e2: #{calculator(e2) == 77 ? 'Pass' : 'Fail'}"
  puts "e3: #{calculator(e3) == -13 ? 'Pass' : 'Fail'}"
  puts "e4: #{calculator(e4) == 12 ? 'Pass' : 'Fail'}"
  puts "e5: #{calculator(e5) == 0 ? 'Pass' : 'Fail'}"
  puts "e6: #{calculator(e6) == 160 ? 'Pass' : 'Fail'}"
  puts "e7: #{calculator(e7) == 2 ? 'Pass' : 'Fail'}"
  puts "e8: #{calculator(e8) == 20 ? 'Pass' : 'Fail'}"
  puts "e9: #{calculator(e9) == 80 ? 'Pass' : 'Fail'}"
  puts "e10: #{calculator(e10) == 170 ? 'Pass' : 'Fail'}"
end
