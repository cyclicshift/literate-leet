# Solution to LeetCode Problem: add-two-numbers
# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = ListNode()
        l3 = x
        val1 = l1.val
        val2 = l2.val

        carry = 0

        while True:
            sum = val1 + val2 + carry
            if sum < 10:
                x.val = sum
                carry = 0
            else:
                x.val = sum - 10
                carry = 1

            if l1 != None:
                l1 = l1.next 
            
            if l2 != None:
                l2 = l2.next

            if l1 == None and l2 == None:
                break
            
            if l1 == None:
                val1 = 0
            else:
                val1 = l1.val
            
            if l2 == None:
                val2 = 0
            else:
                val2 = l2.val

            x.next = ListNode()
            x = x.next

        if carry == 1:
            x.next = ListNode()
            x = x.next
            x.val = 1

        return l3

l1 = ListNode(2,ListNode(4,ListNode(3,None)))
l2 = ListNode(5,ListNode(6,ListNode(4,None)))
s = Solution()
x = s.addTwoNumbers(l1,l2)

while x != None:
    print(x.val)
    x = x.next