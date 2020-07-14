def xml_encoding(xml, mapping):
  result = []
  in_attribute = in_value = False
  i = 0
  while i < len(xml):
    curr_char = xml[i]
    # Tag
    if not in_attribute and not in_value:
      if curr_char == '<':
        next_i = min(xml.find(' ', i), xml.find('>', i))
        if xml[i+1] == '/':
          result.append(0)
        else:
          tag = xml[i+1:next_i]
          result.append(mapping[tag])
          in_attribute = True
        i = next_i-1
      else:
        i += 1
       
    # > or attribute name 
    elif in_attribute and not in_value:
      if curr_char == ' ':
        next_i = xml.find('=', i)
        attr_name = xml[i+1:next_i]
        result.append(mapping[attr_name])
        in_value = True
        i = next_i + 2
      elif curr_char == '>':
        in_attribute = False
        in_value = True
        i += 1
      else:
        i += 1
    
    # attribute value
    elif in_attribute and in_value:
      next_i = xml.find('\"', i)
      attr_value = xml[i:next_i]
      result.append(attr_value)
      i = next_i
      in_value = False
     
    # text between tags 
    elif not in_attribute and in_value:
      next_i = xml.find('<', i)
      str_value = xml[i:next_i].strip()
      if str_value != '':
        result.append(str_value)
      i = next_i - 1
      in_value = False
  
  return result

def test():
  mapping = {"family":1, "person":2, "firstName":3, "lastName":4, "state":5}
  
  xml = '''
  <family lastName="Li=" state="ON">
    TEST
    <person> Some   </person>
    <person firstName="Paul"></person>
  </family>
  '''
  answer = [1, 4, 'Li=', 5, 'ON', 'TEST', 2, 'Some', 0, 2, 3, 'Paul', 0, 0]
  print('PASS' if xml_encoding(xml, mapping) == answer else 'FAIL')
  
  xml = ''' \n   '''
  answer = []
  print('PASS' if xml_encoding(xml, mapping) == answer else 'FAIL')

if __name__ == "__main__":
  test()
         
