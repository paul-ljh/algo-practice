'''
https://leetcode.com/problems/h-index/
'''

def h_index(citations):
  citations.sort()
  for i in reversed(range(len(citations))):
    h_candidate = len(citations) - i
    if h_candidate > citations[i]:
      return h_candidate - 1
  return len(citations)

def test():
  sample_data = [
    ([], 0),
    ([0], 0),
    ([1], 1),
    ([1,3,1], 1),
    ([4,5,6], 3),
    ([3,0,6,1,5], 3),
  ]
  for (input, output) in sample_data:
    print('PASS' if h_index(input) == output else 'FAIL')

if __name__ == "__main__":
  test()
