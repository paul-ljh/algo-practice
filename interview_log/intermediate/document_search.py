'''
Google Japan, Software Engineer New Grad, 2020 June

You are given a String document and a String search_term, as well as a transliteration table. Find whether the search_term is present in the document.

The transliteration table is a map from non-English character to English string, for example:
è -> e
é -> e
û -> u
æ -> ae
…

Example 1:
document: "I love crème brûlée"
search_term: "eme"
output: true

Example 2:
document: "I love crème brûlée"
search_term: "ème"
output: true

Example 3:
document: "Ole Gunnar Solskjær is amazing"
search_term: "Solskjae"
output: true

Example 4:
document: "Ole Gunnar Solskjær is amazing"
search_term: "Solskjear"
output: false
'''

def document_search(document, search_term, table):
  if not document and not search_term:
    return True
  if not document or not search_term:
    return False
  for i in range(len(document) - len(search_term) + 1):
    if match_term(document, search_term, table, i):
      return True
  return False

def match_term(document, search_term, table, document_index):
  search_i = 0
  while search_i < len(search_term):
    curr_char_search = search_term[search_i]
    curr_char_docu = document[document_index]
    if is_english_alpha(curr_char_docu) == is_english_alpha(curr_char_search):
      if curr_char_docu != curr_char_search:
        return False
    elif not is_english_alpha(curr_char_docu):
      eng_str = table.get(curr_char_docu, None)
      if (not eng_str
          or search_i + len(eng_str) > len(search_term)
          or eng_str != search_term[search_i : search_i + len(eng_str)]):
            return False
      search_i += len(eng_str) - 1
    else:
      eng_str = table.get(curr_char_search, None)
      if (not eng_str
          or document_index + len(eng_str) > len(document)
          or eng_str != document[document_index : document_index + len(eng_str)]):
            return False
      document_index += len(eng_str) - 1

    search_i += 1
    document_index += 1
  return True

def is_english_alpha(letter):
  return ord(letter) in range(ord('a'), ord('z')+1)

def test():
  table = {
    'è': 'e',
    'é': 'e',
    'û': 'u',
    'æ': 'ae',
  }
  
  document = "èm"
  search_term = "eme"
  result = False
  print('PASS' if document_search(document, search_term, table) == result else 'FAIL')
  
  document = "I love crème brûlée"
  search_term = "eme"
  result = True
  print('PASS' if document_search(document, search_term, table) == result else 'FAIL')

  document = "I love crème brûlée"
  search_term = "ème"
  result = True
  print('PASS' if document_search(document, search_term, table) == result else 'FAIL')

  document = "Ole Gunnar Solskjær is amazing"
  search_term = "Solskjae"
  result = True
  print('PASS' if document_search(document, search_term, table) == result else 'FAIL')
  
  document = "Ole Gunnar Solskjaer is amazing"
  search_term = "Solskjær"
  result = True
  print('PASS' if document_search(document, search_term, table) == result else 'FAIL')

  document = "Ole Gunnar Solskjær is amazing"
  search_term = "Solskjear"
  result = False
  print('PASS' if document_search(document, search_term, table) == result else 'FAIL')
  
  document = "Ole Gunnar Solskjær! is amazing"
  search_term = "Solskjaer! "
  result = True
  print('PASS' if document_search(document, search_term, table) == result else 'FAIL')


if __name__ == "__main__":
  test()
