def missing_number(arr)
  return find_missing(arr, 0, arr.length.to_s(2).length)
end

def find_missing(arr, i, n)
  if i >= n 
    return 0
  end

  one, zero = [], []
  for bin in arr do
    if i < bin.length && bin[bin.length - 1 - i] == '1'
      one.push(bin)
    else
      zero.push(bin)
    end
  end

  if one.length < zero.length
    v = find_missing(one, i+1, n)
    return v << 1 | 1
  else
    v = find_missing(zero, i+1, n)
    return v << 1 | 0
  end
end

def test
  puts "Input ('[1]') #{missing_number(['1']) == 0 ? "Pass" : "Fail"}"
  puts "Input ('[0]') #{missing_number(['0']) == 1 ? "Pass" : "Fail"}"
  puts "Input ('[0, 10]') #{missing_number(['0', '10']) == 1 ? "Pass" : "Fail"}"
  puts "Input ('[0, 1, 10]') #{missing_number(['0', '1', '10']) == 3 ? "Pass" : "Fail"}"
  puts "Input ('[0, 10, 1, 11, 111, 100, 101]') #{missing_number(['0', '10', '1', '11', '111', '100', '101']) == 6 ? "Pass" : "Fail"}"
  puts "Input ('[0, 10, 1, 11, 110, 100, 101]') #{missing_number(['0', '10', '1', '11', '110', '100', '101']) == 7 ? "Pass" : "Fail"}"
  puts "Input ('[0, 10, 1, 11, 110, 100, 101, 111, 1000, 1110, 1010, 1001, 1100, 1111, 1011]') #{missing_number(['0', '10', '1', '11', '110', '100', '101', '111', '1000', '1110', '1010', '1001', '1100', '1111', '1011']) == 13 ? "Pass" : "Fail"}"
  puts "Input ('[0, 10, 1, 11, 110, 100, 101, 111, 1000, 1110, 1010, 1001, 1100, 1101, 1011]') #{missing_number(['0', '10', '1', '11', '110', '100', '101', '111', '1000', '1110', '1010', '1001', '1100', '1101', '1011']) == 15 ? "Pass" : "Fail"}"
end
