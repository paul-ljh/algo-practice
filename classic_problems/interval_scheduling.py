'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Input: [(1,2),(2,3),(3,4),(1,3)]
Output: 1
Explanation: (1,3) can be removed and the rest of intervals are non-overlapping.
'''

from sys import maxsize

def interval_scheduling(intervals):
  intervals.sort(key=lambda inter: inter[0])
  length = len(intervals)
  cache = [0] * length
  for i in range(length):
    max_so_far = 0
    for j in range(i):
      if intervals[j][1] <= intervals[i][0] and max_so_far < cache[j]:
        max_so_far = cache[j]
    cache[i] = max_so_far+1
  return length - max(cache, default=0)    

def better_interval_scheduling(intervals):
  intervals.sort(key=lambda inter: inter[0])
  cache = [-maxsize-1]
  for start,end in intervals:
    best_len = find_max(start, cache)
    if best_len == len(cache)-1:
      cache.append(end)
    else:
      cache[best_len+1] = min(end, cache[best_len+1])
  return len(intervals) - (len(cache)-1)

def find_max(target, cache):
  left, right = 0, len(cache)-1
  best = -maxsize-1
  while right >= left:
    mid = (right+left) // 2
    if target >= cache[mid]:
      left = mid+1
      best = mid
    else:
      right = mid-1
  return best

def greedy_interval_scheduling(intervals):
  intervals.sort(key=lambda inter: inter[1])
  count, latest_finish_time = 0, -maxsize-1
  length = len(intervals)
  for i in range(length):
    if intervals[i][0] >= latest_finish_time:
      count += 1
      latest_finish_time = intervals[i][1]
  return length - count

def test():
  intervals = []
  answer = 0
  print('PASS' if (greedy_interval_scheduling(intervals)
                   == better_interval_scheduling(intervals)
                   == interval_scheduling(intervals)
                   == answer) else 'FAIL')
  
  intervals = [(1,3)]
  answer = 0
  print('PASS' if (greedy_interval_scheduling(intervals)
                   == better_interval_scheduling(intervals)
                   == interval_scheduling(intervals)
                   == answer) else 'FAIL')
  
  intervals = [(1,4), (1,6), (2,4), (3,5)]
  answer = 3
  print('PASS' if (greedy_interval_scheduling(intervals)
                   == better_interval_scheduling(intervals)
                   == interval_scheduling(intervals)
                   == answer) else 'FAIL')
  
  intervals = [(1,2),(2,3),(3,4),(1,3)]
  answer = 1
  print('PASS' if (greedy_interval_scheduling(intervals)
                   == better_interval_scheduling(intervals)
                   == interval_scheduling(intervals)
                   == answer) else 'FAIL')
  
  intervals = [(1,2),(1,2),(1,2),(1,3)]
  answer = 3
  print('PASS' if (greedy_interval_scheduling(intervals)
                   == better_interval_scheduling(intervals)
                   == interval_scheduling(intervals)
                   == answer) else 'FAIL')

  intervals = [(3,4), (1,2), (8,11), (10,12), (5,9), (7,10)]
  answer = 2
  print('PASS' if (greedy_interval_scheduling(intervals)
                   == better_interval_scheduling(intervals)
                   == interval_scheduling(intervals)
                   == answer) else 'FAIL')
  
  intervals = [(1,1), (1,2), (2,3), (2,5), (2,3), (3,4)]
  answer = 2
  print('PASS' if (greedy_interval_scheduling(intervals)
                   == better_interval_scheduling(intervals)
                   == interval_scheduling(intervals)
                   == answer) else 'FAIL')

if __name__ == "__main__":
  test()
