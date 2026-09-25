# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # store visited nodes in a set, o(1) lookup o(n) space
        seen = set()
        while head is not None:
            if head in seen:
                return True
            else:
                seen.add(head)
                head = head.next
        
        return False