# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # get to middle

        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.val)
        mid = slow

        # reverse second half
        cur = slow.next
        slow.next = None

        prev = None
        while cur:  
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        print(mid.val)

        left = head
        right = prev
        while right:
            left_next = left.next
            right_next = right.next

            left.next = right
            left = left_next
            right.next = left
            right = right_next
        
            


# odd list
# 0 -> 1 -> 2 - > 6 -> 5 -> 4 -> 3

# even lsit
# 2-> 4-> 8-> 6->