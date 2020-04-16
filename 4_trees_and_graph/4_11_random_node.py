from random import randint

class BiNode:
  def __init__(self, *, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
    self.size = 1
    
  def find(self, data):
    if data == self.data:
      return self
    elif data < self.data:
      return self.left.find(data) if self.left else None
    else:
      return self.right.find(data) if self.right else None
    
  def insert(self, data):
    self.size += 1
    if data <= self.data:
      if self.left:
        self.left.insert(data)
      else:
        self.left = BiNode(data=data)
    else:
      if self.right:
        self.right.insert(data)
      else:
        self.right = BiNode(data=data)
  
  def get_ith_node(self, i):
    left_size = self.left.size if self.left else 0
    if i == left_size + 1:
      return self
    elif i <= left_size:
      return self.left.get_ith_node(i)
    else:
      return self.right.get_ith_node(i-left_size-1)
    
  def delete(self, data, parent):
    if data == self.data:
      # leaf or has a single child
      # link the single child directly to parent
      if not self.left or not self.right:
        # if self.data > parent.data:
        #   parent.right = self.left if self.left else self.right
        # else:
        #   parent.left = self.left if self.left else self.right
        setattr(parent,
                "right" if self.data > parent.data else "left",
                self.left if self.left else self.right,
                )
        return self
      
      # 2 children
      else:
        successor = self.right.get_successor()
        if self.right is not successor:
          successor.right = self.right
        successor.left, successor.size = self.left, self.size-1
        # if self.data > parent.data:
        #   parent.right = successor
        # else:
        #   parent.left = successor
        setattr(parent, 
                "right" if self.data > parent.data else "left",
                successor,
                )
        return self

    elif data < self.data and not self.left or data > self.data and not self.right:
      return None
    else:
      r = getattr(self, "left" if data < self.data else "right").delete(data, self)
      if r:
        self.size -= 1 
      return r 
  
  def get_successor(self):
    if self.left is None:
      return self
    successor = self.left.get_successor()
    if successor is self.left:
      self.left = successor.right
    if successor:
      self.size -= 1
    return successor
    
class Tree:
  def __init__(self):
    self.size = 0
    self.root = None
  
  def insert(self, data):
    self.size += 1
    if self.root:
      self.root.insert(data)
    else:
      self.root = BiNode(data=data)
      
  def find(self, data):
    if self.root:
      return self.root.find(data)
    else:
      return None
  
  def get_random_node(self):
    if self.root:
      i = randint(1, self.size)
      return self.root.get_ith_node(i)
    else:
      return None
  
  def delete(self, data):
    if not self.root:
      return None
    else:
      if self.root.data != data:
        r = getattr(self.root, "left" if data < self.root.data else "right").delete(data, self.root)
      else:
        r = self.root
        if not self.root.left or not self.root.right:
          self.root = self.root.left if self.root.left else self.root.right
        else:
          successor = self.root.right.get_successor()
          if successor is not self.root.right:
            successor.right = self.root.right
          successor.left = self.root.left
          self.root = successor
      self.size -= 1 if r else 0
      if self.root:
        self.root.size = self.size 
      return r
    
def test_get_successor():
  print("TEST get_successor")
  t = Tree()
  t.insert(10)
  t.insert(8)
  t.insert(5)
  t.insert(6)
  print('PASS' if t.root.get_successor().data == 5 else 'FAIL')
  print('PASS' if t.root.size == 3 else 'FAIL')
  
  print('PASS' if t.root.get_successor().data == 6 else 'FAIL')
  print('PASS' if t.root.size == 2 else 'FAIL')
  print('PASS' if t.root.left.size == 1 else 'FAIL')
  
  print('PASS' if t.root.get_successor().data == 8 else 'FAIL')
  print('PASS' if t.root.size == 1 else 'FAIL')
  
  print('PASS' if t.root.get_successor().data == 10 else 'FAIL')
  print('PASS' if t.root.size == 1 else 'FAIL')

def test_tree_delete():
  print("TEST Tree's delete")
  t = Tree()
  print('PASS' if not t.delete(5) else 'FAIL')
  t.insert(5)
  t.insert(5)
  t.insert(10)
  t.insert(8)

  print('PASS' if t.delete(5).data == 5 else 'FAIL')
  print('PASS' if t.root.data == 8 else 'FAIL')
  print('PASS' if t.size == 3 else 'FAIL')
  
  print('PASS' if t.delete(8).data == 8 else 'FAIL')
  print('PASS' if t.root.data == 10 else 'FAIL')
  print('PASS' if t.size == 2 else 'FAIL')
  
  print('PASS' if t.delete(10).data == 10 else 'FAIL')
  print('PASS' if t.root.data == 5 else 'FAIL')
  print('PASS' if t.size == 1 else 'FAIL')
  
  print('PASS' if t.delete(5).data == 5 else 'FAIL')
  print('PASS' if not t.root else 'FAIL')
  print('PASS' if t.size == 0 else 'FAIL')
     
def test():
  t = Tree()
  print('PASS' if not t.find(5) else 'FAIL')
  print('PASS' if not t.get_random_node() else 'FAIL')
  
  t.insert(5)
  print('PASS' if t.find(5) else 'FAIL')
  print('PASS' if t.size == 1 else 'FAIL')
  print('PASS' if t.get_random_node().data == 5 else 'FAIL')
  
  t.insert(5)
  t.insert(10)
  t.insert(1)
  t.insert(10)
  t.insert(15)
  t.insert(3)
  print('PASS' if t.find(1) else 'FAIL')
  print('PASS' if t.find(3) else 'FAIL')
  print('PASS' if t.find(15) else 'FAIL')
    
  sizes = [2,1,3,7,1,3,1]
  datas = [1,3,5,5,10,10,15]
  for i in range(1, t.size):
    print ('PASS' if t.root.get_ith_node(i).data == datas[i-1] else 'FAIL')
    print ('PASS' if t.root.get_ith_node(i).size == sizes[i-1] else 'FAIL')
    
  print('PASS' if not t.delete(20) else 'FAIL')
  
  print('PASS' if t.delete(1).data == 1 else 'FAIL')
  print('PASS' if t.size == 6 else 'FAIL')
  sizes = [1,2,6,1,3,1]
  datas = [3,5,5,10,10,15]
  for i in range(1, t.size):
    print ('PASS' if t.root.get_ith_node(i).data == datas[i-1] else f'{i}FAIL')
    print ('PASS' if t.root.get_ith_node(i).size == sizes[i-1] else f'{i}FAIL')
    
  print('PASS' if t.delete(3).data == 3 else 'FAIL')
  print('PASS' if t.size == 5 else 'FAIL')
  sizes = [1,5,1,3,1]
  datas = [5,5,10,10,15]
  for i in range(1, t.size):
    print ('PASS' if t.root.get_ith_node(i).data == datas[i-1] else f'{i}FAIL')
    print ('PASS' if t.root.get_ith_node(i).size == sizes[i-1] else f'{i}FAIL')
  
  print('PASS' if t.delete(10).data == 10 else 'FAIL')
  print('PASS' if t.size == 4 else 'FAIL')
  sizes = [1,4,1,2]
  datas = [5,5,10,15]
  for i in range(1, t.size):
    print ('PASS' if t.root.get_ith_node(i).data == datas[i-1] else f'{i}FAIL')
    print ('PASS' if t.root.get_ith_node(i).size == sizes[i-1] else f'{i}FAIL')
    
  print('PASS' if t.delete(5).data == 5 else 'FAIL')
  print('PASS' if t.size == 3 else 'FAIL')
  sizes = [1,3,1]
  datas = [5,10,15]
  for i in range(1, t.size):
    print ('PASS' if t.root.get_ith_node(i).data == datas[i-1] else f'{i}FAIL')
    print ('PASS' if t.root.get_ith_node(i).size == sizes[i-1] else f'{i}FAIL')

if __name__ == '__main__':
  test_tree_delete()
  test_get_successor()
  test()
