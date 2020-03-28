load "#{Dir.home}/Documents/Interviews/algo-practice/stack.rb"

class Calculator
  attr_reader :result
  def initialize(eq)
    @eq = eq
    @num_stack, @op_stack = Stack.new, Stack.new
    @result = evaluate
  end
  
  def evaluate
    return 0 if @eq.empty?
    num = ''
    0.upto(@eq.size - 1) do |i|
      if /[[:digit:]]/.match?(@eq[i])
        num << @eq[i]
      else
        @num_stack.push(num.to_i)
        unless @op_stack.is_empty? || ((@eq[i] == '/' || @eq[i] == '*') && (@op_stack.peek == '+' || @op_stack.peek == '-'))
          consolidate
        end
        @op_stack.push(@eq[i])
        num = ''
      end
    end
    @num_stack.push(num.to_i)
  
    until @op_stack.is_empty? do
      consolidate
    end
    return @num_stack.pop
  end
  
  def consolidate
    sec_num, fir_num = @num_stack.pop, @num_stack.pop
    op = @op_stack.pop
    @num_stack.push(fir_num.send(op, sec_num))
  end
end


def test
  puts Calculator.new('').result == 0 ? 'PASS' : 'FAIL'
  puts Calculator.new('69').result == 69 ? 'PASS' : 'FAIL'
  puts Calculator.new('100-60+40').result == 80 ? 'PASS' : 'FAIL'
  puts Calculator.new('80/40*2').result == 4 ? 'PASS' : 'FAIL'
  puts Calculator.new('100/100-60+40*2/2*3/10+40').result == -7 ? 'PASS' : 'FAIL'
  puts Calculator.new('100/100*10+100/100*10+100/100*10+100/100*10').result == 40 ? 'PASS' : 'FAIL'
end
