'''
A company calculates an integer score for each of its employees, equal to: 
  The total number of direct and indirect reports under the employee, plus 1.
  
Assume:
1. Each employee has a unique eid
2. An employee with no employees reporting to them has a score of 1.

The input is a valid direct report map, key is eid, the value is an array of eids who directly report to the key. The map contains all employees.

Write a function that calculates scores for all employees.
'''

def calculate_score(eid, score_map, employee_map):
  if eid in score_map:
    return score_map[eid]
  if len(employee_map[eid]) == 0:
    score_map[eid] = 1
    return 1

  count = 1
  for employee in employee_map[eid]:
    count += calculate_score(employee, score_map, employee_map)
  score_map[eid] = count
  return count

def calculate_all_scores(employee_map):
  score_map = {}
  for eid in employee_map.keys():
    calculate_score(eid, score_map, employee_map)
  return score_map

def test():
  m = {
    3: [],
    4: [],
    7: [6],
    6: [],
    1: [2,3],
    2: [4,7],
  }
  print('PASS' if calculate_all_scores(m) == {3:1, 4:1, 7:2, 6:1, 1:6, 2:4} else 'FAIL')

if __name__ == '__main__':
  test()
   
  


