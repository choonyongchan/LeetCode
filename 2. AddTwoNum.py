from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Solution: Use helper ListNode to simplify code
        # Time: O(n)
        # Space: O(n)

        result = ListNode()
        l3 = result

        while l1 or l2:
            v_curr = (l1.val if l1 else 0) + (l2.val if l2 else 0) + l3.val #l3.val as carry
            l3.val = v_curr % 10
            v_curr //= 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if v_curr or l1 or l2:
                l3.next = ListNode(val=v_curr)
                l3 = l3.next

        return result
        

l1 = ListNode(3)
l2 = ListNode(3, ListNode(1))#, ListNode(6, ListNode(4)))
print(Solution().addTwoNumbers(l1, l2).next.val)