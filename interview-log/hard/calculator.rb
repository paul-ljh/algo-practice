=begin

You are building an educational website and want to create a simple calculator for students to use. The calculator will only allow addition and subtraction of non-negative integers.

We also want to allow parentheses in our input. Given an expression string using the "+", "-", "(", and ")" operators like "5+(16-2)", write a function to parse the string and evaluate the result.

Sample output:
  calculate("5+16-((9-6)-(4-2))+1") => 21
  calculate("22+(2-4)") => 20
  calculate("6+9-12") => 3
  calculate("((1024))") => 1024
  calculate("1+(2+3)-(4-5)+6") => 13
  calculate("255") => 255

=end

def calculate(str)
  op_index = -1
  bracket_balance, has_bracket = 0, false
  
  (str.length - 1).downto(0) do |i|
    if str[i] == '('
      bracket_balance += 1
    elsif str[i] == ')'
      bracket_balance -= 1
      has_bracket = true
    elsif bracket_balance.zero? && (str[i] == '+' || str[i] == '-')
      op_index = i
      break
    end
  end

  if op_index == -1
    if has_bracket
      return calculate(str[1..-2])
    else
      return str[0..op_index].to_i
    end
  else
    if str[op_index] == '+'
      if has_bracket
        return calculate(str[0..op_index-1]) + calculate(str[op_index+2..-2])
      else
        return calculate(str[0..op_index-1]) + str[op_index+1..-1].to_i
      end
    else
      if has_bracket
        return calculate(str[0..op_index-1]) - calculate(str[op_index+2..-2])
      else
        return calculate(str[0..op_index-1]) - str[op_index+1..-1].to_i
      end
    end
  end
end

def test
  expression_1 = "5+16-((9-6)-(4-2))+1" #21
  expression_2 = "22+(2-4)" #20
  expression_3 = "6+9-12" #3
  expression_4 = "((1024))" #1024
  expression_5 = "1+(2+3)-(4-5)+(6)" #13
  expression_6 = "255"
  expression_7 = "5+16-(((9-6)+(4-2)))+1" #17

  puts calculate(expression_1)
  puts calculate(expression_2)
  puts calculate(expression_3)
  puts calculate(expression_4)
  puts calculate(expression_5)
  puts calculate(expression_6)
  puts calculate(expression_7)
end
