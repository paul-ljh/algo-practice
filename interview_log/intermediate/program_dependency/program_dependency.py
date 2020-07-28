''' 
Google Japan 2020.4
You have N programs and want to run each of them exactly once. Each program takes exactly one hour to complete. You can run multiple programs in parallel, but some programs depend on the output from one or more other programs and thus can be run only after their completion. Given the dependency between programs, please compute the minimum number of hours you need to run all programs.

Input
Test cases will be provided in the following format, using only ASCII characters. The first line contains one integer, C, which is the number of test cases that will follow. The second line is blank. From third line onwards, multiple test cases separated by a blank line will follow. Each test case has the following format:

N M
A1 B1
A2 B2
…
AM BM

N is the number of programs you want to run, and M is the number of dependencies between programs. Each of the following M lines specifies one dependency; Ai-th program needs to be completed before you run Bi-th program.

All tokens in a line are separated by a single space.

Guarantees:
All numbers in the input are integers.
Number of test cases: 1 <= C <= 50
Number of programs: 1 <= N <= 20
Number of dependencies: 0 <= M <= N*(N-1)/2
1 <= Ai <= N, 1 <= Bi <= N
There is a way to run each program exactly once.
There is no circular dependency, that is, if i-th program depends on j-th program, j-th program does not depend on i-th program directly or indirectly.
No two dependencies are the same: (Ai, Bi) != (Aj, Bj) if i != j.

Note: You can assume that the input data is valid and satisfies all constraints. Your solution does not need to include error handling code.

Output
For each test case, output a result in the following format:

Case #k: H
where k is the number of the test case, starting from 1, and H indicates how many hours you need to run all programs.

All tokens in the output should be separated by a single space.
'''

def program_dependency():
  output = open("output_task2.txt", "w+")
  f = open("task2-test-input.txt", "r")
  total_test_cases = int(f.readline())
  
  for test_case_index in range(1, total_test_cases+1):
    # read the blank line before each test case
    f.readline()
    
    num_program, num_dependency = map(lambda input: int(input), f.readline().split(' '))
    dependencies = {}
    for i in range(1, num_program+1):
      dependencies[i] = set()
    
    for i in range(0, num_dependency):
      pre, post = map(lambda input: int(input), f.readline().split(' '))
      dependencies[post].add(pre)
        
    time = solve_dependency(dependencies)
    output.write(f"Case #{test_case_index}: {time}\n")
    
  f.close()
  output.close()
    
def solve_dependency(dependencies):
  if len(dependencies) == 0:
    return 0

  programs_to_run = set()
  for key in dependencies:
    if len(dependencies[key]) == 0:
      programs_to_run.add(key)
  
  for key in programs_to_run:    
    dependencies.pop(key)
  
  for key in dependencies:
    for program in programs_to_run:
      if program in dependencies[key]:
        dependencies[key].remove(program)
  
  return 1 + solve_dependency(dependencies)

if __name__ == '__main__':
  program_dependency()
