'''
Test cases will be provided in the following multiline text format, using only ASCII characters.

The first line contains one integer, C, which is the number of test cases that will follow. The second line is blank. The test cases will follow starting from the third line, with a blank line between test cases.

Each test case has the following format.

N
A[1] B[1]
A[2] B[2]
…
A[N] B[N]

N is the number of sleep intervals. A[i] is the time of falling-asleep of the i-th sleep interval in 24-hour clock format (hh:mm). B[i] is the time of waking-up of the i-th sleep interval in 24-hour clock format.

All tokens in a line are separated by a single space.

For each test case, output the result in the following format:

Case #k: W S
where k is the index of the test case, starting from 1, W is the total waking time in minutes, and S is the total sleeping time in minutes.

Example
Suppose an input is as follows.

1

3
05:00 06:00
20:00 08:30
01:00 01:30

The first line means there is one test case.

The first line in the test case means there were three periods of sleep.

The hamster slept for one hour, from 5:00 until 6:00.
After that, it was awake for 14 hours, until 20:00.
It then slept until 8:30, which is 12 hours 30 minutes of sleep. (Note that the hamster will never sleep for longer than 18 hours, and thus it’s 8:30 in the second day).
It was then awake for 16 hours 30 minutes, until 1:00. (Note that the hamster will not stay awake for longer than 18 hours, and thus it’s 1:00 in the third day).
Finally it slept for 30 minutes, until 1:30.

The total waking time is: 14 hours + 16 hours 30 minutes = 30 hours 30 minutes (1830 minutes).

The total sleeping time is: 1 hour + 12 hours 30 minutes + 30 minutes = 14 hours (840 minutes).

Limits:
Number of test cases: 1 <= C <= 30
Number of sleeps: 2 <= N <= 60
The hamster sleeps for at least 1 minute and at most 18 hours.
The hamster stays awake for at least 1 minute and at most 18 hours.
Note: You can assume that the input data is valid and satisfies all constraints. Your solution does not need to include error handling code.
'''

from datetime import timedelta

def hamster_sleep_time():
  output = open("output_hamster.txt", "w+")
  f = open("task1_test_data.input.txt", "r")
  total_test_cases = int(f.readline())
  
  for test_case_index in range(1, total_test_cases+1):
    # read the blank line before test case
    f.readline()
    
    num_period = int(f.readline())
    
    sleep, wake = 0, 0
    d_prev_wake = None
    
    for i in range(0, num_period):
      # EX: ['05:00', '06:00']
      interval = f.readline().split(' ')
      
      # EX: [['05', '00'], ['06', '00']]
      sleep_time, wake_time = map(lambda time: time.split(':'), interval)
      
      sleep_hour, sleep_min = sleep_time
      wake_hour, wake_min = wake_time
      
      d_sleep = timedelta(hours=int(sleep_hour), minutes=int(sleep_min))
      d_wake = timedelta(hours=int(wake_hour), minutes=int(wake_min))
      
      if d_prev_wake is not None:
        wake += (d_sleep - d_prev_wake).seconds // 60
      sleep += (d_wake - d_sleep).seconds // 60
      
      d_prev_wake = d_wake
    
    output.write(f"Case #{test_case_index}: {wake} {sleep}\n")
    
  f.close()
  output.close()

if __name__ == '__main__':
  hamster_sleep_time()

