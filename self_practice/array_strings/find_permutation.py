'''
Given a shorter string and a longer string, find all permutations of the shorter string in the longer string. Return the location of each permutation.
'''

'''
O(N) runtime where N = len(long)
'''
def find_permutation(short, long):
  result = []

  long_map = { c: 0 for c in short }
  short_map = { c: 0 for c in short }
  for c in short: short_map[c] += 1

  match_count = 0
  target_count = len(short_map)

  for i in range(len(short)):
    c = long[i]
    if c in long_map:
      long_map[c] += 1
      if long_map[c] == short_map[c]: match_count += 1

  if match_count == target_count:
    result.append(0)

  for i in range(len(short), len(long)):
    in_char, out_char = long[i], long[i - len(short)]
    if in_char != out_char:
      if out_char in long_map:
        if long_map[out_char] == short_map[out_char]:
          match_count -= 1
        elif long_map[out_char] == short_map[out_char] + 1:
          match_count += 1
        long_map[out_char] -= 1

      if in_char in long_map:
        if long_map[in_char] == short_map[in_char]:
          match_count -= 1
        elif long_map[in_char] == short_map[in_char] - 1:
          match_count += 1
        long_map[in_char] += 1

    if match_count == target_count:
      result.append(i - len(short) + 1)

  return result

def test():
  inputs = [
    ('abbc', 'cbabadcbbabbcbabaabccbabc'),
  ]

  outputs = [
    [0, 6, 9, 11, 12, 20, 21],
  ]

  for i in range(len(inputs)):
    print('PASS' if find_permutation(*inputs[i]) == outputs[i] else 'FAIL')

if __name__ == "__main__":
  test()
