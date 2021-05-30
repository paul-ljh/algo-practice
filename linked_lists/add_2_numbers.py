'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

EX:
Input:
l1 = 7->2->4->3
l2 = 5->6->4

Output: 7->8->0->7

https://leetcode.com/problems/add-two-numbers-ii/submissions/
'''

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def add_2_numbers(l1, l2):
  result = convert_list_to_num(l1) + convert_list_to_num(l2)
  return convert_num_to_list(result)

def convert_list_to_num(l):
  length = get_linked_list_len(l)
  multiplier = pow(10, length - 1)
  result = 0
  while l != None:
    result += l.val * multiplier
    l = l.next
    multiplier //= 10
  return result

def get_linked_list_len(l):
  result = 0
  while l != None:
    result += 1
    l= l.next
  return result

def convert_num_to_list(num):
  l = None
  while num != 0:
    remainder = num % 10
    num //= 10
    l = ListNode(remainder, l)
  return l or ListNode(0)
