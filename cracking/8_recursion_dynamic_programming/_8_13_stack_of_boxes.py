def stack_of_boxes(boxes):
  best_h = 0
  stacks = [0] * len(boxes)
  boxes.sort(key=lambda b: b[1], reverse=True)
  for i in range(len(boxes)):
    h = find_max_stack(boxes, stacks, i)
    if h > best_h:
      best_h = h
  return best_h

def find_max_stack(boxes, stacks, index):
  if stacks[index] != 0:
    return stacks[index]
  best_h = 0
  w, h, d = boxes[index]
  for i in range(index+1, len(boxes)):
    curr_w, _, curr_d = boxes[i]
    if curr_w < w and curr_d < d:
      max_h = find_max_stack(boxes, stacks, i)
      if max_h > best_h:
        best_h = max_h
  stacks[index] = best_h + h
  return stacks[index]

def test():
  boxes = []
  print('PASS' if stack_of_boxes(boxes) == 0 else 'FAIL')
  
  boxes = [(4,5,6)]
  print('PASS' if stack_of_boxes(boxes) == 5 else 'FAIL')
  
  boxes = [(10,10,10), (12,9,10), (9,9,9), (8,8,8), (17,8,10), (2,2,2)]
  print('PASS' if stack_of_boxes(boxes) == 29 else 'FAIL')

if __name__ == '__main__':
  test()
