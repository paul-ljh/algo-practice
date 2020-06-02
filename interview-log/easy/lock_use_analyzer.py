'''
We want to monitor how locks are used in a system. The lock log is documented in the following format:
  (A, X)
  (R, X)
  where x is some integer ID of the lock
  
All locks must be released in the reverse order of acquiring them.

It's prohibited to
1. leave locks acquired after termination
2. acquire an already acquired lock
3. release a yet acquired lock

Write a program that returns:
- 0, if there is no problem whatsoever
- N+1, if the only issue after program termination were dangling acquired locks, where N == len(events)
- K, in case event number K violated any of the principles.
'''

def lock_use_analyzer(events):
  active_locks, lock_stack = set(), []
  for i in range(len(events)):
    action, lock_num = events[i]
    if action == 'A':
      if lock_num in active_locks:
        return i+1
      else:
        active_locks.add(lock_num)
        lock_stack.append(lock_num)
    else:
      if len(lock_stack) == 0 or lock_num != lock_stack[-1]:
        return i+1
      else:
        lock_stack.pop()
        active_locks.remove(lock_num)
  return 0 if len(lock_stack) == 0 else len(events) + 1

def test():
  events = []
  print('PASS' if lock_use_analyzer(events) == 0 else 'FAIL')
  
  events = [('A', 5), ('R', 5), ('A', 5), ('R', 5), ('A', 4), ('A', 3), ('R', 3), ('R', 4)]
  print('PASS' if lock_use_analyzer(events) == 0 else 'FAIL')
  
  events = [('A', 5)]
  print('PASS' if lock_use_analyzer(events) == 2 else 'FAIL')
  
  events = [('R', 5)]
  print('PASS' if lock_use_analyzer(events) == 1 else 'FAIL')
  
  events = [('A', 5), ('R', 4)]
  print('PASS' if lock_use_analyzer(events) == 2 else 'FAIL')
  
  events = [('A', 5), ('R', 5), ('A', 5)]
  print('PASS' if lock_use_analyzer(events) == 4 else 'FAIL')
  
  events = [('A', 5), ('A', 5)]
  print('PASS' if lock_use_analyzer(events) == 2 else 'FAIL')

if __name__ == '__main__':
  test()
