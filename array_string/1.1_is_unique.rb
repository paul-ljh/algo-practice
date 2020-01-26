def is_unique(str)
  return true if str.empty?
  accum = 0
  str.each_byte { |char|
    cur = 1 << char.ord
    if cur & accum == cur
      return false
    else
      accum |= cur
    end
  }
  return true
end
