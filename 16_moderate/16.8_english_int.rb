def english_int(int)
  str_int = int.to_s()
  len = str_int.length
  quo, rem = len / 3, len % 3
  # limit to Quadrillion due to testing purposes
  zero_dict = {1 => "thousand", 2 => "million", 3 => "billion", 4 => "trillion", 5 => "quadrillion"}
  result = ""

  if rem != 0
    result << process_hundred(str_int.slice!(0..rem-1)) << ' ' << (zero_dict[quo]||'')
  end

  0.upto(quo-1) do |i|
    result << ' ' << process_hundred(str_int.slice!(0..2)) << ' ' << (zero_dict[quo-i-1]||'')
  end
  return result.strip()
end

def process_hundred(str)
  puts "ERROR" if str.empty?
  return '' if str == '00' || str == '000'

  one_word = {'0' => "zero", '1' => "one", '2' => "two", '3' => "three", '4' => "four", '5' => "five", '6' => "six", '7' => "seven", '8' => "eight", '9' => "nine", '10' => "ten", '11' => "eleven", '12' => "twelve", '13' => "thirteen", '14' => "fourteen", '15' => "fifteen", '16' => "sixteen", '17' => "seventeen", '18' => "eighteen", '19' => "nineteen", '20' => "twenty", '30' => "thirty", '40' => "forty", '50' => "fifty", '60' => "sixty", '70' => "seventy", '80' => "eighty", '90' => "ninty"}

  result = ""
  if str.length == 3
    result << one_word[str.slice!(0)] << " hundred"
  end
  return result if str == "00"
  
  str.slice!(0) if str[0] == '0' && str.length == 2
  if one_word.has_key?(str)
    result << ' ' << one_word[str]
  else
    result << ' ' << one_word[str[0] + '0'] << ' ' << one_word[str[-1]]
  end
  return result
end

def test
  puts "Input ('0') #{english_int(0) == "zero" ? "Pass" : "Fail"}"
  puts "Input ('2') #{english_int(2) == "two" ? "Pass" : "Fail"}"
  puts "Input ('10') #{english_int(10) == "ten" ? "Pass" : "Fail"}"
  puts "Input ('50') #{english_int(50) == "fifty" ? "Pass" : "Fail"}"
  puts "Input ('53') #{english_int(53) == "fifty three" ? "Pass" : "Fail"}"

  puts "Input ('100') #{english_int(100) == "one hundred" ? "Pass" : "Fail"}"
  puts "Input ('203') #{english_int(203) == "two hundred three" ? "Pass" : "Fail"}"
  puts "Input ('990') #{english_int(990) == "nine hundred ninty" ? "Pass" : "Fail"}"
  puts "Input ('132') #{english_int(132) == "one hundred thirty two" ? "Pass" : "Fail"}"
  
  puts "Input ('1000') #{english_int(1000) == "one thousand" ? "Pass" : "Fail"}"
  puts "Input ('1203') #{english_int(1203) == "one thousand two hundred three" ? "Pass" : "Fail"}"
  puts "Input ('1600') #{english_int(1600) == "one thousand six hundred" ? "Pass" : "Fail"}"
  puts "Input ('3333') #{english_int(3333) == "three thousand three hundred thirty three" ? "Pass" : "Fail"}"

  puts "Input ('1,400,330') #{english_int(1400330) == "one million four hundred thousand three hundred thirty" ? "Pass" : "Fail"}"

  puts "Input ('1,400,330,233') #{english_int(1400330233) == "one billion four hundred million three hundred thirty thousand two hundred thirty three" ? "Pass" : "Fail"}"

  puts "Input ('16,500,400,330,233') #{english_int(16500400330233) == "sixteen trillion five hundred billion four hundred million three hundred thirty thousand two hundred thirty three" ? "Pass" : "Fail"}"
end


