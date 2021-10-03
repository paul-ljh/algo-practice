def living_people(l, base_year):
  years, max_birth = build_year_counts(l, base_year)
  return find_max_count(years, max_birth, base_year)
  
def build_year_counts(l, base_year):
  result = []
  max_birth = 0
  for birth, death in l:
    if birth > max_birth:
      max_birth = birth
    add_to_years(result, birth, base_year, 1)
    add_to_years(result, death+1, base_year, -1)
  return (result, max_birth)
  
def add_to_years(r, year, base_year, increase):
  if len(r) > year-base_year:
    r[year-base_year] += increase
  else:
    r.extend([0] * (year-base_year-len(r)+1))
    r[-1] += increase

def find_max_count(years, max_birth, base_year):
  count, max_count, max_year = 0, 0, 0
  for i in range(max_birth-base_year+1):
    count += years[i]
    if count > max_count:
      max_count = count
      max_year = i
  return max_year + base_year

def test():
  base_year = 1900
  people = [(1908,1908),(1920,1940),(1905,1918),(1907,1922),(1911,1914),(1908,1920),(1900,1918)]
  print('PASS' if living_people(people, base_year) == 1908 else 'FAIL')
  
  people = [(1908,1908),(1908,1908),(1908,1908),(1908,1908),(1908,1908),(1908,1908),(1908,1908), (1901,1901)]
  print('PASS' if living_people(people, base_year) == 1908 else 'FAIL')

if __name__ == '__main__':
    test()
