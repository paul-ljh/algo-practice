require './3_stack'

def sort_stack(s)
  return s if s.is_empty?
  tmp_s = s
  tmp = Stack.new
  while !tmp_s.is_empty? do
    item = tmp_s.pop
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
