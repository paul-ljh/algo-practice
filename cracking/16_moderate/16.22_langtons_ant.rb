require 'set'

def langtons_ant(k)
  direction, x, y = 1, k/2, k/2
  row = Hash.new
  0.upto(k-1) do |i|
    row[y] = Set.new if !row.has_key?(y)
    if row[y].include?(x)
      row[y].delete(x)
      # row.delete(x) if row[y].empty?
      direction = direction == 0 ? 3 : direction - 1
    else
      row[y].add(x)
      direction = (direction + 1) % 4
    end
  
    if direction == 1
      x += 1
    elsif direction == 2
      y += 1
    elsif direction == 3
      x -= 1
    else
      y -= 1
    end
  end
  print_k_moves(row, k)
end

def print_k_moves(row, k)
  0.upto(k) do |r|
    # next if !row.has_key?(r)
    0.upto(k) do |c|
      print "#{row.has_key?(r) && row[r].include?(c) ? 'x' : '.'}"
      $stdout.flush
    end
    puts "\n"
  end
end

def test
  1.upto(20) do |i|
    langtons_ant(i)
    puts "\n\n"
  end
end


