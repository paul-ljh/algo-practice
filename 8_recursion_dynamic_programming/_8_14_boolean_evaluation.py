def count_eval(exp, left, right, cache):
  if left == right: return (0,0)
  if left + 1 == right:
    boolean = int(exp[left])
    return (boolean, boolean ^ 1)
  if exp[left:right] in cache:
    return cache[exp[left:right]]
  
  t_ways, f_ways = 0, 0
  for i in range(left+1, right, 2):
    left_t, left_f = count_eval(exp, left, i, cache)
    right_t, right_f = count_eval(exp, i+1, right, cache)
    op = exp[i]
    
    true_evals = 0
    if op == '&':
      true_evals = left_t * right_t
    elif op == '|':
      true_evals = left_t * right_t + left_f * right_t + left_t * right_f
    else:
      true_evals = left_f * right_t + left_t * right_f
    
    total_evals = (left_t + left_f) * (right_t + right_f)
    false_evals = total_evals - true_evals
    
    t_ways += true_evals
    f_ways += total_evals - true_evals

  cache[exp[left:right]] = (t_ways, f_ways)
  return cache[exp[left:right]]

def boolean_evaluation(exp):
  return count_eval(exp, 0, len(exp), {})

def test():
  exp = ''
  print('PASS' if boolean_evaluation(exp) == (0,0) else 'FAIL')
  
  exp = '1'
  print('PASS' if boolean_evaluation(exp) == (1,0) else 'FAIL')
  
  exp = '0'
  print('PASS' if boolean_evaluation(exp) == (0,1) else 'FAIL')
  
  exp = '1&0'
  print('PASS' if boolean_evaluation(exp) == (0,1) else 'FAIL')
  
  exp = '1&1'
  print('PASS' if boolean_evaluation(exp) == (1,0) else 'FAIL')
  
  exp = '1|0'
  print('PASS' if boolean_evaluation(exp) == (1,0) else 'FAIL')
  
  exp = '0|0'
  print('PASS' if boolean_evaluation(exp) == (0,1) else 'FAIL')
  
  exp = '1^0'
  print('PASS' if boolean_evaluation(exp) == (1,0) else 'FAIL')
  
  exp = '0^0'
  print('PASS' if boolean_evaluation(exp) == (0,1) else 'FAIL')
  
  exp = '1^0|0|1'
  print('PASS' if boolean_evaluation(exp) == (3,2) else 'FAIL')
  
  exp = '0&0&0&1^1|0'
  print('PASS' if boolean_evaluation(exp) == (10,32) else 'FAIL')
  
if __name__ == "__main__":
  test()
  
