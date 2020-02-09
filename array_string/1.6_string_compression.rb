def should_compress?(str)
  return false if str.empty?
  prv_ltr = str[0]
  clen, counter = 0, 1
  1.upto(str.length - 1) do |i|
    if str[i] != prv_ltr
      clen += (counter.to_s.length + 1)
      prv_ltr = str[i]
    else
      counter += 1
    end
  end
  return str.length > clen + counter.to_s.length + 1
end

def string_compression(str)
  return str unless should_compress?(str)
  prv_ltr, counter = str[0], 1
  result = ''
  1.upto(str.length - 1) do |i|
    if str[i] != prv_ltr
      result << prv_ltr << counter.to_s
      prv_ltr, counter = str[i], 1
    else
      counter += 1
    end
  end
  return result << prv_ltr << counter.to_s
end

def test
  puts "TESTING should_compress?"
  puts "Input ('abc') #{should_compress?("abc") == false ? "Pass" : "Fail"}"
  puts "Input ('abbc') #{should_compress?("abbc") == false ? "Pass" : "Fail"}"
  puts "Input ('aabbcc') #{should_compress?("aabbcc") == false ? "Pass" : "Fail"}"
  puts "Input ('caabbcc') #{should_compress?("caabbcc") == false ? "Pass" : "Fail"}"
  puts "\n"
  puts "Input ('aabbbcc') #{should_compress?("aabbbcc") == true ? "Pass" : "Fail"}"
  puts "Input ('aabbbcccd') #{should_compress?("aabbbcccd") == true ? "Pass" : "Fail"}"
  puts "Input ('aabbbbbbbbbbcccd') #{should_compress?("aabbbbbbbbbbcccd") == true ? "Pass" : "Fail"}"
  
  puts "\n"
  puts "\n"
  puts "TESTING string_compression"
  puts "Input ('aabbbcc') #{string_compression("aabbbcc") == "a2b3c2" ? "Pass" : "Fail"}"
  puts "Input ('aabbbcccd') #{string_compression("aabbbcccd") == "a2b3c3d1" ? "Pass" : "Fail"}"
  puts "Input ('abbbbbbbbbbcdde') #{string_compression("abbbbbbbbbbcdde") == "a1b10c1d2e1" ? "Pass" : "Fail"}"
end
