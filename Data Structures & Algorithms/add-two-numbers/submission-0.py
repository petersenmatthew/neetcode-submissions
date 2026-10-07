# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 9 -> 1
        # 9 -> 1

        # 19 + 19 = 38

        # 9 + 9 - > 8 '1 + 1 
        # if num + num > 9, bring a carry over to next
        result = ListNode()
        current = result
        carry = 0
        while l1 or l2 or carry != 0:
            digit_added = 0
            if l1 is None and l2 is None:
                digit_added = carry
            elif l1 is None:
                digit_added = l2.val + carry
            elif l2 is None:
                digit_added = l1.val + carry
            else:
                digit_added = l1.val + l2.val + carry
            if digit_added > 9:
                carry = 1
            else:
                carry = 0
            current.next = ListNode(digit_added % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return result.next