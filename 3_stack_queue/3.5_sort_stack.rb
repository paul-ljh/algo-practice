require '../3_stack'

def sort_stack(s)
  return s if s.is_empty?
  tmp = Stack.new
  while !s.is_empty? do
    item = s.pop
    iterative_insert(item, tmp)
  end
  return tmp
end

def iterative_insert(item, tmp)
  if tmp.is_empty? || item <= tmp.peek
    tmp.push(item)
    return tmp
  else
    tmp_pop_item = tmp.pop
    new_tmp = iterative_insert(item, tmp)
    new_tmp.push(tmp_pop_item)
    return new_tmp
  end
end
